import rent
from datetime import *

name = rent.name
ids = rent.ids
rent.basket = []
rent.basket_dict = {}

# date and time
year = str(datetime.now().year)
month = str(datetime.now().month)
day = str(datetime.now().day)
hour = str(datetime.now().hour)
minutes = str(datetime.now().minute)
date_today = year + " - " + month + " - " + day + " , " + hour + " : " + minutes 




def ren():
    #read the data that the customer has previously rented
    rented_items = open(name.upper()+" "+str(ids)+" rent cart"+".txt",'r')
    rented_items_lines = rented_items.readlines()
    Dict_rent = {} 

    #store the data in a dictionery
    for i in range(1,len(rented_items_lines) + 1):    
        Dict_rent[i] = rented_items_lines[i-1].split(",")      
    
    for i in range(1, len(rented_items_lines)):
        Dict_rent[i].pop(6)           
    
    print(Dict_rent)
    
   
    amount = float(Dict_rent[1][5])
    quantity = float(Dict_rent[1][3])

    # to remove $ from the price
    count = 0
    price1 = "" 
    for i in Dict_rent[1][4]:
        if count > 0:
            price1 = price1 + i 
        count = count + 1

    price = float(price1)
    number_of_days = (amount *5)/(quantity * price)

    # for rented date:
    date_data = open(name.upper()+" "+str(ids)+" rented"+".txt","r").readlines()
    date_data_date = date_data[3].split(",")[0].split("-")
    d0 = date(int(date_data_date[0]),int(date_data_date[1]),int(date_data_date[2]))
    d1 = date(int(year), int(month), int(day))
    difference = (d1 - d0).days

    #for total amount
    total = float(0)
    for i in range(1, len(Dict_rent)):
        total = total + float(Dict_rent[i][5])
    

    # for fine
    fine = 0
    if number_of_days < difference:
        overdue = difference - number_of_days
        for i in range(1, len(Dict_rent)):
            fine = fine + (price/5)*int(Dict_rent[i][3]) * overdue
    
    

    # printing the bill generated after returning
    print("The items you have rented previously are:")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("  Number of days: ", int(number_of_days))
    print("  Rented on: ",date_data[3]," Returned on: ",date_today,"\n  Number of days passed: ", difference )
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("  Sno\t\tCostume ID\t\tCostume\t\t\tBrand\t\t\tQuantity\t\tPrice(5 days)\t\tAmount") 
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    for i in range(1, len(Dict_rent)):
        print("  {0}\t\t{1}\t\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t\t\t${6}\n".format(i, Dict_rent[i][0],Dict_rent[i][1],Dict_rent[i][2],Dict_rent[i][3],Dict_rent[i][4],Dict_rent[i][5])) # prints uptop indexes 3 (because 4th is"\n" or "" ) of each list from each index of the dictionery 
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Total: $", "{:.2f}".format(total))
    print("Overdue Fine: $","{:.2f}".format(fine))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Grand Total: $","{:.2f}".format(total + fine))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #updating dictionery containing tthe stock data
    Dict = rent.read_basket()
    for i in range(1, len(Dict_rent)):
        Dict[int(Dict_rent[i][0])][3] = str(int(Dict[int(Dict_rent[i][0])][3]) + int(Dict_rent[i][3]))
    print(Dict)

    #updating the stock.txt file
    write(Dict)


    # keeping the record for the returned data
    bill(name, ids, number_of_days, date_today, difference, Dict_rent, total, fine, date_data)
    
    #record of returened items
    basket_rent = open(name.upper()+" "+str(ids)+" return cart"+".txt",'w')
    for i in range(1, len(Dict_rent)):            
        for j in range(6):         
            basket_rent.write(str(Dict_rent[i][j]))           
            basket_rent.write(',')    
        basket_rent.write("\n")  
    
def bill(name, ids, number_of_days, date_today, difference, Dict_rent, total, fine, date_data):
    bill = open(name.upper()+" "+ids+" returned"+".txt","w")
    bill.write("Your bill \n")
    bill.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    bill.write("  Number of days: "+ str(number_of_days) + "\n")
    bill.write("  Rented on: "+str(date_data[3])+"  Returned on: "+str(date_today)+"\n  Number of days passed: "+ str(difference ) + "\n")
    bill.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    bill.write("  Sno\t\tCostume ID\t\tCostume\t\t\tBrand\t\t\tQuantity\t\tPrice(5 days)\t\tAmount\n") 
    bill.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")
    for i in range(1, len(Dict_rent)):
        bill.write("  {0}\t\t{1}\t\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t\t${6}\n".format(i, Dict_rent[i][0],Dict_rent[i][1],Dict_rent[i][2],Dict_rent[i][3],Dict_rent[i][4],Dict_rent[i][5])) # prints uptop indexes 3 (because 4th is"\n" or "" ) of each list from each index of the dictionery 
        bill.write("\n")
    bill.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    bill.write("Total: $"+ str("{:.2f}".format(total)))
    bill.write("\n")
    bill.write("Fine: $"+str("{:.2f}".format(fine)))
    bill.write("\n")
    bill.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    bill.write("\n")
    bill.write("Sum Total: $"+str("{:.2f}".format(total + fine)))
    bill.write("\n")
    bill.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

def write(Dict):
    stock2 = open('Stock.txt','w')     
    for i in range(1, len(Dict)+1):         
        for j in range(4):         
            stock2.write(Dict[i][j])         
            stock2.write(',')       
        stock2.write("\n")     
    stock2.close()




