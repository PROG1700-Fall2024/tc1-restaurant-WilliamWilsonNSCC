#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.

"""
Student Name: William Wilson
Program Title: Logic and Programming
Description: Tech Check 1 Restaurant Bill
"""

def main():
    #restaurantBill amount through user input and print to make sure it is working
    restaurantBill = float(input("Please enter your bill amount: "))

    #tax the restaurantBill amount #*.15 then run print test
    billTax = restaurantBill*.15
    # print(billTax)

    #tipAmount = restaurantBill*.20 run a print test
    tipAmount = restaurantBill*.20
    # print(tipAmount)

    #print the totalPrice
    totalPrice = restaurantBill+billTax+tipAmount
    # print(totalPrice)
    
    #print billing table
    print("Your starting bill amount is: ${0} \nYour tax amount is: ${1} \nYour tip: ${2} \nYour total bill cost: ${3}".format(restaurantBill, billTax, tipAmount, totalPrice))

main()