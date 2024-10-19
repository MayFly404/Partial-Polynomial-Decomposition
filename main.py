"""
Credits go to Wissam Nusair who coded this project,
Dr. Sauer who made me want to make this, and last but not least,
Claude 3.5 Sonnet who made the amazing comments so you can read the code.
"""

# Import necessary libraries
from sympy import symbols, apart, Add  # For symbolic mathematics operations
from typing import List, Union  # For type hinting

import os, time  # For system operations and time delays

# Define the symbolic variable for our polynomial
x: symbols = symbols('x')

# Get the degrees of the numerator and denominator polynomials from user input
numerator_degree: int = int(input("Enter the degree of the polynomial's numerator: "))
denominator_degree: int = int(input("Enter the degree of the polynomial's denominator: "))

# Brief pause and clear the console for better user experience
time.sleep(0.5)
os.system('clear')

# Initialize lists to store coefficients for numerator and denominator
list_of_coefficients_numerator: List[int] = []
list_of_coefficients_denominator: List[int] = []

# Collect coefficients for the numerator polynomial
for i in range(numerator_degree + 1):
    print(f"What is the numerator coefficient of x^{i}?")
    coefficient_input: int = int(input())
    list_of_coefficients_numerator.append(coefficient_input)

# Another brief pause and console clear
time.sleep(0.5)
os.system('clear')

# Collect coefficients for the denominator polynomial
for i in range(denominator_degree + 1):
    print(f"What is the denominator coefficient of x^{i}?")
    coefficient_input: int = int(input())
    list_of_coefficients_denominator.append(coefficient_input)

# Final pause and console clear before showing results
time.sleep(0.5)
os.system('clear')

# Initialize lists to store the terms of numerator and denominator polynomials
temp_numerator_list: List[Union[int, symbols]] = []
temp_denominator_list: List[Union[int, symbols]] = []

# Construct the numerator polynomial terms
for i in range(numerator_degree, -1, -1):
    numerator_term: Union[int, symbols] = list_of_coefficients_numerator[i] * x**i
    temp_numerator_list.append(numerator_term)

# Construct the denominator polynomial terms
for i in range(denominator_degree, -1, -1):
    denominator_term: Union[int, symbols] = list_of_coefficients_denominator[i] * x**i 
    temp_denominator_list.append(denominator_term)

# Helper function to combine terms with addition
def join_with_plus(lst: List[Union[int, symbols]]) -> Add:
    return Add(*lst)

# Combine terms to form complete numerator and denominator polynomials
numerator: Add = join_with_plus(temp_numerator_list)
denominator: Add = join_with_plus(temp_denominator_list)

# Create the final rational polynomial (fraction of polynomials)
polynomial: Union[int, symbols] = numerator / denominator

# Perform partial fraction decomposition and print the result
print(apart(polynomial))