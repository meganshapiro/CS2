'''
Created on Mar 7, 2023

@author: MShapiro24
'''

def main():

    try:
            file1 = open("midsummer.txt", 'r')      #opens the midsummer.txt file
            print(file1)                            #prints the midsummer.txt files
        
    except:
            print('File cannot be opened:')         #if file cannot be opened, then tell the user
            exit()
    
    ms = dict()                                     #assigning name of dictionary 
    print(ms)                                       #print ms (dictionary)
    for line in file1:                              #goes through each line in file1
        line = line.upper()                         #treats words with upper and lower case letters as the same
        words = line.split()                        #.split separates words in the line by spaces
        for word in words:
            print(word)                             #print word found in file
            if word not in ms:                      #if word is not already found in dictionary
                ms[word] = 1                        #add word to dictionary and make the count 1
            else:
                ms[word] += 1                       #if word is already in dict, add 1 to the count
          
    del ms['O']         #deletes remaining words with no significant meaning 
    del ms['I']
    del ms['A']
    del ms['IN'] 
    del ms['OUR']
    del ms['AT']     
    del ms['TO']
    del ms['SO']
    del ms['IF'] 
    del ms['CAN'] 
    del ms['THE']
    del ms['HIM']
    del ms['BUT'] 
    del ms['AND']
    del ms['MY']
    del ms['YOU']
    del ms['US']
    del ms['THAT']
    del ms['THIS']
                    
    output = open(r'C:\Users\mshapiro24\CS\CS2\Assignments\Midsummer.csv', 'w')         #opens midsummer.txt as a csv file
    for key, value in ms.items():       #for word frequency in dictionary               
        if value > 20:                  #only keeps word if it is counted more than 20 times 
            output.write(key + "," + str(value) + "\n")         #prints word and the number of times it is counted



if __name__ == '__main__':
    main()