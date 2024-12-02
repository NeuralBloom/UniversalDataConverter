# tests/test_xml_converter.py
import unittest
import os
from src.xml_converter import XMLConverter

class TestXMLConverter(unittest.TestCase):
    def setUp(self):
        self.converter = XMLConverter()
        self.input_file = "examples/sample.xml"
        self.output_json = "examples/output.json"
        self.output_csv = "examples/output.csv"
        self.output_excel = "examples/output.xlsx"

    def tearDown(self):
        # Clean up output files after tests
        for file in [self.output_json, self.output_csv, self.output_excel]:
            if os.path.exists(file):
                os.remove(file)

    def test_xml_to_json(self):
        self.converter.to_json(self.input_file, self.output_json)
        self.assertTrue(os.path.exists(self.output_json))

    def test_xml_to_csv(self):
        self.converter.to_csv(self.input_file, self.output_csv)
        self.assertTrue(os.path.exists(self.output_csv))

    def test_xml_to_excel(self):
        self.converter.to_excel(self.input_file, self.output_excel)
        self.assertTrue(os.path.exists(self.output_excel))
