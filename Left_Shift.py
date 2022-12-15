'''
Created on Oct 11, 2022

@author: MShapiro24
'''
from turtledemo.nim import computerzug

#shifts characters to the left and adds pound signs at end
def leftshift(x, text):

    #takes characters off of front of word starting at 0 
    pound = text[0:x]
    pound = len(pound) * '#'
    
    text = text[x:]
    text = text + pound
    
    
y = leftshift(3, 'COMPUTER')  
print(y)  