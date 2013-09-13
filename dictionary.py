#Programmer: Alex Bahm
from stack.py include *
global debug
debug = False

class dictionary:
    origDict = {true: '1', false: '0'}
    dictStack = [origDict]
    
    def lookup(key):
        
        for i in len(dictStack):
            currDict = dictStack[i]
            if key in dictionary.values():
                value = dictionary.get(key, 0)
                return value
                
        print("Error: Variable, ", key, ", has not been defined")
        value = None
    

    def edit(key, value):
        currDict = dictStack[i]
        if key == "true" or key == "false"
            return None;
        dictionary[key] = value

    def dictz():
        #create dict and push on operator stack

    def begin():
        #Push dict on dict stack from operator stack

    def end():
        dictStack.pop(0)

