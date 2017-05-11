home = "America"
if home == "America":
    print("Hello, America!")
else:
    print("Hello, World")


home="Mars"
if home =="America":
    print ("Hello, America")
elif home=="Canada":
    print ("Hello, Canada")
elif home=="Thailand":
    print ("Hello, Thailand")
else:
    print ("Hello, World")
	      
x=5
if x<10:
    print ("x is less than ten.")
elif x>10:
    print ("x is more than ten.")


def even_odd(x):
    if x%2==0:
        print("even")
    else:
        print("odd")


def f(x=2): # parameter in function f is optional.it will use 2 is no input is given
    return x**x

def add_it(x, y=10):# 1st parameter in function add_it is required, 2nd is optional. Required parameters must always be defined first
    return x+y

a= input("type a number:")
b= input("type another:")
a=int(a)
b=int(b)
try:
    print(a/b)
except ZeroDivisionError: # Catches a divide by zero exception
    print("b cannot be zero.")

try:
    a= input("type a number:")
    b= input("type another:")#catches invalid input and the divide by zero
    a= int(a)
    b= int(b)
    print(a/b)
except (ZeroDivisionError, ValueError): #catches invalid input and the divide by zero - Note: code only works correctly in Python 3
    print("invalid input.")



