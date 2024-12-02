import xml.etree.ElementTree as ET
import json
import pandas as pd
from typing import Dict, Optional

class XMLConverter:
    """
    A class to handle conversions from XML to other formats
    """
    
    def __init__(self):
        self.tree = None
        self.root = None
    
    def read_xml(self, file_path: str) -> None:
        """Read XML file into memory"""
        self.tree = ET.parse(file_path)
        self.root = self.tree.getroot()
    
    def xml_to_dict(self, element: ET.Element) -> Dict:
        """Convert XML element to dictionary"""
        result = {}
        
        # Process attributes
        if element.attrib:
            result.update(element.attrib)
        
        # Process children
        for child in element:
            child_data = self.xml_to_dict(child)
            
            if child.tag in result:
                # If the tag already exists, convert to list or append
                if isinstance(result[child.tag], list):
                    result[child.tag].append(child_data)
                else:
                    result[child.tag] = [result[child.tag], child_data]
            else:
                result[child.tag] = child_data
        
        # Process text content
        if element.text and element.text.strip():
            if result:
                result['text'] = element.text.strip()
            else:
                result = element.text.strip()
        
        return result
    
    def to_json(self, input_path: str, output_path: str) -> None:
        """Convert XML to JSON"""
        self.read_xml(input_path)
        data = self.xml_to_dict(self.root)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    
    def to_csv(self, input_path: str, output_path: str) -> None:
        """Convert XML to CSV"""
        self.read_xml(input_path)
        data = self.xml_to_dict(self.root)
        
        # Convert to DataFrame
        df = pd.json_normalize(data)
        df.to_csv(output_path, index=False)
    
    def to_excel(self, input_path: str, output_path: str) -> None:
        """Convert XML to Excel"""
        self.read_xml(input_path)
        data = self.xml_to_dict(self.root)
        
        # Convert to DataFrame
        df = pd.json_normalize(data)
        df.to_excel(output_path, index=False)
