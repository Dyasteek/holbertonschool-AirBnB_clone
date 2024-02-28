#!/usr/bin/python3
"""Unittest for models/amenity.py"""
import unittest
from models.amenity import Amenity


class to_Test_Amenity(unittest.TestCase):
    """Class for testing Amenity class"""

    def test_amenity_is_instance(self):
        """Test Amenity instance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_name_str(self):
        """Test Amenity name"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_id_str(self):
        """Test Amenity id"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

class to_Test_Amenity_save(unittest.TestCase):
    """Class for testing Amenity save method"""

    def test_amenity_save_updated_at(self):
        """Test Amenity save updated_at"""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

    def test_amenity_save_with_arg(self):
        """Test Amenity save with arg"""
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

class to_Test_Amenity_to_dict(unittest.TestCase):
    """Class for testing Amenity to_dict method"""

    def test_amenity_to_dict_dict(self):
        """Test Amenity to_dict"""
        amenity = Amenity()
        self.assertIsInstance(amenity.to_dict(), dict)

    def test_amenity_to_dict_with_arg(self):
        """Test Amenity to_dict with arg"""
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)
