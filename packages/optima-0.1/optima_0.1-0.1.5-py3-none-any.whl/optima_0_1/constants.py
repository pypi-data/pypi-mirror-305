import os
from enum import Enum

MF_CLIENT = os.path.join(os.getcwd(), "optima_0_1", "unimelb-mf-clients-0.7.8")
MF_UPLOAD_EXECUTABLE = os.path.join(MF_CLIENT, "bin", "unix", "unimelb-mf-upload")
MF_DOWNLOAD_EXECUTABLE = os.path.join(MF_CLIENT, "bin", "unix", "unimelb-mf-download")


class FileType(Enum):
    """
    Enumeration representing different types of files.
    """

    INSTANCE = "instances"
    README = "readme"
    METADATA = "metadata"

    @classmethod
    def list(cls):
        """Return a list of all enum members."""
        return list(cls)

    @classmethod
    def values(cls):
        """Return a list of all enum member values."""
        return [member.value for member in cls]


class StatusMF(Enum):
    """
    Enumeration representing the status of an MediaFlux upload process.
    """

    UPLOAD = "uploaded"
    SKIP = "skipped"
    FAIL = "failed"

    @classmethod
    def list(cls):
        """Return a list of all enum members."""
        return list(cls)


class StatusAPI(Enum):
    """
    Enumeration for outcomes of API requests to the database.
    """

    OK = "ok"
    NOT_FOUND = "not found"
    ERROR = "error"

    @classmethod
    def list(cls):
        """Return a list of all enum members."""
        return list(cls)
