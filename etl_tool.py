import xml.etree.ElementTree as Tree

# Function to read an XML file and load the elements.
# Since the presence of the file is tested here, we don't test it elsewhere.
def parse_xml(file_path):
    try:
        tree = Tree.parse(file_path)
        return tree
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to save the XML file after data manipulation.
def save_xml(tree, save_path):
    if tree is not None:
        tree.write(save_path)

# Modified price of items in a category.
def modify_price(tree, category, increase):
    root = tree.getroot()
    for prod in root.findall(f"./product[@category='{category}']"):
        price = float(prod.find("price").text)
        new_price = price * (1 + increase/100)
        prod.find("price").text = str(new_price)

# Rename a category to another one.
def rename_category(tree, old_name, new_name):
    root = tree.getroot()
    for prod in root.findall(f"./product[@category='{old_name}']"):
        prod.set("category", new_name)

# Removes products below a certain rating.
def remove_products(tree, category, min_rating):
    root = tree.getroot()
    for prod in root.findall(f"./product[@category='{category}']"):
        if float(prod.find("rating").text) < min_rating:
            root.remove(prod)

# Outputs the report on the CLI
def generate_report(tree):
    report = {}
    root = tree.getroot()

    for prod in root.findall('product'):
        category = prod.attrib["category"]
        price = float(prod.find("price").text)
        report[category] = report.get(category, {"count": 0, "total_price": 0})
        report[category]["count"] += 1
        report[category]["total_price"] += price

    for k, v in report.items():
        print(f"\nCategory: {k}")
        print(f"Total Product Count: {v['count']}")
        print(f"Total Price: {v['total_price']}")
