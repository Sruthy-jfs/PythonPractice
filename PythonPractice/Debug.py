#debugging

#linting: find errors even before we code. Present in IDE
#ide/editor: built in tools
#pdb: PYTHON DEBUGGER: Built in module

import pdb
def add (num1, num2):
    pdb.set_trace()
    temp=4*5
    return num1+num2

add(1,5)
print(add(1,5))


#step: goes to next line
#a: gives list of all arguments eg num1=1, num2=5
