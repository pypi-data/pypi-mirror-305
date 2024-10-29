from __future__ import annotations

from typing import Any, Literal, Union, cast

import importlib.resources as rs
import math

from collections.abc import Iterable
from functools import reduce
from operator import xor

import numpy as np

from .card import Card

__all__ = ["AVOGADRO", "Element", "Composition", "Material"]

AVOGADRO = 6.0221408576e23
MATERIAL_FRACTION_FORMAT = "{0:.6e}"
_CHARGE_TO_NAME: dict[int, str] = {}
_NAME_TO_CHARGE: dict[str, int] = {}
_NATURAL_ABUNDANCE: dict[int, dict[int, float]] = {}
_ISOTOPE_MASS: dict[int, dict[int, float]] = {}

with rs.as_file(rs.files(__package__).joinpath("data/isotopes.dat")) as p:
    with p.open() as f:
        for line in f:
            str_number, name, *data = line.split()
            number = int(str_number)
            name = name.upper()
            _CHARGE_TO_NAME[number] = name
            _NAME_TO_CHARGE[name] = number
            _NATURAL_ABUNDANCE[number] = {}
            _ISOTOPE_MASS[number] = {}
            for i in range(len(data) // 3):
                isotope = int(data[i * 3])
                _ISOTOPE_MASS[number][isotope] = float(data[i * 3 + 1])
                abundance = data[i * 3 + 2]
                if abundance != "*":
                    _NATURAL_ABUNDANCE[number][isotope] = float(abundance) / 100.0


TFraction = tuple[Union["Element", int, str], float]
TFractions = Iterable[TFraction]


class Composition(Card):
    """Represents composition.

    Composition is not a material. It specifies only isotopes and their
    fractions. It doesn't concern absolute quantities like density and
    concentration. Composition immediately corresponds to the MCNP's
    material.

    weight and atomic are both lists of tuples: (element, fraction, ...).

    Parameters
    ----------
    atomic : list
        Atomic fractions.
    weight : list
        Weight fractions.
    options : dict
        Dictionary of composition options.

    Methods:
    --------
    molar_mass()
        Gets molar mass of the composition.
    get_atomic(isotope)
        Gets atomic fraction of the isotope.
    get_weight(isotope)
        Gets weight fraction of the isotope.
    expand()
        Expands natural abundance elements into detailed isotope composition.
    natural(tolerance)
        Try to replace detailed isotope composition with natural elements.
    """

    _tolerance = 1.0e-3
    """Relative composition element concentration equality tolerance."""

    # TODO dvp: are there specs using both atomic and weight definitions?
    def __init__(
        self, atomic: TFractions | None = None, weight: TFractions | None = None, **options: Any
    ):
        Card.__init__(self, **options)
        self._composition: dict[Element, float] = {}
        elem_w = []
        frac_w = []

        if weight:
            for elem, frac in weight:
                if not isinstance(elem, Element):
                    elem = Element(elem)  # noqa: PLW2901 - elem is to be overwritten
                elem_w.append(elem)
                frac_w.append(frac)

        elem_a = []
        frac_a = []
        if atomic:
            for elem, frac in atomic:
                if not isinstance(elem, Element):
                    elem = Element(elem)  # noqa: PLW2901 - elem is to be overwritten
                elem_a.append(elem)
                frac_a.append(frac)

        if len(frac_w) + len(frac_a) > 0:
            total_frac_w = np.sum(frac_w)
            total_frac_a = np.sum(frac_a)
            atoms_in_weight_spec = np.sum(np.divide(frac_w, [e.molar_mass for e in elem_w]))
            mass_in_atomic_spec = np.sum(np.multiply(frac_a, [e.molar_mass for e in elem_a]))

            totals_diff = total_frac_a - total_frac_w
            sq_root = np.sqrt(totals_diff**2 + 4 * atoms_in_weight_spec * mass_in_atomic_spec)
            if totals_diff <= 0:
                self._molar_mass: float = 0.5 * (sq_root - totals_diff) / atoms_in_weight_spec
            else:
                self._molar_mass = 2 * mass_in_atomic_spec / (sq_root + totals_diff)

            norm_factor = self._molar_mass * atoms_in_weight_spec + total_frac_a
            for el, frac in zip(elem_w, frac_w, strict=False):
                if el not in self._composition.keys():
                    self._composition[el] = 0.0
                self._composition[el] += self._molar_mass / norm_factor * frac / el.molar_mass
            for el, frac in zip(elem_a, frac_a, strict=False):
                if el not in self._composition.keys():
                    self._composition[el] = 0.0
                self._composition[el] += frac / norm_factor
        else:
            raise ValueError("Incorrect set of parameters.")
        self._hash = reduce(xor, map(hash, self._composition.keys()))

    def copy(self) -> Composition:
        return Composition(atomic=cast(TFractions, self._composition.items()), **self.options)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Composition):
            return False
        if len(self._composition.keys()) != len(other._composition.keys()):
            return False
        for k1, v1 in self._composition.items():
            v2 = other._composition.get(k1, None)
            if v2 is None:
                return False
            # TODO dvp: this violates exact equality definition, define separate
            #           'approx' object and method for that if exact equality is required
            if not math.isclose(v1, v2, rel_tol=Composition._tolerance):
                return False
        return True

    #
    # TODO dvp: see TODO above, implementation variant
    #
    # from dataclasses import dataclass
    # @dataclass(eq=False, frozen=True)
    # class Approx:
    #      composition: "Composition"
    #      rel_tol: float = 1e-3
    #      abs_tol: float = 1e-12
    #           ...
    #      def __hash__(self):
    #          return hash(self.composition)
    #
    #      def __eq__(self, other)
    #          ...
    # def approx(self, rel_tol=1e-3, abs_tol=1e-12):
    #     return Approx(self, rel_tol=rel_tol, abs_tol=abs_tol)

    def __hash__(self):
        return reduce(
            xor, map(hash, self._composition.keys())
        )  # TODO dvp: check why self._hash is not used?

    def mcnp_words(self, pretty=False):
        words = [f"M{self.name()} "]
        for elem, frac in self._composition.items():
            words.append(elem.mcnp_repr())
            words.append("  ")
            words.append(MATERIAL_FRACTION_FORMAT.format(frac))
            words.append("\n")
        return words

    def __getitem__(self, key):
        return self.options[key]

    def __iter__(self):
        return iter(self._composition.items())

    def __contains__(self, item: str | Element) -> bool:
        """Checks if the composition contains the item.

        Parameters
        ----------
        item :
            Isotope. It can be either isotope name or Element instance.

        Returns:
        -------
        result :
            True if the composition contains the isotope, False otherwise.
        """
        if not isinstance(item, Element):
            item = Element(item)
        return item in self._composition

    def get_atomic(self, isotope: str | Element) -> float:
        """Gets atomic fraction of the isotope.

        Raises KeyError if the composition doesn't contain the isotope.

        Args:
            isotope: Isotope. It can be either isotope name or Element instance.

        Returns:
            Atomic fraction of the specified isotope.
        """
        if not isinstance(isotope, Element):
            isotope = Element(isotope)
        return self._composition[isotope]

    def get_weight(self, isotope: int | Element) -> float:
        """Gets weight fraction of the isotope.

        Raises KeyError if the composition doesn't contain the isotope.

        Args:
            isotope : Isotope. It can be either isotope name or Element instance.

        Returns:
            Weight fraction of the specified isotope.
        """
        if not isinstance(isotope, Element):
            isotope = Element(isotope)
        frac: float = self._composition[isotope] * isotope.molar_mass / self._molar_mass
        return frac

    @property
    def molar_mass(self) -> float:
        """Gets composition's effective molar mass [g / mol]."""
        return self._molar_mass

    def expand(self) -> Composition:
        """Expands elements with natural abundances into detailed isotope composition.

        Returns:
            New expanded composition or self.
        """
        composition: dict[Element, float] = {}
        already = True
        for el, conc in self._composition.items():
            if el.mass_number == 0:
                already = False
            for isotope, frac in el.expand().items():
                if isotope not in composition.keys():
                    composition[isotope] = 0
                composition[isotope] += conc * frac
        if already:
            return self
        return Composition(atomic=composition.items(), **self.options)

    def natural(self, tolerance=1.0e-8) -> Composition | None:
        """Tries to replace detailed isotope composition by natural elements.

        Modifies current object.

        Parameters
        ----------
        tolerance : float
            Relative tolerance to consider isotope fractions as equal.
            Default: 1.e-8

        Returns:
        -------
        comp : Composition
            self, if composition is reduced successfully to natural. None returned if the
            composition cannot be reduced to natural.
        """
        already = True
        by_charge: dict[int, dict[int, float]] = {}
        for elem, fraction in self._composition.items():
            q = elem.charge
            if q not in by_charge.keys():
                by_charge[q] = {}
            a = elem.mass_number
            if a > 0:
                already = False
            if a not in by_charge[q].keys():
                by_charge[q][a] = 0
            by_charge[q][a] += fraction

        if already:  # No need for further checking - only natural elements present.
            return self

        composition: dict[Element, float] = {}
        for q, isotopes in by_charge.items():
            frac_0 = isotopes.pop(0, None)
            tot_frac = sum(isotopes.values())
            for a, fraction in isotopes.items():
                normalized_fraction = fraction / tot_frac
                delta = (
                    2
                    * abs(normalized_fraction - _NATURAL_ABUNDANCE[q][a])
                    / (normalized_fraction + _NATURAL_ABUNDANCE[q][a])
                )
                if delta > tolerance:
                    return None
            elem = Element(q * 1000)
            composition[elem] = tot_frac
            if frac_0:
                composition[elem] += frac_0
        return Composition(atomic=cast(TFractions, composition.items()), **self.options)

    def elements(self) -> Iterable[Element]:
        """Gets iterator over composition's elements."""
        return iter(self._composition.keys())

    @staticmethod
    def mixture(*compositions: tuple[Composition, float]) -> Composition:
        """Makes mixture of the compositions with specific fractions.

        Parameters
        ----------
        compositions :
            List of pairs composition, fraction.

        Returns:
        -------
        mix :
            Mixture.
        """
        atomics = []
        if len(compositions) == 1:
            return compositions[0][0]
        for comp, frac in compositions:
            for elem, atom_frac in comp:
                atomics.append((elem, atom_frac * frac))
        return Composition(atomic=atomics)


