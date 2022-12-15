'''
Created on Nov 9, 2022

@author: MShapiro24
'''

def get_gcd(x, y):
    if (y==0):
        return x
    else:
        return get_gcd(y, x%y)
    
    













if __name__ == '__main__':
    pass