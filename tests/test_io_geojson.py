import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))
import io_geojson


class TestIoGeoJson(unittest.TestCase):
    def setUp(self):
        self.gj = io_geojson.read_geojson('C:/Users/Todd/Documents/GitHub/assignment_06/data/us_cities.GEOJSON')

    def test_read_geojson(self):
        self.assertIsInstance(self.gj, dict)