def mixture_by_volume(
    *fractions_spec: tuple[Composition, float, float],
    number=0,
) -> tuple[float, Composition]:
    """Compute mix of compositions defined with densities and volume fractions.

    Args:
        fractions_spec: list of specs (Composition, density, volume_fraction)
        number: ... to assign as composition 'name'

    Returns:
        Composition: the mix by atomic fractions
    """
    compositions = [t[0] for t in fractions_spec]
    moles = np.fromiter(
        (
            density * volume_fraction / composition.molar_mass
            for composition, density, volume_fraction in fractions_spec
        ),
        dtype=float,
    )
    total_moles = moles.sum()
    atomic_fractions = moles / total_moles
    mix = Composition.mixture(*zip(compositions, atomic_fractions, strict=False))
    mix.options["name"] = number
    density = sum(density * volume_fraction for _, density, volume_fraction in fractions_spec)
    return density, mix


class Material:
    """Represents material.

    If only one of `weight` or `atomic` parameters is specified, then the Material
    there's no need to normalize it.

    Parameters
    ----------
    atomic : TFractions
        Atomic fractions. New composition will be created.
    weight : TFractions
        Weight fractions of isotopes. density of concentration must present.
    composition : Composition
        Composition instance. If it is specified, then this composition will be
        used. Neither atomic nor weight must be present.
    density : float
        Density of the material (g/cc). It is incompatible with concentration
        parameter.
    concentration : float
        Sets the atomic concentration (1 / cc). It is incompatible with density
        parameter.
    options : dict
        Extra options.

    Properties
    ----------
    density : float
        Density of the material [g/cc].
    concentration : float
        Concentration of the material [atoms/cc].
    composition : Composition
        Material's composition.
    molar_mass : float
        Material's molar mass [g/mol].

    Methods:
    -------
    correct(old_vol, new_vol)
        Correct material density - returns the corrected version of the
        material.
    mixture(*materials, fraction_type)
        Makes a mixture of specified materials in desired proportions.
    __getitem__(key)
        Gets specific option.
    """

    # Relative density tolerance. Relative difference in densities when materials
    _tolerance = 1.0e-3

    def __init__(
        self,
        atomic: TFractions | None = None,
        weight: TFractions | None = None,
        composition: Composition | None = None,
        density: float | None = None,
        concentration: float | None = None,
        **options,
    ):
        # Attributes: _n - atomic density (concentration)
        if isinstance(composition, Composition) and not atomic and not weight:
            self._composition = composition
        elif not composition and (weight or atomic):
            self._composition = Composition(atomic=atomic, weight=weight, **options)
        else:
            raise ValueError("Incorrect set of parameters.")

        if concentration and density or not concentration and not density:
            raise ValueError("Incorrect set of parameters.")
        if concentration is not None:
            self._n = concentration
            if density is not None:
                raise ValueError("Both concentration and density are specified")
        else:
            if density is None:
                raise ValueError("Neither concentration nor density is specified")
            self._n = density * AVOGADRO / self._composition.molar_mass
        self._options = options

    def __eq__(self, other):
        if not math.isclose(self._n, other.concentration, rel_tol=self._tolerance):
            return False
        return self._composition == other.composition

    def __hash__(self):
        return hash(self._composition)

    def __getitem__(self, key):
        return self._options[key]

    @property
    def density(self):
        """Gets material's density [g per cc]."""
        return self._n * self._composition.molar_mass / AVOGADRO

    @property
    def concentration(self):
        """Gets material's concentration [atoms per cc]."""
        return self._n

    @property
    def composition(self):
        """Gets Composition instance that corresponds to the material."""
        return self._composition

    @property
    def molar_mass(self):
        """Gets material's effective molar mass [g / mol]."""
        return self._composition.molar_mass

    def correct(
        self,
        old_vol: float | None = None,
        new_vol: float | None = None,
        factor: float | None = None,
    ) -> Material:
        """Creates new material with fixed density to keep cell's mass.

        Either old_vol and new_vol or factor must be specified.

        Args:
            old_vol: Initial volume of the cell.
            new_vol: New volume of the cell.
            factor : By this factor density of material will be multiplied. If factor
                     is specified, then its value will be used, otherwise - old_vol/new_vol

        Returns:
            New material that takes with corrected density.
        """
        if factor is None:
            if old_vol is None or new_vol is None:
                raise ValueError("'old_vol' is not specified")
            if new_vol is None:
                raise ValueError("'new_vol' is not specified")
            factor = old_vol / new_vol
        return Material(
            composition=self._composition,
            concentration=self._n * factor,
            **self._options,
        )

    @staticmethod
    def mixture(
        *materials: tuple[Material, float],
        fraction_type: Literal["weight", "volume", "atomic"],
    ) -> Material:
        """Creates new material as a mixture of others.

        Volume fractions are not needed to be normalized, but normalization has effect.
        If the sum of fractions is less than 1, then missing fraction is considered
        to be void (density is reduced). If the sum of fractions is greater than 1,
        the effect of compression is taking place. But for weight and atomic fractions
        normalization will be done anyway.

        Args:
            materials: An Iterable of pairs material-fraction. material must be a Material class
                instance because for mixture not only composition but density is
                important.
            fraction_type: Indicate how fraction should be interpreted.
                'weight' - weight fractions (default);
                'volume' - volume fractions;
                'atomic' - atomic fractions.

        Returns:
            New material.
        """
        if not materials:
            raise ValueError("At least one material must be specified.")
        if fraction_type == "weight":

            def fun(m, f):
                return f / m.molar_mass

            norm = sum(fun(m, f) / m.concentration for m, f in materials)
        elif fraction_type == "volume":

            def fun(m, f):
                return f * m.concentration

            norm = 1
        elif fraction_type == "atomic":

            def fun(m, f):
                return f

            norm = sum(fun(m, f) / m.concentration for m, f in materials)
        else:
            raise ValueError("Unknown fraction type")
        factor = sum([fun(m, f) for m, f in materials])
        compositions = [(m.composition, fun(m, f) / factor) for m, f in materials]
        new_comp = Composition.mixture(*compositions)
        return Material(composition=new_comp, concentration=factor / norm)


