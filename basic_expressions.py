"""
Purpose: Illustrate basic expressions and operators in Python.

Author: Denise Case

This file name is:   basic_expressions.py
This module name is: basic_expressions

Expressions

Data analytics is all about getting value out of data.
Expressions are the building blocks of data analytics.

Rather like math expressions, or Excel expressions, Python expressions
are a combination of values, variables, operators, and function calls.

Expressions are made of operands and operators.

- Operators are symbols like +, -, *, /, and =.
- Operands can be values or variables, 
  and can include function calls like len() and str().

Writing expressions in Python is like writing formulas in Excel.
 
"""

# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Declare  Variables
# TODO: Try changing the values of these variables
# TODO: Add some new variables (like rectangle_length and rectangle_width)
#       and calculate the area of a rectangle (rectangle_area = rectangle_length * rectangle_width)
triangle_base = 15
triangle_height = 5
num1 = 59
num2 = 13
float_num1 = 1.9
float_num2 = 2.9
float_num3 = 9.9

rectangle_length = 4
rectangle_width = 9



# Basic Arithmetic Operations
triangle_area = triangle_base * triangle_height / 2
total_sum = float_num1 + float_num2
difference = num1 - num2

rectangle_area = rectangle_length * rectangle_width

# Log Information
logger.info(
    f"Given base={triangle_base} and height={triangle_height}, triangle area = {triangle_area}"
)
logger.info(
    f"Given float_num1={float_num1} and float_num2={float_num2}, sum = {total_sum}"
)
logger.info(f"Given num1={num1} and num2={num2}, the difference = {difference}")
logger.info(
    f"Given width={rectangle_width} and length={rectangle_length}, rectangle area = {rectangle_area}"
)

import statistics
data_a = [10, 11, 14, 20, 20, 20, 22, 24, 28, 31]
data_b = [2, 9, 13, 14, 20, 20, 24, 26, 32, 40] 
mean_data_a = statistics.mean(data_a)
mean_data_b = statistics.mean(data_b)
median_data_a = statistics.median(data_a)
median_data_b = statistics.median(data_b)
mode_data_a = statistics.mode(data_a)
mode_data_b = statistics.mode(data_b)
logger.info(
    f"Mean, median, and mode for data a is ={mean_data_a} {median_data_a}, {mode_data_a}"
)
logger.info(
    f"Mean, median, and mode for data b is ={mean_data_b} {median_data_b}, {mode_data_b}"
)