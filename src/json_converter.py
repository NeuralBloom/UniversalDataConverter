import json
import pandas as pd
import xml.etree.ElementTree as ET
from typing import Optional, Dict, List, Union

class JSONConverter:
    """
    A class to handle conversions from JSON to other formats
    """
    
    def __init__(self):
        self.data = None
        
    def read_json(self, file_path: str) -> None:
        """Read JSON file into memory"""
        with open(file_path, 'r') as f:
            self.data = json.load(f)
    
    def to_csv(self, input_path: str, output_path: str) -> None:
        """Convert JSON to CSV"""
        # Read JSON and convert to DataFrame
        self.read_json(input_path)
        df = pd.json_normalize(self.data)
        # Save to CSV
        df.to_csv(output_path, index=False)
    
    def to_xml(self, input_path: str, output_path: str, root_name: str = 'data') -> None:
        """Convert JSON to XML"""
        self.read_json(input_path)
        
        # Create the root element
        root = ET.Element(root_name)
        
        # Helper function to convert JSON to XML
        def json_to_xml(data: Union[Dict, List], parent: ET.Element) -> None:
            if isinstance(data, dict):
                for key, value in data.items():
                    child = ET.SubElement(parent, str(key))
                    if isinstance(value, (dict, list)):
                        json_to_xml(value, child)
                    else:
                        child.text = str(value)
            elif isinstance(data, list):
                for item in data:
                    child = ET.SubElement(parent, 'item')
                    if isinstance(item, (dict, list)):
                        json_to_xml(item, child)
                    else:
                        child.text = str(item)
        
        # Convert the JSON data to XML
        json_to_xml(self.data, root)
        
        # Create XML tree and save to file
        tree = ET.ElementTree(root)
        tree.write(output_path, encoding='utf-8', xml_declaration=True)
    
    def to_excel(self, input_path: str, output_path: str) -> None:
        """Convert JSON to Excel"""
        # Read JSON and convert to DataFrame
        self.read_json(input_path)
        df = pd.json_normalize(self.data)
        # Save to Excel
        df.to_excel(output_path, index=False)
