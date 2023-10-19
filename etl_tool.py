import xml.etree.ElementTree as Tree
import unittest
import os

# Clear Screen
def clear_screen():
    if os.name == 'posix':  # Linux
        os.system('clear')
    elif os.name in ('nt', 'dos', 'ce'):    # Windows
        os.system('CLS')

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
    def save_xml(self, save_path):
        if self.tree is not None:
            self.tree.write(save_path)

    # Modified price of items in a category.
    def modify_price(self, category, increase):
        root = self.tree.getroot()
        for prod in root.findall(f"./product[@category='{category}']"):
            price = float(prod.find("price").text)
            new_price = price * (1 + increase/100)
            prod.find("price").text = str(new_price)

    # Rename a category to another one.
    def rename_category(self, old_name, new_name):
        root = self.tree.getroot()
        for prod in root.findall(f"./product[@category='{old_name}']"):
            prod.set("category", new_name)

    # Removes products below a certain rating.
    def remove_products(self, category, min_rating):
        root = self.tree.getroot()
        for prod in root.findall(f"./product[@category='{category}']"):
            if float(prod.find("rating").text) < min_rating:
                root.remove(prod)

    # Outputs the report on the CLI
    def generate_report(self):
        report = {}
        root = self.tree.getroot()

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
            clear_screen()
            print("\nWelcome to the Product ETL Tool")
            print("1: Load XML File")
            print("2: Increase Price By Percent")
            print("3: Rename Category")
            print("4: Remove Products Below Minimum Rating")
            print("5: Save Changes to New File")
            print("6: Generate Report on CLI")
            print("7: Exit")

            select = input("Enter your choice here (Number): ")
            LOAD_ERR = "Please load an XML file first by selecting option 1."

            # Menu based CLI
            if select == "1":
                file_path = input("Enter the relative path to the XML file: ")
                self.parse_xml(file_path)
            
            elif select == "2":
                # Check if tree is filled with a loaded XML. If not, we first need to load it (1)
                if self.tree is None:
                    print(LOAD_ERR)
                    break
                category = input("Enter the category name: ")
                percentage = float(input("Enter the percentage increase (number only): "))
                self.modify_price(category, percentage)
            
            elif select == "3":
                if self.tree is None:
                    print(LOAD_ERR)
                    break
                old_name = input("Enter the current category name: ")
                new_name = input("Enter the new category name: ")
                self.rename_category(old_name, new_name)
            
            elif select == "4":
                if self.tree is None:
                    print(LOAD_ERR)
                    break
                category = input("Enter the category name: ")
                min_rating = float(input("Enter the minimum rating: "))
                self.remove_products(category, min_rating)
            
            elif select == "5":
                if self.tree is None:
                    print(LOAD_ERR)
                    break
                save_path = input("Enter the path to save the XML file: ")
                self.save_xml(save_path)
            
            elif select == "6":
                if self.tree is None:
                    print(LOAD_ERR)
                    break
                self.generate_report()

            elif select == "7":
                print("\nGoodbye!")
                break
            
            input("\nClick any key to proceed")     # Breakpoint before next menu appears


if __name__ == "__main__":
    # Init new tool
    etl_tool = ETLTool()
    
    # Run the tool
    etl_tool.run_tool()