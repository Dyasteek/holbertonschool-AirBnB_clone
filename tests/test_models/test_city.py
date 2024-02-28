#!/usr/bin/python3
"""Unittest for models/city.py"""
import unittest
from models.city import City


class to_Test_City(unittest.TestCase):
    """Class for testing City class"""

    def test_city_is_instance(self):
        """Test City instance"""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_name_str(self):
        """Test City name"""
        city = City()
        self.assertIsInstance(city.name, str)

    def test_city_id_str(self):
        """Test City id"""
        city = City()
        self.assertIsInstance(city.id, str)

class to_Test_State_save(unittest.TestCase):
    """Class for testing City class"""

    def test_city_save_with_arg(self):
        """Test City save()"""
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

class to_Test_State_to_dict(unittest.TestCase):
    """Class for testing City class"""

    def test_city_to_dict_dict(self):
        """Test City to_dict()"""
        city = City()
        self.assertIsInstance(city.to_dict(), dict)

    def test_city_to_dict_with_arg(self):
        """Test City to_dict()"""
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)
