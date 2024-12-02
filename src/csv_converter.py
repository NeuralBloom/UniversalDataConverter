import pandas as pd
import json
import xml
from typing import Optional

class CSVConverter:
    """
    A class to handle conversions from CSV to other formats
    """
    
    def __init__(self):
        self.data = None
        
    def read_csv(self, file_path: str) -> None:
        """Read CSV file into pandas DataFrame"""
        self.data = pd.read_csv(file_path)
        
    def to_json(self, input_path: str, output_path: str) -> None:
        """Convert CSV to JSON"""
        self.read_csv(input_path)
        self.data.to_json(output_path, orient='records', indent=4)
        
    def to_xml(self, input_path: str, output_path: str, root_name: str = 'data') -> None:
        """Convert CSV to XML"""
        self.read_csv(input_path)
        xml_data = self.data.to_xml(root_name=root_name)
        with open(output_path, 'w') as f:
            f.write(xml_data)
            
    def to_excel(self, input_path: str, output_path: str) -> None:
        """Convert CSV to Excel"""
        self.read_csv(input_path)
        self.data.to_excel(output_path, index=False)
