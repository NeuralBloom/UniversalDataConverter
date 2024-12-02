# tests/test_json_converter.py
import unittest
import os
from src.json_converter import JSONConverter

class TestJSONConverter(unittest.TestCase):
    def setUp(self):
        self.converter = JSONConverter()
        self.input_file = "examples/sample.json"
        self.output_csv = "examples/output.csv"
        self.output_xml = "examples/output.xml"
        self.output_excel = "examples/output.xlsx"

    def tearDown(self):
        # Clean up output files after tests
        for file in [self.output_csv, self.output_xml, self.output_excel]:
            if os.path.exists(file):
                os.remove(file)

    def test_json_to_csv(self):
        self.converter.to_csv(self.input_file, self.output_csv)
        self.assertTrue(os.path.exists(self.output_csv))

    def test_json_to_xml(self):
        self.converter.to_xml(self.input_file, self.output_xml)
        self.assertTrue(os.path.exists(self.output_xml))

    def test_json_to_excel(self):
        self.converter.to_excel(self.input_file, self.output_excel)
        self.assertTrue(os.path.exists(self.output_excel))
