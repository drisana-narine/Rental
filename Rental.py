import math

def calculateMiles(start, end):                                                                 #finds number of miles
    if end>start:                                                                               #finds miles when end odometer reading is greater than start odometer reading
        miles=(end-start)/10
        return miles
    else:                                                                                       #finds miles when start odometer reading is greater than end odometer reading
        end=end+1000000
        miles=(end-start)/10
        return miles
       
def moneysaverBill(code, miles, days):                                                          #finds price when code is m or M
    price=(40*days)+(0.25*miles)
    return price

def dailyBill(code, miles, days):                                                               #finds price when code is d or D
    if (miles/days)<=100:                                                                       #finds price when miles is less than or equal to 100 per day
        price=(60*days)
        return price
    else:                                                                                       #finds price when miles is greater than 100 per day
        miles=miles-(100*days)
        price=(60*days)+(0.25*miles)
        return price

def weeklyBill(code, miles, days):                                                              #finds price when code is w or W
    weeks=math.ceil(days/7)                                                                     #converts days to weeks
    if (miles/weeks)<=900:                                                                      #finds price when miles is less than equal to 900 per week                                                                          
        price=(190*weeks)
        return price
    elif (miles/weeks)<=1500:                                                                   #finds price when miles is greater than 900 and less than or equal to 1500 per week
        price=(190*weeks)+(100*weeks)
        return price
    else:                                                                                       #finds price when miles is greater than 1500 per week
        miles=miles-(1500*weeks)
        price=(190*weeks)+(200*weeks)+(0.25*miles)
        return price

def findPrice(code, miles, days):                                                               #finds price depending on code
    if code=="M":
        price=moneysaverBill(code, miles, days)
        return price
    elif code=="D":
        price=dailyBill(code, miles, days)
        return price
    elif code=="W":
        price=weeklyBill(code, miles, days)
        return price

def capitalize(code):                                                                           #capitalizes code if a lowercase letter was entered
    if code=="m":
        code="M"
        return code
    elif code=="d":
        code="D"
        return code
    elif code=="w":
        code="W"
        return code
    else:
        return code

def main():
    for x in range(3):     
        print("At the prompts, please enter the following:")
        print("")
        print("Customer's classification code (a character)")
        print("Number of days the motorcycle was rented (an integer)")
        print("Odometer reading at the start of the rental period (an integer)")
        print("Odometer reading at the end of the rental period (an integer)")
        print("------------------------------------------------------------------------")
        code=input("Customer code: ")
        code=capitalize(code)
        days=int(input("Number of days: "))                                                     #converts input for days to an integer
        odometer1=int(input("Odometer reading at the start: "))                                 #converts input for start odometer reading to an integer
        odometer2=int(input("Odometer reading at the end: "))                                   #converts input for end odometer reading to an integer
        miles=calculateMiles(odometer1, odometer2)                                              #calls function to calculate miles
        price=findPrice(code, miles, days)                                                      #calls function to find price
        print("Customer summary:")
        print("         classificaton code: ",code)
        print("         rental period (days): ",days)
        print("         odometer reading at start: ",odometer1)
        print("         odometer reading at end: ", odometer2)
        print("         Number of miles driven: ",miles)
        print("         amount due: $",price)
        print("------------------------------------------------------------------------")
   
main()
