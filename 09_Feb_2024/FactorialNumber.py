# Task - Factorial
# # Factorial
# # n = 5
# # 5! -->5*4*3*2*1 -> 120
# # 3! -> 3*2*1 -> 6
# # 4! -> 4*3*2*1 -> 24

number = int(input("Enter a number as input: "))
result = None
for result in range(1, number):
    result = result * number
    print(result)