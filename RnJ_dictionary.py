'''
Created on Feb 27, 2023

@author: MShapiro24
'''
def main():
        
    try:
        file1 = open("Romeo_Juliet.txt", 'r')           #opens the Romeo_Juliet.txt file
        print(file1)                                    #prints the Romeo_Juliet.txt file
    except:
        print('File cannot be opened:')                 #if file cannot be opened, tell the user
        exit()
        
        
    RnJ = dict()                                        #assigning name of dictionary 
    print(RnJ)                                          #print dictionary 
    for line in file1:                                  #goes through each line in file1
        line = line.upper()                             #treats words with upper and lower case letters as the same word
        words = line.split()                            #.split separates words in the line with spaces
        for word in words:
            print(word)                                 #print word found in file
            if word not in RnJ:                         #if word is not already found in dictionary 
                RnJ[word] = 1                           #add word to dictionary and make the count 1
            else:
                RnJ[word] += 1                          #if word is already in dict, add 1 to the count
                
    del RnJ['BY']                                       #deletes remaining words with no significant meaning
    del RnJ['AND']
    del RnJ['FROM']
    del RnJ['THE']
    del RnJ['SUCH']
    del RnJ['THS']
    del RnJ['A']
    del RnJ['S']
    del RnJ['T']
    del RnJ['O']
    del RnJ['OF']
    del RnJ['SHOULD']
                
    output = open(r'C:\Users\mshapiro24\CS\CS2\Assignments\Romeo_Juliet.csv', 'w')              #opens Romeo_Juliet.txt as a csv file
    for key, value in RnJ.items():                      #for word frequency in dictionary 
        if value > 20:                                  #only keeps word if it is counted more than 20 times
            output.write(key + "," + str(value) + "\n") #prints word and the number of times it is counted
    
    
    

if __name__ == '__main__':
    main()