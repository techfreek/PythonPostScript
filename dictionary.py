#Programmer: Alex Bahm
global debug
debug = False

class dictionary:
    def lookup(dictionary, key):
        if key in dictionary.values():
            value = dictionary.get(key, 0)
        else:
            print("Error: Variable, ", key, ", has not been defined")
            value = None
    return value

    def edit(dictionary, key, value):
        dictionary[key] = value
    return None

