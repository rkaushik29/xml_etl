import unittest
from unittest.mock import patch
import os
import io
import xml.etree.ElementTree as Tree
from etl_tool import ETLTool

# Testing suite that inherits from unittest.TestCase, with setUp inherited method running before each testcase 
class ETLToolTest(unittest.TestCase):

    # Set up the test case with any sample data
    def setUp(self):
        self.sample_data = (
        '''
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
        )
        # Generate a element tree from test data
        self.tool = ETLTool()
        self.tool.tree = Tree.ElementTree(Tree.fromstring(self.sample_data))        # test the data injested by this with parsed data
    
    # Testing the parsing and loading of the XML doc
    def test_parse_xml(self):
        self.tool.parse_xml("test.xml")
        root = self.tool.tree.getroot()
        self.assertEqual(root.tag, "products")      # assertion changes with change in test data

    # Testing modification of price by imitating actual call
    def test_modify_price(self):
        category, increase_pct = "Electronics", 10
        self.tool.modify_price(category, increase_pct)
        for product in self.tool.tree.getroot().findall("./product[@category='Electronics']"):
            self.assertEqual(float(product.find('price').text), 659.989)
    
    # Testing rename of category
    def test_rename(self):
        old_name, new_name = "Books", "Python Books"
        self.tool.rename_category(old_name, new_name)
        for product in self.tool.tree.getroot().findall("./product[@category='Python Books']"):
            self.assertIsNotNone(product)
    
    # Testing removal of products below a min rating
    def test_remove_products(self):
        category, min_rating = "Books", 4.2
        self.tool.remove_products(category, min_rating)
        for product in self.tool.tree.getroot().findall("./product[@category='Books']"):
            self.assertIsNone(product)
    
    def test_save_changes(self):
        # Save to a temporary file and then read to verify
        out_file = "temp.xml"
        self.tool.tree.write(out_file)
        tree = Tree.parse(out_file)
        root = tree.getroot()
        self.assertEqual(root.tag, 'products')
        os.remove(out_file)  # Cleanup temp file

if __name__ == "__main__":
    unittest.main()
