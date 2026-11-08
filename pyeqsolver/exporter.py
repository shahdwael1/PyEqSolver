import json
from pathlib import Path

class JSONExporter:

    def __init__(self, output_path):
        self.output_path = Path(output_path)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

    def _format_solution(self, solutions):
        formatted_solution = {}

        for variable, value in solutions.items():
            value = round(value, 4)

            if value == 0:
                value = 0.0

            formatted_solution[variable] = value

        return formatted_solution


    def save(self, solutions, metadata):

        formatted_solution = self._format_solution(solutions)

        data = {
        "status": "SUCCESS",
        "system_info": metadata,
        "solution": formatted_solution
        }

        with open(self.output_path, 'w') as file:
            json.dump(data, file, indent=2)



    def save_error(self, exc):

        data = {
        "status": "ERROR",
        "error_type": type(exc).__name__,
        "message": str(exc)
        }

        with open(self.output_path, 'w') as file:
            json.dump(data, file, indent=2)