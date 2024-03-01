# Task - Factorial
# # Factorial
# # n = 5
# # 5! -->5*4*3*2*1 -> 120
# # 3! -> 3*2*1 -> 6
# # 4! -> 4*3*2*1 -> 24
import math

number = int(input("Enter a number as input: "))
# print(math.factorial(number))
fact = 1
for i in range(1, number + 1):
    fact = fact * i
print("Factorial is: :", fact)


#Fibonacci Series
i = 0
j = 1
result = 1
number = int(input("Enter a number as input: "))
for k in range (1, number):
    result += number + j
print("Fibonacci series is: ",i, j, number)
