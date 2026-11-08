import sys

from pyeqsolver import EquationParser, GaussianSolver, JSONExporter
from pyeqsolver.exceptions import PyEqSolverError


def main():

    input_path = "data/input_equations.txt"
    output_path = "data/solution.json"

    exporter = JSONExporter(output_path)

    try:
        # 1. Parse equations
        parser = EquationParser(input_path)
        matrix, variables = parser.parse()

        # 2. Solve the system
        solver = GaussianSolver(matrix, variables)
        solutions = solver.solve()

        # 3. Get metadata
        metadata = solver.get_metadata()

        # 4. Export the solution
        exporter.save(solutions, metadata)

        print(f"Solved. Results written to {output_path}")

    except (PyEqSolverError, FileNotFoundError) as error:

        exporter.save_error(error)

        print(f"Could not solve the system: {error}")

        sys.exit(1)


if __name__ == "__main__":
    main()