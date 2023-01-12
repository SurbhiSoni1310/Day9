from art import logo
from time import sleep
import os
def find_max(auction):
    max=0
    for i in auction:
        if auction[i]>= max:
            max = auction[i]
            name = i
    return name


print(logo)
print("Welcome to the Secret Auction Program")
auction = {}
continue_loop = True
while continue_loop:
    name = input("What's your name ? : ")
    bid = int(input("What's your bid ? $"))
    auction[name] = bid
    right_input = True
    while right_input:
        other = input("Are there any other bidders ? Type 'yes' or 'no' : ").lower()
        if other == "yes":
            right_input = False
            os.system('cls')
            continue
        elif other == "no":
            print("Thank you")
            continue_loop = False
            right_input = False
        else:
            print("Wrong input. Try Again")
print("The Auction is won by : "+find_max(auction)+" with amount $"+str(auction[find_max(auction)]))
sleep(10)






