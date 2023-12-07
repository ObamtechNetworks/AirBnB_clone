#!/usr/bin/python3
"""the init package file"""

# import the FileStorage class from the file_storage module
from .engine.file_storage import FileStorage
# create dummy attributes as arguments for filestorage
storage = FileStorage('file.json', {})
storage.reload()
