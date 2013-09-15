#Programmer: Alex Bahm
global debug
debug = False

psStack = []
psStackDicts = []
origDict = {true: '1', false: '0'}
dictStack = [origDict]

#<-------------------------Stack------------------------->
def dup():
    psStack.append(psStack[0])

def exch():
    psStack[0], psStack[1] = psStack[1], psStack[0]

def popTop():
    psStack.pop(0)

def stackPrint():
    stackHeight = len(psStack)
    for i in range(stackHeight):
        print(psStack[i], "\n")

def top():
    print(psStack(0), "\n")
    return psStack.pop(0)

def poptwo():
    a = psStack.pop(0)
    b = psStack.pop(0)
    return (a, b)

def pushStack(value):
    psStack.insert(0, value)

def popDict():
    return psStack.pop(len(psStack) - psStackDicts.pop(0))

#<-------------------------Misc. Functions------------------------->

def ifOp(boolVal, function):
    if boolVal:
        execute(function)

def ifelseOp(boolVal, funcA, funcB):
    if boolVal:
        execute(funcA)
    else:
        execute(funcB)


def execute(funcName):
    print("W.I.P.\n")


    
#<----------------------Math---------------------->
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


#<----------------------Logical---------------------->
def andOp(boolA, boolB): #named for and operator, but the shortened form of that name
    if boolA != True:
        if boolA != False:
            raise NameError('Error: Invalid input')
    if boolB != True:
        if boolB != False:
            raise NameError('Error: Invalid input')
    if boolA ==  boolB == True:
        return True
    else:
        return False

def orOp(boolA, boolB):
    if boolA != True:
        if boolA != False:
            raise NameError('Error: Invalid input')
    if boolB != True:
        if boolB != False:
            raise NameError('Error: Invalid input')
    if boolA == True or boolB == True:
        return True
    else:
        return False

def notOp(boolVar):
    if boolVar != True:
        if boolVar != False:
            raise NameError('Error: Invalid input')
    if boolVar == True:
        return False
    else:
        return True

#<-------------------------Dictionary------------------------->

def lookup(key):
    for i in len(dictStack):
        currDict = dictStack[i]
        if key in dictionary.values():
            value = dictionary.get(key, 0)
            pushStack(value)
            return value
    raise NameError("Error: Variable, ", key, ", has not been defined")
    

def define(key, value):
    currDict = dictStack[0]
    if key == "true" or key == "false":
        return None;
    dictionary[key] = value

def dictz():
    psStackDicts.insert(0, len(psStack))
    push({})

def begin():
    dictStack.insert(0, popDict())

def end():
    dictStack.pop(0)
