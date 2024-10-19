from sympy import symbols, apart, Add

import os, time

# Define the variable
x = symbols('x')

numerator_degree = int(input("Enter the degree of the polynomial's numerator: "))
denominator_degree = int(input("Enter the degree of the polynomial's denominator: "))

time.sleep(0.5)
os.system('clear')

list_of_coefficients_numerator = []
list_of_coefficients_denominator = []

# add degrees to a list for numerator and denominator
for i in range(numerator_degree + 1):
    print(f"What is the numerator coefficient of x^{i}?")
    coefficient_input = int(input())
    list_of_coefficients_numerator.append(coefficient_input)

time.sleep(0.5)
os.system('clear')

for i in range(denominator_degree + 1):
    print(f"What is the denominator coefficient of x^{i}?")
    coefficient_input = int(input())
    list_of_coefficients_denominator.append(coefficient_input)

time.sleep(0.5)
os.system('clear')

# goes through that list and multiplies each coefficient by x^i for both numerator and denominator
temp_numerator_list = []
temp_denominator_list = []

for i in range(numerator_degree, -1, -1):
    numerator_term = list_of_coefficients_numerator[i] * x**i
    temp_numerator_list.append(numerator_term)

for i in range(denominator_degree, -1, -1):
    denominator_term = list_of_coefficients_denominator[i] * x**i 
    temp_denominator_list.append(denominator_term)

def join_with_plus(lst):
    return Add(*lst)

numerator = join_with_plus(temp_numerator_list)
denominator = join_with_plus(temp_denominator_list)

polynomial = numerator / denominator
print(apart(polynomial))