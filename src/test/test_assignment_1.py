import unittest
from src.main.assignment_1 import (
    approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson_method
)

class TestAlgorithms(unittest.TestCase):
    def test_approximation(self):
        f = lambda x: x**2 - 4
        result = approximation_algorithm(f, 2.0)
        self.assertAlmostEqual(result, 2, places=2)

    def test_bisection(self):
        f = lambda x: x**2 - 4
        result = bisection_method(f, 0, 3)
        self.assertAlmostEqual(result, 2, places=2)

    def test_fixed_point(self):
        g = lambda x: (4 + x) / 2
        result = fixed_point_iteration(g, 1.0)
        self.assertAlmostEqual(result, 2, places=2)

    def test_newton_raphson(self):
        f = lambda x: x**2 - 4
        df = lambda x: 2*x
        result = newton_raphson_method(f, df, 3.0)
        self.assertAlmostEqual(result, 2, places=2)

if __name__ == "__main__":
    unittest.main()
