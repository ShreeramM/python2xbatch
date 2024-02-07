'''Write a Python program to calculate the area of a circle
given its radius using the formula area=π×r^2 ( Take pie as 3.14)'''

radius_input = float(input("Enter radius as input: "))
area_result = 3.14 * radius_input * radius_input
print("Area of circle is: ", area_result)

'''Create a program that takes two numbers as input and prints 
whether the first number is greater than, less than, or equal to the second number.'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter the second number: "))
result = num1 > num2
print("Result for num1 is greater than num2", result)
result_1 = num1 < num2
print("Result for num1 is less than num2",result_1)
result_2 = num1 == num2
print("Result for num1 is equal to num2",result_2)

'''Develop a Python script that calculates the square and cube of a given number.'''

num_input = int(input("Enter first number: "))
print("Square of number is", num_input * num_input)
print("Cube of number is", num_input * num_input * num_input)
