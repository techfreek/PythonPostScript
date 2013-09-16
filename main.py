#Programmer: Alex Bahm
global debug
debug = False
from sps import *

#This file has not practical purpose in the long run. It is built to show off the functionality and bug-free-ness of the existing code. It will not exist in the final version.

if __name__ == '__main__':
    
    value = 20
    print("Testing stack: Pushing 0 - 19")
    for i in range(value):
        pushStack(i)
    stackPrint()

    print("\nTesting math functions:")
    print("Adding")
    add()
    top()
	
    print("Subtracting")
    sub()
    top()
	
    print("Multiplying")
    mul()
    top()

    print("Dividing")
    div()
    top()

    print("Equality")
    eq()
    top()

    print("Less Than")
    lt()
    top()

    print("Greater than")
    gt()
    top()


    print("\nTesting Dictionary")
    print("Running Dictz()")
    dictz()

    print("Running begin()")
    begin()
    
    print("Defining Alex: Bahm")
    define('Alex', 'Bahm')
    print("Defining 355: Programming Language Design")
    define('355', 'Programming Language Design')
    print("Defining Go: Cougs!")
    define('Go', 'Cougs!')
    print("Defining Apple: iPhone")
    define('Apple', 'iPhone')
    print("Defining NSA: Spying")
    define('NSA', 'Spying')

    print("\nLooking up: Alex, 355, Go, Apple, NSA")
    lookup('Alex')
    top()
    lookup('355')
    top()
    lookup('Go')
    top()
    lookup('Apple')
    top()
    lookup('NSA')
    top()

    print("Running end")
    end()

    print("Looking up Alex")
    print("\n<-----------------This will cause an error----------------->")
    print("This is to show that Alex is not in the bottom most \n(only surviving) dictionary")
    lookup('Alex')
