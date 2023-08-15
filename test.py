import unittest
import json
from io import StringIO
from unittest.mock import patch
import pandas as pd
from main import printData  # Replace 'your_module_name' with your actual module name

class TestPrintData(unittest.TestCase):
    def setUp(self):
        self.expected_output = pd.DataFrame({'numbers': [1, 2, 3], 'colors': ['red', 'white', 'blue']}).to_json()

    @patch('sys.stdout', new_callable=StringIO)
    def capture_stdout(self, mock_stdout):
        printData()
        return mock_stdout.getvalue()

    def test_printData_output(self):
        output = self.capture_stdout()
        self.assertEqual(output.strip(), self.expected_output)

    def test_printData_json_format(self):
        output = self.capture_stdout()
        try:
            json.loads(output)
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON format")

if __name__ == '__main__':
    unittest.main()