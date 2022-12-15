'''
Created on Nov 8, 2022

@author: MShapiro24
'''

def get_powers (a, n):

    if n == 0:
            return 1
     
    return (a*get_powers(a, n-1)) 


def main():

    print (get_powers(2, 3))

if __name__ == '__main__':
    main()