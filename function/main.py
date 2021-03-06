# function beginer
#using argv
def fun(*argv):
  for arg in argv:
    print (arg)

fun("hai", "How are you")

# using kwarg
def fun2(**kwarg):
  for keycode, value in kwarg.items():
    print("%s == %s" %(keycode, value))

fun2(first = '123',second = '213', third = '321')

# lambda untuk anonymous function

triangle = lambda z: z*z
print(triangle(2))

#class method

from datetime import date

class person:
  def __init__(self, name , age):
    self.name = name
    self.age = age

  @classmethod
  def frombirthyear(cls, name, year):
    return cls(name, date.today().year - year)

  @staticmethod
  def isold(age):
    return age > 18

hen   = person('hendy', 21)
anto  = person.frombirthyear('hendy', 1990)

print(hen.age)
print(anto.age)

print(person.isold(22))

# generator function

def nextnumber():
  i=1;
  while True:
    yield i*i
    i += 1

for num in nextnumber():
  if num > 100:
    break
  print(num)

# return multiple ValueError
# using object

class Ujicoba:
  def __init__(self):
    self.str = "using this object"
    self.z = 99

def fun3():
  return Ujicoba()

a = fun3()
print(a.str)
print(a.z)


# using tuple
def ujicobatuple():
  string =  "using tuple"
  x = 20
  return string, x;

string, x = ujicobatuple()
print(string)
print(x)

# # using list
def list2():
   str2 = "using list"
   c = 12
   return [str2, c];

list = list2()
print(list)


# # using dictionary
# # A Dictionary is similar to hash or map in other languages. See this for details of dictionary
def dictio():
  d = dict();
  d['str'] = "this is using dictionary"
  d['a'] = 12
  return d

d = dictio()
print(d)

# partial function 
# Partial functions allow us to fix a certain number of arguments of a function and generate a new function

from functools import partial

def f(a, b, c, x):
  return 100*a + 10*b + 100*c + x

g = partial(f, 1, 2, 3)
print(g(5))

# another exercise

from functools import *

def add(a, b, c):
  return 100 / a + 10 * b + c

add_part = partial(add, c = 2, b = 1)
print(add_part(4))

# precision

a = 3.4536
  
# # using "%" to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using %) is : ",end="") 
print ('%.2f'%a) 
  
# # using format() to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using format()) is : ",end="") 
print ("{0:.2f}".format(a)) 
  
# # using round() to print value till 2 decimal places  
print ("The value of number till 2 decimal place(using round()) is : ",end="") 
print (round(a,2)) 

# # decorator
def welcome(fun):
  
  # #nested function
  def addwelcome(my_name):
    return " welcome to " + fun(my_name)

  return addwelcome

@welcome
def name(my_name):
  return my_name

print(name("hendy"))

# # attach_data in python
def new_data(fun):
      fun.data = 10
      return fun

@new_data
def add2(x, y):
  return x * y

print(add2(10,20))
print(add2.data)

# Decorator behavior

def hello_decorator(func):
  def inner1():
    print("Hello, this is before function execution")

    func()
    print("this is after func")

  return inner1

def function_to_be_used():
  print("this is inside the function")

function_to_be_used = hello_decorator(function_to_be_used)

function_to_be_used()

# exercise decorator

import time
import math

def calculate_time(func):
  def inner1(*args, **kwargs):
    begin = time.time()

    func(*args, **kwargs)

    end = time.time()
    print("Total time : ", func.__name__,end - begin)
  return inner1

@calculate_time
def factorial(num):
  time.sleep(2)
  print(math.factorial(num))

factorial(10)

# decorator with param

def decorator(*args, **kwargs):
  print("inside decorator")
  def inner(func):
    print("inside inner function")
    print("I like", kwargs['like'])
    return func
  return inner
@decorator(like = " coffe")
def func():
  print("inside actual function")

func()

# exercise decorator with param

def course(*args, **kwargs):
  print("welcome inside this course ")
  def person(func):
    print("Hello what is your name ?")
    print("my name :", kwargs['name'])
    return func
  return person
@course(name = " Hendy")
def func2():
  print("welcome inside in this course ")

func2()

# # iterator
class reverse:
  def __init__(self, data):
    self.data = data
    self.index = len(data)

  def __iter__(self):
    return self

  def __next__(self):
    if self.index == 0:
        raise StopIteration
    self.index -= 1
    return self.data[self.index]

def Main():
  rev = reverse('Hendy')
  for char in rev:
    print(char)

if __name__ == '__main__':
  Main()

# # generator 

# def reverse2(data):
#   for index in range(len(data)-1, -1, -1):
#     yield data[index]

# def Main2():
#   data = 'Hendy'
#   print(list(data[i] for i in range(len(data)-1,-1,-1)))

# if __name__=="__main__":
#   Main2()

