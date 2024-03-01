text = input("Enter a String: ")
reverse = ""
for i in text:
    reverse = i + reverse
print(reverse)
if reverse == text:
    print("Palindrome")
else:
    print("Not a Palindrome")