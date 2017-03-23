import unittest
import random
import point
import utils
from point import Point

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Seed a random number generator so we get the same random values every time
        random.seed(12345)
        # A list comprehension to create 50 random points
        self.points = [(random.randint(0, 100), random.randint(0, 100)) for i in range(50)]
        self.marks = ['England', 'France', 'Castile', 'Portugal', 'Burgundy',
                      'Aragon', 'Austria', 'Ming', 'Apache', 'Brittany', 'Muscovy']

    def test_test_coincident(self):
        point_a = point.Point(9, 7, random.choice(self.marks))
        point_b = point.Point(22, 13, random.choice(self.marks))
        point_c = point.Point(9, 7, random.choice(self.marks))
        self.assertTrue(point_a.test_coincident(point_c.get_point()))
        self.assertFalse(point_a.test_coincident(point_b.get_point()))

    def test_shift(self):
        original_point = point.Point(13, 21, random.choice(self.marks))
        original_point.shift(7, 11)
        self.assertEqual((20, 32), original_point.get_point())

    def test_markers(self):
        some_marks = list()
        count_marks = dict()
        variable = 1
        for a in range(10):
            some_marks.append(random.choice(self.marks))
        for a in range(len(some_marks)):
            for b in range(len(some_marks)):
                if some_marks[a] == some_marks[b]:
                    variable += 1
                else:
                    continue
            count_marks[some_marks[a]] = variable - 1
        self.assertTrue(count_marks['Ming'], 1)
        self.assertTrue(count_marks['Aragon'], 1)

    def test_magic_methods(self):
        point_a = Point(9, 7)
        point_b = Point(22, 13)
        point_c = Point(31, 20)
        point_d = Point(-13, -6)
        self.assertEqual(point_a + point_b, point_c)
        self.assertEqual(point_a - point_b, point_d)
        self.assertEqual(abs(point_d), Point(13, 6))
