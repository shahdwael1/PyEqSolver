from pyeqsolver.exceptions import DimensionMismatchException,InconsistentSystemException,InfiniteSolutionsException

class GaussianSolver:

    def __init__(self, matrix,variables):
        self.matrix = [row[:] for row in matrix]
        self.variables=variables
        self.pivot_columns=[]


    def _forward_elimination(self):
        matrix = self.matrix
        self.pivot_columns = []

        rows = len(matrix)
        cols = len(matrix[0]) - 1

        pivot_row = 0

        for pivot_col in range(cols):

            if pivot_row >= rows:
                break

            best_row = self._find_pivot(pivot_row, pivot_col)

            if abs(matrix[best_row][pivot_col])  < 1e-9:
                continue

            if best_row != pivot_row:
                self._swap_rows(pivot_row, best_row)

            pivot = matrix[pivot_row][pivot_col]

            for r in range(pivot_row + 1, rows):
                factor = matrix[r][pivot_col] / pivot

                for c in range(pivot_col, cols + 1):
                    matrix[r][c] -= factor * matrix[pivot_row][c]

                matrix[r][pivot_col] = 0.0
            self.pivot_columns.append(pivot_col)
            pivot_row += 1

        return matrix


    def _back_substitution(self):
        matrix = self.matrix

        num_variables = len(matrix[0]) - 1
        solution = [0.0] * num_variables

        for i in range(len(self.pivot_columns) - 1, -1, -1):
            pivot_col = self.pivot_columns[i]
            total = matrix[i][-1]

            for j in range(pivot_col + 1, num_variables):
                total -= matrix[i][j] * solution[j]

            solution[pivot_col] = total / matrix[i][pivot_col]

        return solution
    
    def _swap_rows(self, row1, row2):
        self.matrix[row1], self.matrix[row2] = (self.matrix[row2],self.matrix[row1])

                

    def _find_pivot(self, pivot_row, pivot_col):
        max_row = pivot_row

        for r in range(pivot_row + 1, len(self.matrix)):
            if abs(self.matrix[r][pivot_col]) > abs(self.matrix[max_row][pivot_col]):
                max_row = r

        return max_row


    def _find_inconsistent_row(self):
        matrix = self.matrix
        num_variables = len(self.variables)

        for row in matrix:
            all_zero = True

            for col in range(num_variables):
                if abs(row[col]) >= 1e-9:
                    all_zero = False
                    break

            if all_zero and abs(row[-1]) >= 1e-9:
                return row

        return None


    def solve(self):
        num_equations=len(self.matrix)
        num_variables=len(self.variables)

        if num_equations < num_variables:
            raise DimensionMismatchException(num_equations,self.variables)


        self._forward_elimination()
        
        inconsistent_row = self._find_inconsistent_row()

        if inconsistent_row is not None:
            raise InconsistentSystemException(inconsistent_row[-1])


        rank = len(self.pivot_columns)

        if rank < num_variables:
            raise InfiniteSolutionsException(rank, num_variables)


        solution = self._back_substitution()
        return dict(zip(self.variables, solution))



    def get_metadata(self):
        return {"num_variables": len(self.variables),"num_equations": len(self.matrix)}