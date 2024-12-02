Usage Guide
CSV Converter
pythonCopyfrom src.csv_converter import CSVConverter

# Initialize converter
converter = CSVConverter()

# Convert CSV to JSON
converter.to_json("input.csv", "output.json")

# Convert CSV to XML
converter.to_xml("input.csv", "output.xml", root_name="data")

# Convert CSV to Excel
converter.to_excel("input.csv", "output.xlsx")
JSON Converter
pythonCopyfrom src.json_converter import JSONConverter

# Initialize converter
converter = JSONConverter()

# Convert JSON to CSV
converter.to_csv("input.json", "output.csv")

# Convert JSON to XML
converter.to_xml("input.json", "output.xml", root_name="data")

# Convert JSON to Excel
converter.to_excel("input.json", "output.xlsx")
XML Converter
pythonCopyfrom src.xml_converter import XMLConverter

# Initialize converter
converter = XMLConverter()

# Convert XML to JSON
converter.to_json("input.xml", "output.json")

# Convert XML to CSV
converter.to_csv("input.xml", "output.csv")

# Convert XML to Excel
converter.to_excel("input.xml", "output.xlsx")
Excel Converter
pythonCopyfrom src.excel_converter import ExcelConverter

# Initialize converter
converter = ExcelConverter()

# Convert Excel to CSV
converter.to_csv("input.xlsx", "output.csv")

# Convert Excel to JSON
converter.to_json("input.xlsx", "output.json")

# Convert Excel to XML
converter.to_xml("input.xlsx", "output.xml", root_name="data")

# List all sheets in an Excel file
sheets = converter.list_sheets("input.xlsx")
