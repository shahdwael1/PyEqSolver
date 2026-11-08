class PyEqSolverError(Exception):
    pass


class InvalidFileFormatException(PyEqSolverError):
    def __init__(self, line_number=None, line=None, message=None):

        if message is not None:
            error_message = message
        elif line_number is None:
            error_message = "The file contains no equations"
        else:
            error_message = f'Line {line_number}: invalid format in "{line}"'

        super().__init__(error_message)


class DimensionMismatchException(PyEqSolverError):
    def __init__(self, num_equations, variables):

        if isinstance(variables, int):
            num_variables = variables
            variable_names = ""
        else:
            num_variables = len(variables)
            variable_names = f" ({', '.join(variables)})"

        message = (
            f"{num_equations} equations for "
            f"{num_variables} variables{variable_names}"
        )

        super().__init__(message)


class InconsistentSystemException(PyEqSolverError):
    def __init__(self, constant):
        message = (
            f"The system has no solution "
            f"(row reduces to 0 = {constant:g})"
        )
        super().__init__(message)


class InfiniteSolutionsException(PyEqSolverError):
    def __init__(self, rank, num_variables):
        message = (
            f"Infinitely many solutions: "
            f"rank {rank} < {num_variables} variables"
        )
        super().__init__(message)
