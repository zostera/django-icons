__all__ = [
    "__version__",
]

try:
    from importlib.metadata import metadata
except ImportError:
    from importlib_metadata import metadata

meta = metadata("django-icons")

__version__ = meta["Version"]
