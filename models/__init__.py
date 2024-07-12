#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage


"""Grace checks the value of HBNB_TYPE_STORAGE environment variable"""
if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()
    """Call relaod() to initialize the storage"""
storage.reload()
