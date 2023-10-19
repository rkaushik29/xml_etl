# ETLTool
CLI app to extract and manipulate XML data.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Dependencies](#dependencies)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Testing](#testing)
7. [Contributions](#contributions)
8. [License](#license)

---

## Introduction

The `ETLTool` is a command-line interface (CLI) tool that allows users to manage product information, including price modifications, category renaming, and product removal based on minimum ratings.

## Features

1. **Load XML File**: Load an XML file containing product data.
2. **Increase Price By Percent**: Increase the price of products within a specified category.
3. **Rename Category**: Rename a category of products.
4. **Remove Products Below Minimum Rating**: Remove products below a specified rating within a category.
5. **Save Changes to New File**: Save the changes made to product data in a new XML file.
6. **Generate Report on CLI**: Generate and display a summary report of product data on the CLI.

## Requirements
- A Computer
- Python 3.8+

## Usage

Run the tool by executing the following command:

```bash
chmod +x etl_tool.py
python3 etl_tool.py
```

Follow the prompts to manage your product data. 

Note: The given test data is in `test.xml` -> use this as the path of the file to load.

## Testing

Automated tests are written using Python's `unittest` framework. 

To run the tests, execute the bash script:

1. Give executable permissions to the script:
    ```bash
    chmod +x test.sh
    ```
2. Run the script:
    ```bash
    ./test.sh
    ```

This will automatically run all the test cases defined in `etl_tool_test.py`.

## Contributions

To contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
