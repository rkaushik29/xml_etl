import unittest
import os
import xml.etree.ElementTree as Tree
from etl_tool import parse_xml, modify_price, rename_category, remove_products, generate_report

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
        self.tree = Tree.ElementTree(Tree.fromstring(self.sample_data))
    
    # Testing the parsing and loading of the XML doc
    def test_parse_xml(self):
        new_tree = parse_xml("test.xml")
        root = new_tree.getroot()
        self.assertEqual(root.tag, "products")      # assertion changes with change in test data

    def test_save_changes(self):
        # Save to a temporary file and then read to verify
        out_file = "temp.xml"
        self.tree.write(out_file)
        tree = Tree.parse(out_file)
        root = tree.getroot()
        self.assertEqual(root.tag, 'products')
        os.remove(out_file)  # Cleanup temp file

    # Testing modification of price by imitating actual call
    def test_modify_price(self):
        category, increase_pct = "Electronics", 10
        modify_price(self.tree, category, increase_pct)
        for product in self.tree.getroot().findall("./product[@category='Electronics']"):
            self.assertEqual(float(product.find('price').text), 659.989)
    
    # Testing rename of category
    def test_rename(self):
        old_name, new_name = "Books", "Python Books"
        rename_category(self.tree, old_name, new_name)
        for product in self.tree.getroot().findall("./product[@category='Python Books']"):
            self.assertIsNotNone(product)
    
    # Testing removal of products below a min rating
    def test_remove_products(self):
        category, min_rating = "Books", 4.2
        remove_products(self.tree, category, min_rating)
        for product in self.tree.getroot().findall("./product[@category='Books']"):
            self.assertIsNone(product)
    
    def test_generate_report(self):

        report = generate_report(self.tree)
        self.assertEqual(report, {'Electronics': {'count': 1, 'total_price': 599.99},
                                  'Books': {'count': 1, 'total_price': 29.99}})

if __name__ == "__main__":
    unittest.main()
