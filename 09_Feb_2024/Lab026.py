#Conditions
#Max from 3 numbers

num1=int(input("Enter number1"))
num2=int(input("Enter number2"))
num3=int(input("Enter number3"))

if num1 > num2 and num1 > num3:
    print("Num1 is max number")
elif num2 > num3 and num2 > num1:
    print("Num2 is max number")
else:
    print("Num3 is greater")