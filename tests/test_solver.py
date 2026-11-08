import unittest
from pathlib import Path

from pyeqsolver import EquationParser, GaussianSolver
from pyeqsolver.exceptions import (
    DimensionMismatchException,
    InconsistentSystemException,
    InfiniteSolutionsException
)

DATA_DIR = Path(__file__).parent / "data"


class TestGaussianSolver(unittest.TestCase):

    def solve_case(self, filename):
        parser = EquationParser(DATA_DIR / filename)
        matrix, variables = parser.parse()

        solver = GaussianSolver(matrix, variables)
        return solver.solve()

    def test_case1(self):
        solution = self.solve_case("case1.txt")

        self.assertAlmostEqual(solution["x1"], 0.0, places=4)
        self.assertAlmostEqual(solution["x2"], 1.0, places=4)
        self.assertAlmostEqual(solution["x3"], 2.0, places=4)

    def test_case2(self):
        solution = self.solve_case("case2.txt")

        self.assertAlmostEqual(solution["x"], 1.0, places=4)
        self.assertAlmostEqual(solution["y"], 2.0, places=4)
        self.assertAlmostEqual(solution["z"], 3.0, places=4)

    def test_case3(self):
        solution = self.solve_case("case3.txt")

        self.assertAlmostEqual(solution["a"], 1.0, places=4)
        self.assertAlmostEqual(solution["b"], 2.0, places=4)

    def test_case4(self):
        solution = self.solve_case("case4.txt")

        self.assertAlmostEqual(solution["x"], 1/3, places=4)

    def test_case5(self):
        solution = self.solve_case("case5.txt")

        self.assertAlmostEqual(solution["x"], 2.0, places=4)

    def test_case6(self):
        solution = self.solve_case("case6.txt")

        self.assertAlmostEqual(solution["x"], 2.0, places=4)
        self.assertAlmostEqual(solution["y"], 1.0, places=4)

    def test_case7_inconsistent(self):
        with self.assertRaises(InconsistentSystemException):
            self.solve_case("case7.txt")

    def test_case8_infinite_solutions(self):
        with self.assertRaises(InfiniteSolutionsException):
            self.solve_case("case8.txt")

    def test_case9_dimension_mismatch(self):
        with self.assertRaises(DimensionMismatchException):
            self.solve_case("case9.txt")


if __name__ == "__main__":
    unittest.main()