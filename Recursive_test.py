'''
Created on Nov 11, 2022

@author: MShapiro24
'''

def get_factorial(n):
    """
    Get the factorial of a number
    Arguments:
        n: the number
    Returns:
        The factorial of the number
    """

    if n == 0:
        return 1  # the factorial of 0 is 1
    else:
        return n * get_factorial(n - 1)  # find the factorial, ex: 5! = 5*4*3*2*1
    
def get_summation(n):
    '''
    Arguments: 
        n: number value taken from main and changed in function
        get_summation: recalls function from within the function
    Takes:
        number variable from main
    Returns:
        sends edited product back to main
    '''
    if n == 0:
        return 0
    
    else:
        return n+get_summation(n-1)
    
    
def get_powers (a, n):
    ''' 
    Arguments:
        n: number that will be changed in the function
        get_powers: recalls function from the function
    Returns:
        power of a number
    '''
    if n > 0:
        n = a * get_powers(a,n-1)
        return n
    elif n == 0:
        n = 1
        return n
            


def get_sum_of_numbers_digits(n):
    """
    Add together a number's digits
    Arguments:
        n: the number
    Returns:
        sum: the sum of the number's digits
    """
    if n < 10:
        return (n)
    else:
        return(n % 10 + get_sum_of_numbers_digits(int(n/10)))


def get_fibonacci(n):
    '''
    Arguments: 
        n: number value taken from main and changed in function
        get_fibonacci: recalls function from within the function
    Takes:
        number variable from main
    Returns:
        sends edited product back to main
    '''
    if n == 0:
        return 0
            
    if n == 1:
        return 1
    
    else:
        return get_fibonacci(n-1)+get_fibonacci(n-2)
    
    
    
    
def get_product_of_2_whole_numbers(a, b):
    '''
    Get the product of two whole numbers
    Arguments:
        a: the first number
        b: the second number
    Returns:
        The product of a and b
    '''

    if a < b:  # if a is less than b switch the numbers
        return get_product_of_2_whole_numbers(b, a)


    elif b != 0:  # calculate b, times sum of a
        return (a + get_product_of_2_whole_numbers(a, b - 1))

    else:  # if a number is 0 return 0
        return 0


def main():
    
    info1 = input("please choose a function number:\n" + "1. factorial:\n" + "2. summation:\n" + "3. powers:\n" + "4. sum of numbers digits:\n" + "5. fibonacci:\n" + "6. product of 2 whole numbers:\n")
    
    if info1 == "1":
        info2 = input("insert a number n\n")
        info2 = int(info2)
        print(get_factorial(info2))
        
    elif info1 == "2":
        info2 = input("insert a number n\n")
        info2 = int(info2)
        print(get_summation(info2))
        
    elif info1 == "3":
        a = int(input("insert a number"))
        n = int(input("insert a second number"))
        print(get_powers(a, n))
           
        
    elif info1 == "4":
        n = int(input("insert a number"))
        print(get_sum_of_numbers_digits(n))
        
    elif info1 == "5":
        info2 = int(input("insert a number"))
        info2 = int(info2)
        print(get_fibonacci(info2))
    
    elif info1 == "6":
        info2 = input("insert a number")
        info2 = int(info2)
        info3 = input("insert a number")
        info3 = int(info3)
        print(get_product_of_2_whole_numbers(info2,info3))
        
    else:
        print("please restart and enter a number on the menu")
        main()
        
    

if __name__ == '__main__':
    main()

