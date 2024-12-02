import pandas as pd
import json
import xml.etree.ElementTree as ET
from typing import Optional

class ExcelConverter:
    """
    A class to handle conversions from Excel to other formats
    """
    
    def __init__(self):
        self.data = None
    
    def read_excel(self, file_path: str, sheet_name: Optional[str] = None) -> None:
        """Read Excel file into pandas DataFrame"""
        self.data = pd.read_excel(file_path, sheet_name=sheet_name)
    
    def to_csv(self, input_path: str, output_path: str, sheet_name: Optional[str] = None) -> None:
        """Convert Excel to CSV"""
        self.read_excel(input_path, sheet_name)
        self.data.to_csv(output_path, index=False)
    
    def to_json(self, input_path: str, output_path: str, sheet_name: Optional[str] = None) -> None:
        """Convert Excel to JSON"""
        self.read_excel(input_path, sheet_name)
        self.data.to_json(output_path, orient='records', indent=4)
    
    def to_xml(self, input_path: str, output_path: str, sheet_name: Optional[str] = None, root_name: str = 'data') -> None:
        """Convert Excel to XML"""
        self.read_excel(input_path, sheet_name)
        xml_data = self.data.to_xml(root_name=root_name)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_data)
    
    def list_sheets(self, file_path: str) -> list:
        """List all sheets in the Excel file"""
        xl = pd.ExcelFile(file_path)
        return xl.sheet_names
