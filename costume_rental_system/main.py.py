print("-------------------------------------------------------------------")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("   Welcome to Our Shrestha Costume Rental Store"  )
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("--------------------------------------------------------------------\n\n")

import rent
import return_

def main():
    condition = True
    while condition == True:
        print("Select a Desirable Option \n(1) || Type r to rent a costume\n(2) || Type ren to return a costume\n(3) || Type E to exit.\n")
        message =(input("Enter an option: "))
        if message =="r":
            print("\n\nLet's rent a costume of different brands with affordable price.\n\n")
            rent.rent()
            main()
        elif message == "ren":
            print("\n\nLet's return the rented costumes\n\n")
            return_.ren()
            ree()
        elif message == "E":
            print("\n\n###################################################################\n")
            print("<<<<<<<<<<<<<<<<<<<<Thank you Mr/Ms: " + rent.name + ">>>>>>>>>>>>>>>>>>>>>>>")
            print("\n####################################################################")
            End()
            break
        else:
            print("\n\nInvalid input!!!\nPlease select the value as per the provided as options\n\n")
            main()
    

def ree():
    print("\n\nThe costume has been returned.Thank you!!!\n\n")
    

def End():
    print("\n\n \t\tThank you for using our application for rental purpose... ")
    print("\t\t\t\tVisit again!!!")
    print("___________________________________________________________________________________________________\n")

    
main()
        
        

      


