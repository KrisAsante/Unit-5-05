# Created by: Chris Asante
# Created on: 11-April-2019
# Created for: ICS3U
# Unit 5-05
# This program finds the average of a 2D array with random numbers
import random

def two_dimension_loop_average(array):
    total = 0
    for row in array:
        for column in row:
            total = total + column
    average = total / (len(array[0]) * len(array))
    return average

rows_number = int(input("Enter the number of rows: "))
if rows_number < 0:
    rows_number = int(input("Please enter a positive value for the number of rows: "))
else:
    pass

columns_number = int(input("Enter the number of columns: "))
if columns_number < 0:
    columns_number = int(input("Please enter a positive value for the number of columns: "))
else:
    pass

table = []

for rows in range(0, rows_number):
    table.append([])
    for columns in range(0, columns_number):
        table[rows].append(random.randint(0, 50+1))
average_of_elements_table = two_dimension_loop_average(table)

print(table)
print("The average of numbers in the table is : " + str(average_of_elements_table) + ".\n")