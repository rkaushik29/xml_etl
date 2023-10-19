import xml.etree.ElementTree as Tree

# Function to read an XML file and load the elements
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