class Element:
    """Represents isotope or isotope mixture for natural abundance case.

    Attributes:
        _charge: Z of the element,
        _mass_number: A of the element
        _comment: Optional comment to the element.
        _lib:  Data library ID. Usually it is MCNP library, like '31b' for FENDL31b.
        _isomer: Isomer level. Default 0. Usually may appear in FISPACT output.
        _molar: molar mass of the element

    Methods:
        expand()
            Expands natural composition of this element.
        fispact_repr()
            Gets FISPACT representation of the element.
        mcnp_repr()
            Gets MCNP representation of the element.
    """

    def __init__(self, _name: str | int, lib=None, isomer=0, comment=None):
        """Initialize an Element.

        Args:
            _name: Name of isotope. It can be ZAID = Z * 1000 + A, where Z - charge,
            A - the number of protons and neutrons. If A = 0, then natural abundance
            is used. Also, it can be an atom_name optionally followed by '-' and A.
            '-' can be omitted. If there is no A, then A is assumed to be 0.
            comment: Optional comment to the element.
            lib:  Data library ID. Usually it is MCNP library, like '31b' for FENDL31b.
            isomer: Isomer level. Default 0. Usually may appear in FISPACT output.
        """
        if isinstance(_name, int):
            self._charge = _name // 1000
            self._mass_number = _name % 1000
        else:
            z, a = self._split_name(_name.upper())
            if z.isalpha():
                self._charge = _NAME_TO_CHARGE[z]
            else:
                self._charge = int(z)
            self._mass_number = int(a)

        # molar mass calculation
        Z = self._charge
        A = self._mass_number
        if A > 0:
            if A in _ISOTOPE_MASS[Z].keys():
                self._molar = _ISOTOPE_MASS[Z][A]
            else:  # If no data about molar mass present, then mass number
                self._molar = A  # itself is the best approximation.
        else:  # natural abundance
            self._molar = 0.0
            for at_num, frac in _NATURAL_ABUNDANCE[Z].items():
                self._molar += _ISOTOPE_MASS[Z][at_num] * frac
        # Other flags and parameters
        if isinstance(lib, str):
            lib = lib.lower()
        self._lib = lib
        if self._mass_number == 0:
            isomer = 0
        self._isomer = isomer
        self._comment = comment

    def __hash__(self):
        return self._charge * (self._mass_number + 1) * (self._isomer + 1)

    def __eq__(self, other):
        if (
            self._charge == other.charge
            and self._mass_number == other.mass_number
            and self._isomer == other._isomer
        ):
            return True
        return False

    def __str__(self):
        _name = _CHARGE_TO_NAME[self.charge].capitalize()
        if self._mass_number > 0:
            _name += "-" + str(self._mass_number)
            if self._isomer > 0:
                _name += "m"
            if self._isomer > 1:
                _name += str(self._isomer - 1)
        return _name

    def mcnp_repr(self):
        """Gets MCNP representation of the element."""
        _name = str(self.charge * 1000 + self.mass_number)
        if self.lib is not None:
            _name += f".{self.lib}"
        return _name

    def fispact_repr(self):
        """Gets FISPACT representation of the element."""
        _name = _CHARGE_TO_NAME[self.charge].capitalize()
        if self._mass_number > 0:
            _name += str(self._mass_number)
            if self._isomer > 0:
                _name += "m"
            if self._isomer > 1:
                _name += str(self._isomer - 1)
        return _name

    @property
    def charge(self) -> int:
        """Gets element's charge number."""
        return self._charge

    @property
    def mass_number(self):
        """Gets element's mass number."""
        return self._mass_number

    @property
    def molar_mass(self):
        """Gets element's molar mass."""
        return self._molar

    @property
    def lib(self):
        """Gets library name."""
        return self._lib

    @property
    def isomer(self):
        """Gets isomer level."""
        return self._isomer

    def expand(self) -> dict[Element, float]:
        """Expands natural element into individual isotopes.

        Returns:
            A dictionary of elements that are comprised by the isotopes of this one and their fractions.
        """
        result = {}
        if self._mass_number > 0 and self._mass_number in _NATURAL_ABUNDANCE[self._charge].keys():
            result[self] = 1.0
        elif self._mass_number == 0:
            for at_num, frac in _NATURAL_ABUNDANCE[self._charge].items():
                elem_name = f"{self._charge:d}{at_num:03d}"
                result[Element(elem_name, lib=self._lib)] = frac
        return result

    @staticmethod
    def _split_name(_name: str) -> tuple[str, str]:
        """Splits element's name into charge and mass number parts."""
        if _name.isnumeric():
            return _name[:-3], _name[-3:]
        for i, t in enumerate(_name):  # noqa: B007 - `i` is used below
            if t.isdigit():
                break
        else:
            return _name, "0"
        q = _name[: i - 1] if _name[i - 1] == "-" else _name[:i]
        return q, _name[i:]
