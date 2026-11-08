import unittest
from pathlib import Path

from pyeqsolver.parser import EquationParser
from pyeqsolver.exceptions import InvalidFileFormatException

DATA_DIR = Path(__file__).parent / "data"


class TestEquationParser(unittest.TestCase):

    def test_case10_invalid_format(self):
        with self.assertRaises(InvalidFileFormatException) as context:
            EquationParser(DATA_DIR / "case10.txt").parse()

        self.assertIn("Line 1", str(context.exception))

    def test_case11_invalid_characters(self):
        with self.assertRaises(InvalidFileFormatException):
            EquationParser(DATA_DIR / "case11.txt").parse()

    def test_case12_empty_file(self):
        with self.assertRaises(InvalidFileFormatException):
            EquationParser(DATA_DIR / "case12.txt").parse()

    def test_case13_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            EquationParser(DATA_DIR / "does_not_exist.txt").parse()


if __name__ == "__main__":
    unittest.main()