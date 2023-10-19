import xml.etree.ElementTree as Tree
import unittest
from etl_tool_test import ETLToolTest


class ETLTool:
    # Constructor
    def __init__(self):
        self.tree = None

    # Function to read an XML file and load the elements.
    # Since the presence of the file is tested here, we don"t test it elsewhere.
    def parse_xml(self, file_path):
        try:
            self.tree = Tree.parse(file_path)
        except Exception as e:
            print(f"Error: {e}")

    # Function to save the XML file after data manipulation.
    def save_xml(self, tree, save_path):
        if tree is not None:
            tree.write(save_path)

    # Modified price of items in a category.
    def modify_price(self, tree, category, increase):
        root = tree.getroot()
        for prod in root.findall(f"./product[@category='{category}']"):
            price = float(prod.find("price").text)
            new_price = price * (1 + increase/100)
            prod.find("price").text = str(new_price)

    # Rename a category to another one.
    def rename_category(self, tree, old_name, new_name):
        root = tree.getroot()
        for prod in root.findall(f"./product[@category='{old_name}']"):
            prod.set("category", new_name)

    # Removes products below a certain rating.
    def remove_products(self, tree, category, min_rating):
        root = tree.getroot()
        for prod in root.findall(f"./product[@category='{category}']"):
            if float(prod.find("rating").text) < min_rating:
                root.remove(prod)

    # Outputs the report on the CLI
    def generate_report(self, tree):
        report = {}
        root = tree.getroot()

        for prod in root.findall("product"):
            category = prod.attrib["category"]
            price = float(prod.find("price").text)
            report[category] = report.get(category, {"count": 0, "total_price": 0})
            report[category]["count"] += 1
            report[category]["total_price"] += price

        for k, v in report.items():
            print(f"\nCategory: {k}")
            print(f"Total Product Count: {v['count']}")
            print(f"Total Price: {v['total_price']}")

    # Runs the UI for the tool as a menu based interface.
    def run_tool(self):
        while True:
            print("\nWelcome to the Product ETL Tool")
            print("1: Load XML File")
            print("2: Increase Price By Percent")
            print("3: Rename Category")
            print("4: Remove Products Below Minimum Rating")
            print("5: Save Changes to New File")
            print("6: Generate Report on CLI")
            print("7: Run Unit Test Suite")
            print("8: Exit")

            select = input("Enter your choice here (Number): ")
            LOAD_ERR = "Please load an XML file first by selecting option 1."

            # Menu based CLI
            if select == "1":
                file_path = input("Enter the relative path to the XML file: ")
                self.parse_xml(file_path)
            
            elif select == "2":
                # Check if tree is filled with a loaded XML. If not, we first need to load it (1)
                if self.tree is not None:
                    print(LOAD_ERR)
                    continue
                category = input("Enter the category name: ")
                percentage = float(input("Enter the percentage increase (number only): "))
                self.modify_price(self.tree, category, percentage)
            
            elif select == "3":
                if self.tree is not None:
                    print(LOAD_ERR)
                    continue
                old_name = input("Enter the current category name: ")
                new_name = input("Enter the new category name: ")
                self.rename_category(self.tree, old_name, new_name)
            
            elif select == "4":
                if self.tree is not None:
                    print(LOAD_ERR)
                    continue
                category = input("Enter the category name: ")
                min_rating = float(input("Enter the minimum rating: "))
                self.remove_products(self.tree, category, min_rating)
            
            elif select == "5":
                if self.tree is not None:
                    print(LOAD_ERR)
                    continue
                save_path = input("Enter the path to save the XML file: ")
                self.save_xml(self.tree, save_path)
            
            elif select == "6":
                if self.tree is not None:
                    print(LOAD_ERR)
                    continue
                self.generate_report(self.tree)

            elif select == "7":
                test = unittest.TestLoader().loadTestsFromTestCase(ETLToolTest)
                if test:
                    print("\nRunning Unit Test Suite...")
                    unittest.TextTestRunner().run(test=test)
                else:
                    print("Test Case unavailable")

            elif select == "8":
                break


if __name__ == "__main__":
    etl_tool = ETLTool()