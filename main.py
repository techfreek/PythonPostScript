#Programmer: Alex Bahm
import re
import sys
from sps import *
global debug
global static
static = False
debug = True

pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'

#Takes a string, and uses the pattern provided to tokenize the file
def parse(s):
    tokens = re.findall(pattern, s)
    return tokens

#Takes a file, and joins all the lines in the file to one long string on the same line
def parseFile(f):
    tokens = parse(''.join(f.readlines()))
    return tokens

#Takes a token, then checks to see if it a recognized functions, and returns the number of arguments the function needs
def isOperator(token):
    if token[0] == '/': #Skips if its a to be defined variable
        return -1
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
    elif token == "dictz":
        return 1
    elif token == "begin":
        return 1
    elif token == "end":
        return 0
    else:
        value = lookup(token, static)
        if value != None:
            try:
                if value[0:1] == "{":
                    return -2
            except:
                pass
        return -1 #In case its anything else

#To process the functions with no inputs
def noInput(token):
    if token == "dup":
        dup()
        return None #since these do not return any values
    elif token == "exch":
        exch()
        return None
    elif token == "pop":
        popTop()
        return None
    elif token == "stack":
        stack()
        return None
    elif token == "top":
        top()
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
    elif token == "=":
        top()

#For functions that take one input, returns input relevant to the function
def oneInput(token, param):
    if token == "not":
        return notOp(param)
    elif token == "dict":
        dictz()
        return None
    elif token == "dictz":
        dictz()
        return None
    elif token == "begin":
        begin()
        return None

#Takes 3 inputs, the function name, and the two inputs and calls the functions, and returns input relevant to that function
def twoInput(token, paramA, paramB):
    if debug: print("Token = ", token, "ParamA = ", paramA, "ParamB = ", paramB)
    if token == "if":
        ifOp(paramA) #ifOp() pushes the result onto the stack
    elif token == "and":
        return andOp(paramA, paramB)
    elif token == "or":
        return orOp(paramA, paramB)
    elif token == "def":
        define(paramB, paramA)
        return None
    
#Takes 4 inputs, the function name, and the two inputs and calls the functions, and returns input relevant to that function
def threeInput(token, paramA, paramB, paramC):
    ifelseOp(paramC, paramB, paramA) #ifelseop pushes the code to be processed onto the stack

#Checks if a token is a variable
def isVar(token):
    value = lookup(token, static)
    if debug: print("Key: ", token, "Value: ", value)
    printDictStack()
    if(value == None): #checks if anything was returned
        return None #Not a variable
    else:
        return value

#Takes the tokens, processes them
def read(tokens):
    print("Reading!!")
    if debug: stack()
    #if debug: print("Tokens Length = ", len(tokens))
    i = 0 #starting i value
    while i < len(tokens): #Needed to use a while loop because a for loop would not let me change 'i' value when '{' were encountered and have that be reflected in further iterations
        print("Token: " + tokens[i])
        print("Tokens: ", end = "")
        for z in range(len(tokens)):
            print(tokens[z], end = " ")
        print("/n")
        print("I = " + str(i))
        opParams = isOperator(tokens[i]) #counts how many variables need to be passed, if any
        if debug: stack()
        if debug: print("\nToken[i] = ", tokens[i], " - ", opParams)
        if opParams == -1 and isVar(tokens[i]) != None: #if it is a variable
            if debug: printDictStack()
            value = lookup(tokens[i], static) #get the value
            if not(isinstance(value, (int, float))) and value[0] == "{" and value[len(value) - 1] == "}": #If the value happens to be a code block
                if debug: print("<--------------------------------Read again!")
                read(parse(value[1:-1])) #sends the parsed tokens of the value to the read function
                value = topVal() #pops it mostly for the purpose of printing it if need be
                if debug: print("Result: ", value)
                pushStack(value)
            else:
                pushStack(lookup(tokens[i], static)) #Checks if the tokens[i] is a variable before pushing it
        elif opParams == -2: #is a function
            dictz()
            begin()
            print("NewFunc!")
            read(parse(lookup(tokens[i], static)[1:-1])) #isOperator already tested and knows this is a function, hence no double checking
            end()
             
        elif(tokens[i] == '{'): #if a code block, concate to a string, then push on the stack as whole
            #codeBlock = ""
            #codeBlock += tokens[i]
            #blocks = 1 #how many code blocks are contained in the code block
            #if debug:  print("I = ", i, " tokens[i] = ", tokens[i])
            #for j in range((i + 1), len(tokens) - 1): #scans from after the { till the last token unless enough '}' are found 
                #codeBlock += " " + tokens[j]  #add token to string
                #if tokens[j] == "{": #Another code block has started
                    #blocks = blocks + 1
                #elif tokens[j] == "}": #another code block has ended, so make not
                    #blocks = blocks - 1
                    #if blocks == 0: #if we are now out of all code blocks, we can push that string onto the stack
                        #pushStack(codeBlock)
                        #break #Ends loop so we don't keep scanning for '}' when we don't need to
            #i = j #So we don't rescan those tokens
            codeBlock = concatFunc(tokens[i:])
            i += codeBlock[1]
            pushStack(codeBlock[0])
            
        elif(opParams != -1): #If it is an operator
            if debug: print("Operand: ", tokens[i])
            if(opParams == 0): 
                noInput(tokens[i])
            elif(opParams == 1):
                oneInput(tokens[i], topVal()) #passes the top most value
            elif(opParams == 2):
                twoInput(tokens[i], topVal(), topVal()) #top two values, etc
            elif(opParams == 3):
                threeInput(tokens[i], topVal(), topVal(), topVal())
                if tokens[i] == "ifelse": #This could be bundled above, but this allows for greater reuse
                    if debug: print("<--------------------------------Read again!")
                    read(parse(topVal()[1:-1]))#Takes the top most value, parses it, and evaluates it in read()
            if debug:
                if tokens[i] == "def": printDictStack

        else:
            if debug: print("Pushing...")
            pushStack(tokens[i])#If it is none of the above, it goes on the stack
        i = i + 1
    
    

if __name__== "__main__":
    if(len(sys.argv) > 2): #If arguments are passed, the file is opened, if not,  the fact.txt file is opened
        if sys.argv[1] == "-d":
            static = False
        else:
            static = True
        fn = sys.argv[1]
    else:
        static = True;
        fn = "test.txt"
    if debug: print("<--------------------------------Debug Mode On-------------------------------->")
    print("File: ", fn)
    stack()
    printDictStack()
    tokens = parseFile(open(fn, "r"))
    if debug: print(tokens)
    stack()
    dictz()
    begin()
    read(tokens)
    stack()
    printDictStack()
    wait = input("PRESS ENTER TO EXIT ") #So the window doesn't auto close if opened directly
