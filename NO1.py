''' VARIABLE '''




'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z) '''

# taking multiple inputs at a time separated by comma
# x = [int(x) for x in input().split(",")]
# print(x)

'''
Local Variable
def f():
    a = "I am local"
    print(a)

f()
print(a)  # This would raise an error since 'local_var' is not accessible outside the function


Global Variable
a = "I am global"

def f():
    global a
    a = "Modified globally"
    print(a)

f()
print(a)

'''
