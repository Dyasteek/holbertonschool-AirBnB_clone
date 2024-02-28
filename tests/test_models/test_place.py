#!/usr/bin/python3
"""Unittest for models/place.py"""
import unittest
from models.place import Place


class to_Test_Place(unittest.TestCase):
    """Test for Place class"""

    def test_place_is_instance(self):
        """Test if Place is an instance of Place"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_name_str(self):
        """Test if name is a string"""
        place = Place()
        self.assertIsInstance(place.name, str)

    def test_place_id_str(self):
        """Test if id is a string"""
        place = Place()
        self.assertIsInstance(place.id, str)

    def test_place_city_id_str(self):
        """Test if city_id is a string"""
        place = Place()
        self.assertIsInstance(place.city_id, str)

    def test_place_user_id_str(self):
        """Test if user_id is a string"""
        place = Place()
        self.assertIsInstance(place.user_id, str)

    def test_place_description_str(self):
        """Test if description is a string"""
        place = Place()
        self.assertIsInstance(place.description, str)

    def test_place_number_rooms_int(self):
        """Test if number_rooms is an integer"""
        place = Place()
        self.assertIsInstance(place.number_rooms, int)

    def test_place_number_bathrooms_int(self):
        """Test if number_bathrooms is an integer"""
        place = Place()
        self.assertIsInstance(place.number_bathrooms, int)

    def test_place_max_guest_int(self):
        """Test if max_guest is an integer"""
        place = Place()
        self.assertIsInstance(place.max_guest, int)

    def test_place_price_by_night_int(self):
        """Test if price_by_night is an integer"""
        place = Place()
        self.assertIsInstance(place.price_by_night, int)

    def test_place_latitude_float(self):
        """Test if latitude is a float"""
        place = Place()
        self.assertIsInstance(place.latitude, float)

    def test_place_longitude_float(self):
        """Test if longitude is a float"""
        place = Place()
        self.assertIsInstance(place.longitude, float)

    def test_place_amenity_ids_list(self):
        """Test if amenity_ids is a list"""
        place = Place()
        self.assertIsInstance(place.amenity_ids, list)

class to_Test_Place_save(unittest.TestCase):
    """Test for Place class"""

    def test_place_save_with_arg(self):
        """Test if save with arg works"""
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

class to_Test_Place_to_dict(unittest.TestCase):
    """Test for Place class"""

    def test_place_to_dict_dict(self):
        """Test if to_dict returns a dictionary"""
        place = Place()
        self.assertIsInstance(place.to_dict(), dict)

    def test_place_to_dict_contains_correct_keys(self):
        """Test if to_dict contains the correct keys"""
        place = Place()
        self.assertIn('id', place.to_dict())
        self.assertIn('created_at', place.to_dict())
        self.assertIn('updated_at', place.to_dict())

    def test_place_to_dict_contains_added_attributes(self):
        """Test if to_dict contains added attributes"""
        place = Place()
        place.name = 'Holberton'
        place.number_rooms = 98
        self.assertIn('name', place.to_dict())
        self.assertIn('number_rooms', place.to_dict())

    def test_place_to_dict_with_arg(self):
        """Test if to_dict with arg works"""
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)
