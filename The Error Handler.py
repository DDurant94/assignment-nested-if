'''
3. Silent Failures: The Error Handler 🐞
Objective:

To practice the use of the pass statement in handling potential errors silently.

Task 1: Code Correction

You are provided with a Python script that is supposed to handle errors silently, but it has some mistakes. Identify and fix them.

Buggy Code:

try:
    x = 1 / 0
except ZeroDivisionError
    pass
Task 2: Division Calculator

Based on the corrected code from Task 1, enhance the program to handle other potential errors, such as a ValueError or TypeError. Experiment with what happens when you divide an integer by a string and identify what kind of error it gives you. Then use the except statement to handle the error.

Task 3: File Reader

Ask the user for a filename to read. Try to open and read the file. If the file doesn't exist, use the pass statement to handle the error silently.
'''
# Task one.
'''
try:
  x = 1 / 0
except ZeroDivisionError:
  pass'''

# Task Two.

'''
try:
 x = 1 / 0
except ZeroDivisionError:
  pass


try:
 age = (input("Enter your age! "))
 print("You can drive!" if age >= 18 else "You can't drive!")   # if anything other than a number is put in we get a TypeError we can pass that with this
except TypeError:
  pass
  print("TypeError: We need a number to see if you can drive or not!") 


try:
 x = 10
 y = int("hello")
 z = x + y
except ValueError: #i am getting a ValueError from the variable y not being able to convert hello to a int
  pass
  print("ValueError: 'hello' can't be converted to a number.")


try:
 a = 1
 b = "hello"
 c = a / b    #this gave me a type error python can't divid a int by a str it is the same error i get from above.
except TypeError:
  pass
  print("TypeError:", a, "Can't be divided by 'hello'!")
'''
# Task three.

'''
try:
  file = input("Enter in the name of your file! ")
  with open(file, "r") as file_object:
    print(file_object.read())
  file_object.close()
except FileNotFoundError:
  print("File can not be opened")
  '''
# can open with a with or how i did below. I opened "The Event PLanner.py"
# i couldn't figure out how to open files from outside vs code. That gives me a OSError also couldn't figure out how to run two execptions together. 
try:
  file = input("Enter in the name of your file! ")
  file_object = open(file, "r")
  print(file_object.read())
  file_object.close()
except FileNotFoundError:
  pass
  
