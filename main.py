#Programmer: Alex Bahm
import re
import sys
from sps.py import *
global debug
debug = False

pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'

def parse(s):
    tokens = re.findall(pattern, s)
    return tokens

def parseFile(f):
    tokens = parse(''.join(f.readlines()))
    return tokens

def noInput(token):
    if token == "dup":
        dup()
        return None
    elif token == "exch":
        exch()
        return None
    elif token == "pop":
        popTop()
        return None
    elif token == "stack":
        stackPrint()
        return None
    elif token == "top":
        top()
        return None
    elif token == "begin":
        begin()
        return None
    elif token == "end":
        end()
        return None
    elif token == "add":
        return add()
    elif token == "sub":
        return sub()
    elif token == "mul":
        return mul()
    elif token == "div":
        return div()
    elif token == "eq":
        return eq()
    elif token == "lt":
        return lt()
    elif token == "gt":
        return gt()

def oneInput(token, param):
    if token == "not":
        return notOp(param)
    elif token == "dict":
        dictz()
        return None

def twoInput(token, paramA, paramB):
    if token == "if":
        if ifOp(paramA):
            return paramB
    elif token == "and":
        return andOp(paramA, paramB)
    elif token == "or":
        return orOp(paramA, paramB)
    elif token == "def":
        define(paramA, paramB)
        return None

def threeInput(token, paramA, paramB, paramC):
    if token == "ifelse":
        if ifelseOp(paramA):
            return paramB
        else:
            return paramC
    
def isOperator(token):
    if token == "dup":
        return 0
    elif token == "exch":
        return 0
    elif token == "pop":
        return 0
    elif token == "stack":
        return 0
    elif token == "top":
        return 0
    elif token == "if":
        return 2
    elif token == "ifelse":
        return 3
    elif token == "add":
        return 0
    elif token == "sub":
        return 0
    elif token == "mul":
        return 0
    elif token == "div":
        return 0
    elif token == "eq":
        return 0
    elif token == "lt":
        return 0
    elif token == "gt":
        return 0
    elif token == "and":
        return 2
    elif token == "or":
        return 2
    elif token == "not":
        return 1
    elif token == "def":
        return 2
    elif token == "dict":
        return 1
    elif token == "begin":
        return 0
    elif token == "end":
        return 0
    else:
        return -1

def isVar(token):
    value = lookup(token)
    if(!value):
        return token #Not a variable
    else:
        return value

def read(tokens):
    for i in range(1, len(tokens) - 1):
        opParams = isOp(token[i])
        if(opParams > 0):
            if(opPararms == 0):
                noInput(token[i])
            elif(opParams == 1):
                oneInput(token[i], topVal())
            elif(opParams == 2):
                twoInput(token[i], topVal(), topVal())
            elif(opParams == 3):
                threeInput(token[i], topVal(), topVal(), topVal())
        else:
            pushStack(isVar(tokens[i])) #Checks if the token is a variable before pushing it
        

if __name__=="__main__":
    #fn = sys.argv[1]
    fn = "fact.txt"
    tokens = parseFile(open(fn, "r"))
    print(tokens)
    read(tokens)
