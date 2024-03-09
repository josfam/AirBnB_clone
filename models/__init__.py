"""Defines models to be used in the project"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
