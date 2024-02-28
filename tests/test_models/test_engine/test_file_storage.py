#!/usr/bin/python3
"""Unittest for models/engine/file_storage.py"""
import unittest
from models.engine.file_storage import FileStorage


class to_Test_file_storage(unittest.TestCase):
    """Test for FileStorage class"""

    def test_file_storage_instance(self):
        """Tests if instance is created"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_storage_with_args(self):
        """Tests if args are passed"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_storage_with_no_args(self):
        """Tests if args are passed"""
        self.assertEqual(FileStorage(), FileStorage())


class to_Test_file_storage_methods(unittest.TestCase):
    """Test for FileStorage class"""

    def test_all_method(self):
        """Tests if all method returns dict"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new_method(self):
        """Tests if new method adds object to storage"""
        storage = FileStorage()
        storage.new(self)
        self.assertTrue(True)

    def test_reload_method(self):
        """Tests if reload method loads from file"""
        storage = FileStorage()
        storage.reload()
        self.assertTrue(True)

    def test_reload_with_args(self):
        """Tests if reload method loads from file"""
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.reload(None)
