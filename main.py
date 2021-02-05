# This is a program that solves the quadratic equation.
import math

print("Please Enter The Following Values: ")

while True:
    try:
        # Prompts user for input.
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
    except ValueError:
        print("Please Enter Numerical Values!")
        continue
    else:
        break
try:
    # Calculates the quadratic equation.
    part_1 = b * b
    part_2 = 4 * a * c
    part_3 = part_1 - part_2
    part_4 = math.sqrt(part_3)
    part_5 = -1 * b
    part_6 = part_5 + part_4
    part_7 = part_5 - part_4
    part_8 = 2 * a
    part_9 = part_6 / part_8
    part_10 = part_7 / part_8

    # Prints out the answer.
    print(f"x={part_9} or x={part_10}")
except:
    print("Quadratic Solution Doesn't Exist.")
