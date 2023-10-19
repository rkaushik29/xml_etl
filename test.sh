#!/bin/bash

clear

echo "Running the ETLTool TestSuite"
python -m unittest etl_tool_test.py

echo "Finished running tests."
