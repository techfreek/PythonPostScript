#Programmer: Alex Bahm
global debug
debug = False

psStack = [] #values are stored in a list, with 0 being the top
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
def stack():
    print("OperandStack:")
    stackHeight = len(psStack) #gets length
    for i in range(stackHeight): #goes through each item
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
    for i in range(len(psStack)):
        if psStack[i] == "{}":#Scans for the top most empty dict on the operand stack
            psStack.pop(i) #pops it
    return {}

#Used in processing file
def topVal():
    val = psStack[0] #So I don't try to return a deleted value
    psStack.pop(0)
    return val

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
    if debug: print(boolVal)
    if boolVal != True: #This and the next 5 lines ensure it is a boolean value
        if boolVal != False: 
            raise ValueError('Error: Invalid input')
    if boolVal:
        pushStack(funcA)
    else:
        pushStack(funcB)

#<----------------------Math---------------------->
#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def add():
    vals = popTwo() #gets two values
    pushStack(int(vals[1]) + int(vals[0]))

#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def sub():
    vals = popTwo()
    pushStack(int(vals[1]) - int(vals[0]))

    
#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def mul():
    vals = popTwo()
    pushStack(int(vals[0]) * int(vals[1]))

#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def div():
    vals = popTwo()
    if vals[0] == 0:
        raise ValueError("Error: Cannot divide by zero") #So other errors don't arise
    pushStack(int(vals[1]) / int(vals[0]))

#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def eq():
    vals = popTwo()
    boolean = False
    if debug: print(vals)
    if str(vals[0]) == str(vals[1]): #Problems when they are not converted to the same type
        boolean = True
    pushStack(boolean)

#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def lt():
    vals = popTwo()
    lessThan = False
    if int(vals[0]) > int(vals[1]):
        lessThan = True
    pushStack(lessThan)
    
#No inputs, does a function call to get values, then pushes the answer on the stack, so no output
def gt():
    vals = popTwo() #recieves two values
    greaterThan = False
    if int(vals[0]) < int(vals[1]): #ensures the values are ints
        greaterThan = True
    pushStack(greaterThan)


#<----------------------Logical---------------------->
#recieves two boolean values, verifies they are boolean, then evaluates, pushes boolean value back on stack
def andOp(boolA, boolB): #named for and operator, but the shortened form of that name
    if boolA != True: #This and the next 5 lines ensure it is a boolean value
        if boolA != False:
            raise ValueError('Error: Invalid input')
    if boolB != True:#Ensures it is actually a boolean value
        if boolB != False:
            raise ValueError('Error: Invalid input')
    if boolA ==  boolB == True:
        pushStack(True)
    else:
        pushStack(False)

#recieves two boolean values, verifies they are boolean, then evaluates, pushes boolean value back on stack
def orOp(boolA, boolB):
    if boolA != True: #Ensures it is actually a boolean value
        if boolA != False:
            raise ValueError('Error: Invalid input')
    if boolB != True:#Ensures it is actually a boolean value
        if boolB != False:
            raise ValueError('Error: Invalid input')
    if boolA == True or boolB == True:
        pushStack(True)
    else:
        pushStack(False)

#recieves a boolean value, verifies it is boolean, then evaluates, pushes opposite boolean value back on stack
def notOp(boolVar):
    if boolVar != True: #Ensures it is actually a boolean value
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
        currDict = dictStack[i] #Gets topmost dictionary
        if debug: print(currDict)
        value = currDict.get(key, "No Value") #Returns value or "No Value" (helps differentiate between not being defined or being an actual value)
        if value != "No Value":
            return value #Run this to avoid the following error
    #return "No Value"

#Recieves a key and its value, and pushes it onto the current stack to use later. Either that or it raises an error
def define(key, value): #puts the value in the topmost dictionary
    if debug: print("Key: ", key, "Value: ", value)
    currDict = dictStack[0] #Gets the topmost dictionary
    if key == "true" or key == "false": #So people don't over-write the default
        raise ValueError("Error: You can't re-define True and False")
    currDict[key[1:]] = value #pushes the key onto the stack while ignoring the '/'

#Creates a new blank dictionary on the stack, and records its position
def dictz():
    pushStack({})#pushes empty dict

#Makes a call to get top most dict off the psStack, then put it on the dictStack
def begin():
    dictStack.insert(0, popDict()) #Get the dictionary off the opstack
    if debug: printDictStack()

#Makes a call to a built in list operator to remove the top most value on the dictStack
def end():
    dictStack.pop(0)

#Included for debugging purposes
def printDictStack():
    print("\nDict Stack: ")#Labeling & spacing
    stackHeight = len(dictStack) #gets length
    for i in range(stackHeight): #goes through each itme
        print(dictStack[i])
        print("==========================================================================")
