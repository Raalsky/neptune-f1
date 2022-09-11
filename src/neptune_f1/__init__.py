from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("neptune-f1")
except PackageNotFoundError:
    # package is not installed
    pass

__all__ = ["__version__"]
