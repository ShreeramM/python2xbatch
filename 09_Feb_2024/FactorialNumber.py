# Task - Factorial
# # Factorial
# # n = 5
# # 5! -->5*4*3*2*1 -> 120
# # 3! -> 3*2*1 -> 6
# # 4! -> 4*3*2*1 -> 24
import math

number = int(input("Enter a number as input: "))
# print(math.factorial(number))

for i in range(1, number):
    number = number * i
    print("Factorial is: :", number)