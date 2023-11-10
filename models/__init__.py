#!/usr/bin/python3
"""
This module always runs at the start of the
program, and loads the stored instances to memory
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
