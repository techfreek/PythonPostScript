#Programmer: Alex Bahm
global debug
debug = False

class stack:
    psStack = []
    def dup():
        psStack.append(psStack[0])

    def exch():
        psStack[0], psStack[1] = psStack[1], psStack[0]

    def pop():
        psStack.pop(0)
        

    def top():
        return psStack.pop(0)

    def poptwo():
        a = psStack.pop(0)
        b = psStack.pop(0)
        return (a, b)

    def push(value):
        psStack.insert(0, value)

    def popDict():
        #Develop method to find and pop dictionar

