# *args - any number of argumnets not to define
# multiple * parameters not allowed

def sum(*args):
    for i in args:
        print(i)


result = sum(1, 2, 3, 4)
print(result)
