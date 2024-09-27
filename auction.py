import os

# This function clear out the screen
def clear_screen():
    os.system('cls')

print("welcome to auction program")

list_of_bids = []
list_of_names = []

while True:
    name = input("what is your name :")
    list_of_names.append(name)
    bid = int(input("what is your bid :"))
    list_of_bids.append(bid)
    ask = input("are there any other bidders type 'yes' or 'no':")
    if ask == "yes":
        # calling the function for clearing out the screen
        clear_screen()

    # if user type 'no' loop ends  
    elif ask == 'no':
        break
# Getting highest bid using max function
highest_bid = max(list_of_bids)

# getting the name of person having highest bid using index (i)
for i in range(len(list_of_bids)):
    if highest_bid == list_of_bids[i]:
        highest_bid_person = list_of_names[i] 

print("The person gave the highest bid is",highest_bid_person)        
