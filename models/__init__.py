"""Defines models to be used in the project, most of which do inherit their
functionality from BaseModel.
Objects are reconstructed from whatever storage engine is being used, at the
very start of the program.
Storage is globally available to other modules to use.
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
