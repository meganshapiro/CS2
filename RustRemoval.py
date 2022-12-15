'''
Name: Megan Shapiro
Date: October 2, 2022
Description: A program that allows the user to get the price of their package 
            when entering its dimensions
Bugs: None
Features: Allows user to enter in length, height, and width of package
          Tells the user 'unmailable' when information is invalid
          Allows user to enter in new information over again without having to restart
Log: Submitted for a grade on October 2, 2022
Plan:
    1. Convert all entered information into floats or integers
    2. Create functions for the type of package (getType), zip code ranges (rangeZip),
       and cost (getCost) 
    3. Created a counter so that user can keep entering in information without having to restart
'''
type = 0

def getType(l, h, w):
    
#getType determines package type based on 3 variable passed from main: 
#l = length, h = height, w = width
    

    
        if (l >= 3.5 and l <= 4.25) and (h >= 3.5 and h <= 6) and (w >= .007 and w <= .016):
            type = 1
            
        elif (l > 4.25 and l < 6) and (h > 6 and h < 11.5) and (w >= .007 and w <= .015):
            type = 2
            
        elif (l >= 3.5 and l <= 6.125) and (h >= 5 and h <= 11.5) and (w > .016 and w < .25):
            type = 3
            
        elif (l > 6.125 and l < 24) and (h >= 11 and h <= 18) and (w >= .25 and w <= .5):
            type = 4
            
        elif (l > 24 and h > 18 and w > .5) and (l + l + h + h + w + w <= 84):
            type = 5
            
        elif (l + h + h + w + w >= 84 and l + h + h + w + w <= 130):
            type = 6
            
        else:
            print("UNMAILABLE") 
            type = 7            

        return type

def rangeZip(zip):
    
#rangeZip determines the starting point and ending point for each zone number
     
    zone_start = 0 
 
    #zone_start states that the starting zone is zero
 
    if (zip >= 1 and zip <= 6999): 
        zone_start = 1 
    elif (zip >= 7000 and zip <= 19999): 
        zone_start = 2 
    elif (zip >= 20000 and zip <= 35999): 
        zone_start = 3
    elif (zip >= 36000 and zip <= 62999):
        zone_start = 4
    elif (zip >= 63000 and zip <= 84999):
        zone_start = 5
    elif (zip >= 85000 and zip <= 99999):
        zone_start = 6

    return zone_start


def getCost(type, net_zones):

#getCost calculates the price of the piece of mail

    price = 0
    
    if type == 1:
        price = (.2 + net_zones*(.03))
    elif type == 2:
        price = (.37 + net_zones*(.03)) 
    elif type == 3:
        price = (.37 + net_zones*(.04))
    elif type == 4:
        price = (.6 + net_zones*(.05))  
    elif type == 5:
        price = (2.95 + net_zones*(.25))      
    elif type == 6:
        price = (3.95 + net_zones*(.35))
            
            
    return price

def main():
   
#main holds the basic information for the code   
   
    type = 0
    counter = 0

    while counter < 5:
    
        try:    #try except to tell user their mail is 'unmailable' when typing in information wrong
        
            data = input("l, h, w, z1, and z2:")  
          
            data = data.split(",")
            
            l = data[0]
            l = float(l)
            h = data[1]
            h = float(h)
            w = data[2]
            w = float(w)
            z1 = data [3]
            z1 = int(z1)
            z2 = data[4]
            z2 = int(z2)
        
        except:
            print("UNMAILABLE")
            continue
        
            
        zone_start = rangeZip(z1)
        zone_end = rangeZip(z2)
        type = getType(l, h, w)
        
        #makes sure each variable is assigned to its specific function
    
        net_zones = abs(zone_start - zone_end)
        
        #taking the absolute values of zone_start and zone_end so the value will never be negative
    
        price = getCost(type, net_zones)
        
        print(f"{price :.2f}".lstrip("0"))
        
        #prints the total price and if the value is less than one, it will print without a zero in the ones place
        

        
        counter = counter + 1
        
        #makes sure the same prompt to ender in dimensions of mail appears each time 
        
if __name__ == '__main__':
    main()
