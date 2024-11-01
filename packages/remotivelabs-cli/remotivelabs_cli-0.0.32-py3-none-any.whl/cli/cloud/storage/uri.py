from __future__ import annotations

from os import PathLike
from pathlib import PurePosixPath
from urllib.parse import urlparse


class InvalidURIError(Exception):
    """Raised when an invalid URI is encountered"""


class JoinURIError(Exception):
    """Raised when an error occurs while joining URIs"""


class URI:
    """
    Custom type for rcs (Remotive Cloud Storage) URIs.
    """

    def __init__(self, value: str, scheme: str = "rcs"):
        self.original_uri = value
        self.scheme = scheme

        parsed = urlparse(value)
        if parsed.scheme != self.scheme:
            raise InvalidURIError(f"Invalid URI scheme. Expected '{self.scheme}://', got '{parsed.scheme}://'")
        if parsed.netloc.startswith((".", "-", "#", " ", "/", "\\")):
            raise InvalidURIError(f"Invalid URI. Path cannot start with invalid characters: '{value}'")
        if not parsed.netloc and parsed.path == "/":
            raise InvalidURIError(f"Invalid URI: '{value}'")

        self.path = f"/{parsed.netloc}{parsed.path}" if parsed.netloc else f"/{parsed.path}"

        self._posix_path = PurePosixPath(self.path)
        self.filename = self._posix_path.name

    def is_dir(self) -> bool:
        return self.path.endswith("/")

    def __truediv__(self, other: PathLike[str] | str) -> URI:
        """Returns a new URI object with the joined path"""
        if str(other).startswith("/"):
            raise JoinURIError(f"Cannot join absolute path '{other}' to URI")

        new_path = self._posix_path / other

        # handle relative paths
        for part in new_path.parts:
            if part == "..":
                new_path = new_path.parent
            elif part != ".":
                new_path = new_path / part

        new_uri = f"{self.scheme}://{new_path.relative_to('/')}"  # we need to strip the starting '/'
        return URI(new_uri, scheme=self.scheme)

    def __str__(self) -> str:
        return self.original_uri
