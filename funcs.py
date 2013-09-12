#Programmer: Alex Bahm
global debug
from stack.py import *
debug = False

def add(a, b):
    push(a + b)
return a + b

def sub(a, b):
    push(a - b)
return a - b

def mul(a, b):
    push(a * b)
return a * b

def div(a, b):
    push(a / b)
return a / b

def eq(a, b):
    boolean = 0
    if a == b:
        boolean = 1
return boolean

def lt(a, b):
    lessThan = 0
    if a > b:
        lessThan = 1
return lessThan

def gt(a, b):
    greaterThan = 0
    if a < b:
        greaterThan = 1
return greaterThan
