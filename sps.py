#Programmer: Alex Bahm
global debug
debug = False

psStack = [] #values are stored in a list, with 0 being the top
psStackDicts = [] #used to store the positions of dicts in the psStack, values are stored similar to the psStack
origDict = {'true': True, 'false': False} #stores variables, functions in the dictionary. true/false already exist so ps true/false can be converted to python True/False
dictStack = [origDict] #The dict stack stores values just like the psStack with the newest at dictStack[0]

#<-------------------------Stack------------------------->
#requires no inputs, just adds a duplicate of the top value
def dup():
    psStack.append(psStack[0])

#no inputs, just swaps the position of the values with a dual assignment
def exch():
    psStack[0], psStack[1] = psStack[1], psStack[0]

#No input, just removes top most value
def popTop():
    if len(psStack) > 0:
        psStack.pop(0)
    else:
        raise ValueError("Error: Can't pop. No values on the stack.")

#No inputs needed, just prints value, only output is the text displayed.
def stackPrint():
    stackHeight = len(psStack) #gets length
    for i in range(stackHeight): #goes through each itme
        print(psStack[i])

#Removes top most element and prints it
def top():
    print(psStack[0])
    popTop()

#No inputs, returns top two elements in a tuple
def popTwo(): #For use in mathmatical operations which use two digits
    if len(psStack) < 2:
        raise ValueError("Error: Not enough values to evaluate.")
    a = psStack.pop(0) 
    b = psStack.pop(0)
    return (a, b) #return as tuple

#input is a token from the input file
def pushStack(value):
    psStack.insert(0, value) #0 corresponds to the position, and the value is what goes there

#No inputs, returns the top most dictionary
def popDict():
    #algorithm works by counting how many values in the stack when pushed and popped. When popped, it counts that far from the end to the correct position
    if debug: print(psStack[len(psStack) - psStackDicts[0] - 1])
    return psStack.pop(len(psStack) - psStackDicts.pop(0) - 1) #uses the values from psStackDicts to remove the dictionaries

#<-------------------------Misc. Functions------------------------->
#is passed two values, a bool, and a function name. If the bool passes, the function is run
def ifOp(boolVal, function):
    if boolVal != True: #This and the next 5 lines ensure it is a boolean value
        if boolVal != False: 
            raise ValueError('Error: Invalid input')
    if boolVal:
        execute(function)

#simila to ifOp, instead it has two functions where if boolVal is false, funcB runs instead of just ending
def ifelseOp(boolVal, funcA, funcB):
    if boolVal != True: #This and the next 5 lines ensure it is a boolean value
        if boolVal != False: 
            raise ValueError('Error: Invalid input')
    if boolVal:
        execute(funcA)
    else:
        execute(funcB)

#Recieves a function name for processing
def execute(funcName):
    print("W.I.P.\n") #To come later, this is the interpreter/function executer

#<----------------------Math---------------------->
#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def add():
    vals = popTwo() #gets two values
    if isinstance(vals[0], (int, float, complex)) and isinstance(vals[0], (int, float, complex)): #Filters out bad inputs ie if some bad code is on the stack. Does not filter out bools.
        pushStack(vals[0] + vals[1])
    else:
        raise ValueError("Error: Input must contain digits")

#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def sub():
    vals = popTwo()
    if isinstance(vals[0], (int, float, complex)) and isinstance(vals[0], (int, float, complex)):
        pushStack(vals[0] - vals[1])
    else:
        raise ValueError("Error: Input must contain digits")
    
#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def mul():
    vals = popTwo()
    if isinstance(vals[0], (int, float, complex)) and isinstance(vals[0], (int, float, complex)):
        pushStack(vals[0] * vals[1])
    else:
        raise ValueError("Error: Input must contain digits")

#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def div():
    vals = popTwo()
    if isinstance(vals[0], (int, float, complex)) and isinstance(vals[0], (int, float, complex)):
        if vals[1] == 0:
            raise ValueError("Error: Cannot divide by zero")
        pushStack(vals[0] / vals[1])
    else:
        raise ValueError("Error: Input must contain digits")

#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def eq():
    vals = popTwo()
    if isinstance(vals[0], (int, float, complex)) and isinstance(vals[0], (int, float, complex)):
        boolean = False
        if vals[0] == vals[1]:
            boolean = True
        pushStack(boolean)
    else:
        raise ValueError("Error: Input must contain digits")

#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def lt():
    vals = popTwo()
    if isinstance(vals[0], (int, float, complex)) and isinstance(vals[0], (int, float, complex)):
        lessThan = False
        if vals[0] > vals[1]:
            lessThan = True
        pushStack(lessThan)
    else:
        raise ValueError("Error: Input must contain digits")    
#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def gt():
    vals = popTwo()
    if isinstance(vals[0], (int, float, complex)) and isinstance(vals[0], (int, float, complex)):
        greaterThan = False
        if vals[0] < vals[1]:
            greaterThan = True
        pushStack(greaterThan)
    else:
        raise ValueError("Error: Input must contain digits")


#<----------------------Logical---------------------->
#recieves two boolean values, verifies they are boolean, then evaluates, pushes boolean value back on stack
def andOp(boolA, boolB): #named for and operator, but the shortened form of that name
    if boolA != True: #This and the next 5 lines ensure it is a boolean value
        if boolA != False:
            raise ValueError('Error: Invalid input')
    if boolB != True:
        if boolB != False:
            raise ValueError('Error: Invalid input')
    if boolA ==  boolB == True:
        pushStack(True)
    else:
        pushStack(False)

#recieves two boolean values, verifies they are boolean, then evaluates, pushes boolean value back on stack
def orOp(boolA, boolB):
    if boolA != True:
        if boolA != False:
            raise ValueError('Error: Invalid input')
    if boolB != True:
        if boolB != False:
            raise ValueError('Error: Invalid input')
    if boolA == True or boolB == True:
        pushStack(True)
    else:
        pushStack(False)

#recieves a boolean value, verifies it is boolean, then evaluates, pushes opposite boolean value back on stack
def notOp(boolVar):
    if boolVar != True:
        if boolVar != False:
            raise ValueError('Error: Invalid input')
    if boolVar == True:
        pushStack(True)
    else:
        pushStack(False)

#<-------------------------Dictionary------------------------->
#Gets a token, checks in dictionary, then pushes value back on stack or raises an error. No return value
def lookup(key):
    for i in range(len(dictStack)): #scans all the dicts to see if it is a older variable
        if debug: print(i)
        currDict = dictStack[i]
        if debug: print(currDict)
        value = currDict.get(key, False)
        if value != False:
            if debug: print(value)
            pushStack(value)    
            return None #Run this to avoid the following error
    raise ValueError("Error: Variable, ", key, ", has not been defined")   

#Recieves a key and its value, and pushes it onto the current stack to use later. Either that or it raises an error
def define(key, value): #puts the value in the topmost dictionary
    currDict = dictStack[0]
    if key == "true" or key == "false":
        raise ValueError("Error: You can't re-define True and False")
    currDict[key] = value

#Creates a new blank dictionary on the stack, and records its position
def dictz():
    psStackDicts.insert(0, len(psStack)) #insert position data for popping onto psStackDicts
    pushStack({})#pushes empty dict

    #Makes a call to get top most dict off the psStack, then put it on the dictStack
def begin():
    dictStack.insert(0, popDict())

#Makes a call to a built in list operator to remove the top most value on the dictStack
def end():
    dictStack.pop(0)

#Included for debugging purposes
def printDictStack():
    stackHeight = len(dictStack) #gets length
    for i in range(stackHeight): #goes through each itme
        print(dictStack[i])
