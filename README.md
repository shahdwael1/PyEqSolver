# PyEqSolver

PyEqSolver is a Python package that parses and solves systems of linear equations using Gaussian Elimination with partial pivoting.

## Features

- Reads linear equations from a text file.
- Supports positive and negative coefficients, integers, and decimals.
- Builds an augmented matrix automatically.
- Solves systems using Gaussian Elimination.
- Uses partial pivoting for numerical stability.
- Handles different system outcomes:
  - Unique solution.
  - No solution.
  - Infinitely many solutions.
  - Dimension mismatch.
- Exports results and errors to JSON.
- Includes unit tests using Python's built-in `unittest` framework.

## Project Structure

```text
pyeqsolver-project/
├── pyeqsolver/
│   ├── __init__.py
│   ├── parser.py
│   ├── solver.py
│   ├── exporter.py
│   └── exceptions.py
├── tests/
│   ├── test_parser.py
│   ├── test_solver.py
│   └── data/
├── data/
│   ├── input_equations.txt
│   └── solution.json
├── main.py
└── README.md
```

## Requirements

- Python 3.10 or higher.
- No third-party libraries required.

## Input Format

Write one equation per line in `data/input_equations.txt`.

Example:

```text
2x + 3y = 8
x - y = 1
```

## How to Run

From the project root directory, run:

```bash
python main.py
```

The results will be saved to:

```text
data/solution.json
```

## Running Tests

Run all unit tests using:

```bash
python -m unittest discover -s tests -v
```

## Error Handling

The package handles the following exceptions:

- `InvalidFileFormatException`
- `DimensionMismatchException`
- `InconsistentSystemException`
- `InfiniteSolutionsException`
- `FileNotFoundError`

## License

This project was developed as a Python programming project.