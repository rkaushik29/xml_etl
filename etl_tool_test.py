import unittest
import xml.etree.ElementTree as Tree
from etl_tool import parse_xml, modify_price, rename_category, remove_products, generate_report

# Testing suite that inherits from unittest.TestCase, with setUp inherited method running before each testcase 
class ETLToolTest(unittest.TestCase):
    # Set up the test case with any sample data
    def setUp(self):
        self.sample_data = '''
                            <products>
                                <product category="Electronics">
                                <name>Iphone 12 Pro</name>
                                <price>599.99</price>
                                <rating>4.5</rating>
                                </product>
                                <product category="Books">
                                <name>Python for Beginners</name>
                                <price>29.99</price>
                                <rating>4.0</rating>
                                </product>
                            </products>
                            '''
        self.tree = Tree.ElementTree(Tree.fromstring(self.sample_data))
    
    