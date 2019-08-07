#Python program to get a string which is n (non-negative integer) copies of a given string
def copy_string(str,n):
    result=""
    for i in range(n):
        result+=str

    return result
print(copy_string("abc",3))
print(copy_string(".py",2))
print(copy_string(".test",4))
