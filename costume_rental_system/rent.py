from datetime import date

basket = []                              
basket_dict ={}                             
name = input("Please Enter Your name: \n")
ids = input("\nEnter Your Contact Number: ")



# date and time
date_today = date.today()
print("Today's date:", date_today)



def read_basket():
    stock = open('Database.txt','r')               
    stock_lines = stock.readlines()             
    Dict = {}                          

    for i in range(1, len(stock_lines) + 1): 
        Dict[i] = stock_lines[i-1].split(",")     
    
    for i in range(1, len(Dict) + 1):  
        Dict[i].pop(4)                 

    return Dict




while True: 
    try:
        days = int(input("Enter the number of days you want to rent the costume for: "))
        print("\n__________________________________________________________________________________________")
        break
    except:
        print("Enter valid data")


Dict = read_basket()
def rent():
    #try:
        
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("  ID\t\tCostume\t\t\tCostume Brand\t\tPrice\t\t\tQuantity") 
        print("----------------------------------------------------------------------------------------------------------------------------------\n")
    
        for i in range(1, len(Dict)+1):
            print("  {0}\t\t{1}\t\t{2}\t\t{3}\t\t\t{4}\n".format(i, Dict[i][0],Dict[i][1],Dict[i][2],Dict[i][3])) 
        print("-----------------------------------------------------------------------------------------------------------------------------------")

        user = int(input("Enter the ID of the costume you want to rent: "))    
        present = False 

        for i in range(1, len(Dict) + 1):       
            if user == i:
                present = True      
                break
    
        if present == False: 
            print("\n\n")
            print("-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-")
            print("\t\tPlease Enter a valid ID !!! ")
            print("-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-__-\n\n")
            rent()
        else:

            if int(Dict[user][3]) == 0:
                print("\n\n")
                print("++++++++++++++++++++++++++++++++++++++")
                print("This particular Costume is out of stock !!! ")
                print("++++++++++++++++++++++++++++++++++++++\n\n")
                rent()
            else: 
                print("Costume ID is {0}\n\n".format(user))
                print("+++++++++++++++++++++")    
                print("Selected costume is available")
                print("+++++++++++++++++++++\n\n")

                user_req = int(input("Enter the Quantity of the costume you want to rent: ")) 

                if int(Dict[user][3]) < user_req:     
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("Sorry the quantity provided is greater than what we have in stock!!!")     
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print(Dict, "\n\n")
                    rent()
                else:

                    # remove $ from the price
                    count = 0
                    price = "" 

                    for i in Dict[user][2]:
                        if count > 0: 
                            price = price + i 
                        count = count + 1
                    
                    
                    actual_price = "{:.2f}".format((int(price)/5) *user_req * days) 
           

                    basket.append([user,Dict[user][0], Dict[user][1], str(user_req), Dict[user][2], actual_price ]) 
                    for i in range(1,len(basket)+1):
                        basket_dict[i] = basket[i-1]

                    print("Your basket:\n {0}".format(basket_dict))


                    Dict[user][3]= str(int(Dict[user][3]) - user_req)     

                    reask_validation = False 

                    while reask_validation == False:
                        reask = input("Do you want to rent any other costume from our list? (Yes/No): ")
                        if reask == "Yes": 
                            rent()
                            reask_validation = True
                        elif reask == "No": 
                            reask_validation = True
                            bills(name, ids, days, date_today, basket_dict)
                            print(Dict)        
                            update_stock(Dict) 
                            bill(name, ids, days, date_today, basket_dict) 
                            basket_(name, ids, basket_dict, date_today) 
                            clear_() 
                            
                        else:
                            print("+++++++++++++++++++++++")
                            print("  Enter either Yes or No ")
                            print("+++++++++++++++++++++++")
        


def bills(name, ids, days, date_today, basket_dict):  
    print("Your Receipt:\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("  Name: "+name+"\t\t" + "ID: "+ids +"\t\t"+ "For: "+ str(days) + " Day/s" +"\n  "+ str(date_today))
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------") 
    print("  Sno.\t\tCostume ID\t\tCostume Name\t\tBrand\t\tQuantity\t\trate\t\tTotal  ")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in range(1, len(basket_dict) + 1): 
        print("  {0}\t\t{1}\t\t\t{2}\t\t{3}\t{4}\t\t{5}\t\t{6}  ".format(i,basket_dict[i][0], basket_dict[i][1], basket_dict[i][2], basket_dict[i][3],basket_dict[i][4], "$" + str(basket_dict[i][5])  )) # i-1 because i starts form 1 and list index starts from 0
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    total_amount = float(0) 
    for i in range(1, len(basket_dict)+1):
        total_amount = total_amount + float(basket_dict[i][5])
                    
    print("Total Amount:","$" + str("{:.2f}".format(total_amount)))
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")


def update_stock(Dict):
    stock2 = open('Stock.txt','w')    
    for i in range(1, len(Dict)+1):
        for j in range(4):          
            stock2.write(Dict[i][j])           
            stock2.write(',')           
        stock2.write("\n")      
    stock2.close()
    

def bill(name, ids, days, date_today, basket_dict):
    bill = open(name.upper()+" "+str(ids)+" rented"+".txt","w")
    bill.write("Your Receipt:\n")
    bill.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    bill.write("\n")
    bill.write("  Name: "+name+"\t\t" + "ids: "+ids +"\t\t"+ "For: "+ str(days) + " Day/s" +"\n  "+ str(date_today))
    bill.write("\n")
    bill.write("-----------------------------------------------------------------------------------------------------------------------")
    bill.write("\n")
    bill.write("  Sno.\t\tCostume ids\t\tCostume Name\t\tBrand\t\tQuantity\trate\t\tTotal  ")
    bill.write("\n")
    bill.write("-----------------------------------------------------------------------------------------------------------------------")
    bill.write("\n")
    for i in range(1, len(basket_dict) + 1): # i+1 becaust Sno starts form 1
        bill.write("  {0}\t\t{1}\t\t\t{2}\t\t{3}\t{4}\t\t{5}\t\t{6}  ".format(i,basket_dict[i][0], basket_dict[i][1], basket_dict[i][2], basket_dict[i][3],basket_dict[i][4], "$" + str(basket_dict[i][5])  )) # i-1 because i starts form 1 and list index starts from 0
        bill.write("\n")
    bill.write("-----------------------------------------------------------------------------------------------------------------------")
    bill.write("\n")
    total_amount = float(0) # local variable to store total amount
    for i in range(1, len(basket_dict)+1): # adds the prices in the basket and stores in total_amount
        total_amount = total_amount + float(basket_dict[i][5])
                    
    bill.write("Total Amount: "+"$" + str("{:.2f}".format(total_amount)))# total as float with 2 digits after decimal
    bill.write("\n")
    bill.write("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    bill.close()



def basket_(name, ids, basket_dict, date_today):
    basket_p = open(name.upper()+" "+str(ids)+" rent cart"+".txt",'w')      
    for i in range(1, len(basket_dict)+1):            
        for j in range(6):        
            basket_p.write(str(basket_dict[i][j]))
            basket_p.write(',')           
        basket_p.write("\n")     
    basket_p.write(str(date_today))
    basket_p.write("\n")
    basket_p.close()
    return basket_p




def clear_():
    empty = False
    while empty == False:
        try:
            basket.pop() 
            basket_dict.popitem() 
        except:
            empty = True 
    
    return empty
    
