from __future__ import annotations

from typing import Union, Tuple, Optional
import re
from functools import total_ordering


@total_ordering
class Version:
    """A class to represent and compare package versions.

    This class handles version numbers in both string ("x.y.z") and tuple ((x,y,z))
    formats, providing comparison operations and string representations.

    Parameters
    ----------
    version : Union[str, Tuple[int, ...], 'Version']
        The version information in one of the following formats:
        - String: "major.minor.micro" or "major.minor"
        - Tuple: (major, minor, micro) or (major, minor)
        - Version: another Version instance

    Attributes
    ----------
    major : int
        The major version number
    minor : int
        The minor version number
    micro : int
        The micro (patch) version number

    Raises
    ------
    ValueError
        If the version format is invalid or contains non-integer values
    TypeError
        If the version input is of an unsupported type

    Examples
    --------
    >>> v1 = Version("1.2.3")
    >>> v2 = Version((1, 2))
    >>> v1 > v2
    True
    >>> str(v1)
    '1.2.3'
    """

    # Regular expression for validating version strings
    _VERSION_PATTERN = re.compile(r'^\d+(\.\d+){1,2}$')

    def __init__(
        self,
        version: Union[str, Tuple[int, ...], 'Version']
    ) -> None:
        """Initialize a Version instance."""
        self.major: int = 0
        self.minor: int = 0
        self.micro: int = 0

        if isinstance(version, str):
            self._parse_version_string(version)
        elif isinstance(version, tuple):
            self._parse_version_tuple(version)
        elif isinstance(version, Version):
            self._copy_version(version)
        else:
            raise TypeError(
                f"Version must be a string, tuple, or Version instance, "
                f"not {type(version).__name__}"
            )

    def _parse_version_string(self, version: str) -> None:
        """Parse a version string into its components.

        Parameters
        ----------
        version : str
            Version string in the format "x.y.z" or "x.y"

        Raises
        ------
        ValueError
            If the version string format is invalid
        """
        if not self._VERSION_PATTERN.match(version):
            raise ValueError(
                "Invalid version string format. Expected 'x.y.z' or 'x.y'"
            )

        try:
            parts = [int(part) for part in version.split('.')]
        except ValueError as e:
            raise ValueError("Version components must be valid integers") from e

        if len(parts) == 2:
            self.major, self.minor = parts
            self.micro = 0
        else:
            self.major, self.minor, self.micro = parts

    def _parse_version_tuple(self, version: Tuple[int, ...]) -> None:
        """Parse a version tuple into its components.

        Parameters
        ----------
        version : Tuple[int, ...]
            Version tuple in the format (x, y, z) or (x, y)

        Raises
        ------
        ValueError
            If the tuple length is invalid or contains non-integer values
        """
        if not (2 <= len(version) <= 3):
            raise ValueError("Version tuple must have 2 or 3 elements")

        if not all(isinstance(part, int) for part in version):
            raise ValueError("All version components must be integers")

        if len(version) == 2:
            self.major, self.minor = version
            self.micro = 0
        else:
            self.major, self.minor, self.micro = version

    def _copy_version(self, version: 'Version') -> None:
        """Copy version components from another Version instance.

        Parameters
        ----------
        version : Version
            Source Version instance to copy from
        """
        self.major = version.major
        self.minor = version.minor
        self.micro = version.micro

    def to_tuple(self) -> Tuple[int, int, int]:
        """Convert the version to a tuple representation.

        Returns
        -------
        Tuple[int, int, int]
            Version components as a tuple (major, minor, micro)
        """
        return (self.major, self.minor, self.micro)

    def __eq__(self, other: object) -> bool:
        """Compare two versions for equality."""
        if not isinstance(other, (Version, str, tuple)):
            return NotImplemented
        other_version = Version(other) if not isinstance(other, Version) else other
        return self.to_tuple() == other_version.to_tuple()

    def __lt__(self, other: Union[Version, str, Tuple[int, ...]]) -> bool:
        """Compare if this version is less than another version."""
        if not isinstance(other, (Version, str, tuple)):
            return NotImplemented
        other_version = Version(other) if not isinstance(other, Version) else other
        return self.to_tuple() < other_version.to_tuple()

    def __repr__(self) -> str:
        """Return a detailed string representation of the Version instance."""
        return (f"{self.__class__.__name__}("
                f"major={self.major}, minor={self.minor}, micro={self.micro})")

    def __str__(self) -> str:
        """Return a string representation of the version."""
        return f"{self.major}.{self.minor}.{self.micro}"