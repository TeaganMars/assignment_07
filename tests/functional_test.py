import os
import sys
import random
import unittest
import analytics
import io_geojson
import point
import utils
sys.path.insert(0, os.path.abspath('..'))



class TestFunctionalPointPattern(unittest.TestCase):

    def setUp(self):
        self.marks = ['England', 'France', 'Castile', 'Portugal', 'Burgundy',
                      'Aragon', 'Austria', 'Ming', 'Apache', 'Brittany', 'Muscovy']
        random.seed(12345)
        i = 0
        self.points = []
        while i < 100:
            seed = (round(random.random(), 2), round(random.random(), 2))
            self.points.append(point.Point(seed[0], seed[1], random.choice(self.marks)))
            n_additional = random.randint(5, 10)
            i += 1
            c = random.choice([0, 1])
            if c:
                for j in range(n_additional):
                    x_offset = random.randint(0,10) / 100
                    y_offset = random.randint(0,10) / 100
                    pt = (round(seed[0] + x_offset, 2), round(seed[1] + y_offset, 2))
                    self.points.append(point.Point(pt[0], pt[1], random.choice(self.marks)))
                    i += 1
                    if i == 100:
                        break
            if i == 100:
                break

    def test_point_pattern(self):
        """
        This test checks that the code can compute an observed mean
         nearest neighbor distance and then use Monte Carlo simulation to
         generate some number of permutations.  A permutation is the mean
         nearest neighbor distance computed using a random realization of
         the point process.
        """
        random.seed()  # Reset the random number generator using system time
        # I do not know where you have moved avarege_nearest_neighbor_distance, so update the point_pattern module
        observed_avg = analytics.average_nearest_neighbor_distance(self.points)
        self.assertAlmostEqual(0.027, observed_avg, 3)

        # Again, update the point_pattern module name for where you have placed the point_pattern module
        # Also update the create_random function name for whatever you named the function to generate
        #  random points
        rand_points = utils.generate_random_points(100)
        self.assertEqual(100, len(rand_points))

        # As above, update the module and function name.
        permutations = utils.permutations(99)
        self.assertEqual(len(permutations), 99)
        self.assertNotEqual(permutations[0], permutations[1])

        # As above, update the module and function name.
        lower, upper = utils.crit_tations(permutations)
        self.assertTrue(lower > 0.03)
        self.assertTrue(upper < 0.07)
        self.assertTrue(observed_avg < lower or observed_avg > upper)

        # As above, update the module and function name.
        significant = utils.check_yer_sig(lower, upper, observed_avg)
        self.assertTrue(significant)
