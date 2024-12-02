# tests/test_csv_converter.py
import unittest
import os
from src.csv_converter import CSVConverter

class TestCSVConverter(unittest.TestCase):
    def setUp(self):
        self.converter = CSVConverter()
        self.input_file = "examples/sample.csv"
        self.output_json = "examples/output.json"
        self.output_xml = "examples/output.xml"
        self.output_excel = "examples/output.xlsx"

    def tearDown(self):
        # Clean up output files after tests
        for file in [self.output_json, self.output_xml, self.output_excel]:
            if os.path.exists(file):
                os.remove(file)

    def test_csv_to_json(self):
        self.converter.to_json(self.input_file, self.output_json)
        self.assertTrue(os.path.exists(self.output_json))

    def test_csv_to_xml(self):
        self.converter.to_xml(self.input_file, self.output_xml)
        self.assertTrue(os.path.exists(self.output_xml))

    def test_csv_to_excel(self):
        self.converter.to_excel(self.input_file, self.output_excel)
        self.assertTrue(os.path.exists(self.output_excel))
