import re
from pyeqsolver.exceptions import InvalidFileFormatException

class EquationParser:

    def __init__(self,file_path):
        self.file_path=file_path

    def parse(self):
        equations=[]
        variables=[]
        with open(self.file_path,'r') as file:
            for line_number, line in enumerate(file, start=1):
                line=line.strip()
                if not line or line.startswith("#"):
                    continue

                self._validate_line(line,line_number)

                coefficients, constant = self._parse_line(line)

                equations.append((coefficients, constant))

                for variable in coefficients:
                    if variable not in variables:
                        variables.append(variable)

        if not equations:
            raise InvalidFileFormatException(message="The file contains no equations")


        A=[]

        for coefficients, constant in equations:
            row=[]

            for variable in variables:
                value= coefficients.get(variable,0.0)
                row.append(value)


            row.append(constant)
            A.append(row)


        return A ,variables
        


    def _parse_line(self,line):
        left , right =line.split("=")

        left=left.replace(" ",'')
        right=right.strip()

        pattern = r'([+-]?)(\d+(?:\.\d+)?)?\*?([a-zA-Z_]\w*)'

        terms=re.findall(pattern,left)


        coefficients={}

        for sign, coefficient, variable in terms:

            if coefficient =='':
                coefficient=1.0
            else:
                coefficient=float(coefficient)

            if sign =="-":
                coefficient*=-1

            coefficients[variable]=(coefficients.get(variable, 0) + coefficient)


        constant=float(right)

        return coefficients,constant
            

        

    def _validate_line(self, line, line_number):

    # Check that there is exactly one equal sign
        if line.count("=") != 1:
            raise InvalidFileFormatException(line_number, line)

        left, right = line.split("=")

    # Check that both sides are not empty
        if not left.strip() or not right.strip():
            raise InvalidFileFormatException(line_number, line)

    # Check for unsupported characters
        invalid_chars_pattern = r'[^a-zA-Z0-9_+\-.*= ]'
        if re.search(invalid_chars_pattern, line):
            raise InvalidFileFormatException(line_number, line)

    # Check that the left side contains valid variable terms
        left_pattern = (
        r'\s*[+-]?\s*'
        r'(?:(?:\d+(?:\.\d+)?|\.\d+)\s*\*?\s*)?'
        r'[a-zA-Z_]\w*'
        r'(?:\s*[+-]\s*'
        r'(?:(?:\d+(?:\.\d+)?|\.\d+)\s*\*?\s*)?'
        r'[a-zA-Z_]\w*)*\s*'
        )

        if not re.fullmatch(left_pattern, left):
            raise InvalidFileFormatException(line_number, line)

    # Check that the right side is a single valid number
        right_pattern = r'[+-]?\s*(?:\d+(?:\.\d+)?|\.\d+)'

        if not re.fullmatch(right_pattern, right.strip()):
            raise InvalidFileFormatException(line_number, line)














    