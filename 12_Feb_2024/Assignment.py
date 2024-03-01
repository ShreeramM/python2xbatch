name = input("Enter a name")
length = len(name)
reverse = ""
for i in range(length, 1):
    reverse += name[i]
    print(reverse)