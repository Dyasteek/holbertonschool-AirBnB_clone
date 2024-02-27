#!/usr/bin/python3
"""Start the File Storage class"""
import models.engine.file_storage as file_storage


storage = file_storage.FileStorage()
storage.reload()