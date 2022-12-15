'''
Created on Oct 17, 2022

@author: MShapiro24
'''


def leftcirc(x,text):
    
    circ = text[x:]
    text = text[:x]
    text = circ + text
    
    return text

y = leftcirc(3, 'COMPUTER')
print(y)


