print("hello")
# lets do some python 
# this is a one line comment 

import math #use code from another python module, put import statements at the top always 
from datetime import datetime #importing a module from a package 
import random 
""" 
this is a multi 
line
comment 

"""

# VARIABLES 
x = 5 # no type information 
print(x) 
# use the built in type() function to determine the type of a variable or value 
print(x, type(x))
# we can reassign variables for different types 
x = "hello"
print(x, type(x))

# OPERATORS 
#pretty much the same as C++ with some exceptions 
# / floating point division // integer division % mod 
print (5 / 2, 5 // 2, 5 %2)
#exponentiation **
print(5**2)
# another way: using math library 
print(math.pow(5,2)) #RETURNS A FLOAT 
#CAN DO:: 
print("a" * 5)
my_var = False 
print(my_var + 1) #to learn more: look at object oriented programmingn

# && || ! : boolean operators in C++ 
#in python: use: and or not 

#DECIMAL FORMATTING 
#choose the one you prefer 
print("%.2f" %(math.pi))
print("{:.2f}".format(math.pi))
print(f"{math.pi:.2f}")

print(round(math.pi, 2))

#USER INPUT 
print("enter your favorite number: ", end="") # makes cursor on the same line 
fav_num = input() # input is ALWAYS a string 
#type conversion:
fav_num = int(fav_num)
print("fav number doubled::", 2 * fav_num)


#CONDITIONALS  (AKA if statements) 
#we have if elif(else if) else
temp = 72
if temp < 32:
    #python uses indetation to group statements together (like {} in c++)
    print("it is cold out")
elif temp < 60:
    print("it is not too bad out")
else:
    print("It is not cold out")


#you can nest if statements inside if statements 
#WATCH INDENTATION 


#LOOPS 
# we have for loops and while loops 
#for item in sequence: 
#   body of statements to be repeated 
for char in "hello":
        print(char) #prints hello 

for item in [1,2,3,4]:
     print(item)

#we can make our own sequences with range()
#range(stop) [0, stop)
#range (start, stop) [start, stop) !! pay attention to [ vs (
#range(start, stop, step) specifies a step 
#EXAMPLE: 

for i in range(5): #goes up to 4 from 0
    print(i)

for i in range(-2, 5, 3):
    print(i)

#TASK: print the first 20 even numbers all on one line separated by a comma and a space 
#2, 4, ..., 40 
for i in range(2, 40, 2):
     print(i, end=", ")
print(i + 2)

# while loop structure 
#similar to C++, 
#while boolean is true:
#   body (code we want repeated)
#   progress towards boolean condition being false 
# task: rewrite the even number loop using a while loop  
x= 2
while x <= 38:
     print(x, end= ", ")
     x += 2
print(x)

while True:
     user_input = input("enter a word (\"stop\" to exit): ")
     if user_input == "stop":
            break 
print ("outside the loop")

#FUNCTIONS 
#functionm is  a named sequence of statements 
#functions can accept inputs (arguments when you call parameters when you define the function)
#they can return 0 or more values 
#def function_name(parameter list):
#   body(only executes once you call the function)
def my_print(msg_str): #header 
    print(f"{datetime.now()}: {msg_str}")
    """docstring 
    prepends a timestamp to the msg_str before printing 
    """


my_print("testing123")
#TASK: define/call a function that accepts a radius 
#and returns the area and the circumference of a circle with that radius 
def compute_circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius 
    print("area:", area, "circumference:", circumference)

compute_circle_stats(5)


#with return 
def compute_circle_stats2(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius 
    return (area, circumference) #send back values to the calling code! 
    #THIS IS A TUPLE^

#tuples are immutable (cannot be changed)
#lists are mutable (can be changed )

#unpacks return values 
area_result, circum_result = compute_circle_stats2(5)
print("area result:", area_result, "circumference result:", circum_result)
#does not unpack return values 
result = compute_circle_stats2(5)
print("type(result):", type(result))
print("result:", result, result[0], result[1])

#RANDOM NUMBERS 
#often we need random numbers for simulating random events 
#or initializing the state of an algorithm 
#need to import random 

#if you want the same random numbers each time you run your program, "seed" the random number generator 
random.seed(0)
#seed to get the same results every time? 

#let us roll a 6 sided die 
#import the random module 
roll = random.randrange(1,7) #[1,7)
print("roll:", roll)
roll = random.randint(1,6) # [1,6]
print("roll:", roll )






