# Dictionary on mini market
inventory = {
    "apple": 50,
    "banana": 100,
    "orange": 80,
    "milk": 30,
    "bread": 20
}

# Customer request
item = input("Enter the item you want: ").lower()

if item == "apple":
    print("We have", inventory["apple"], "apples in stock.")
elif item == "banana":
    print("We have", inventory["banana"], "bananas in stock.")  
elif item == "orange":
    print("We have", inventory["orange"], "oranges in stock.")
elif item == "milk":
    print("We have", inventory["milk"], "packs of milk in stock.")
elif item == "bread":
    print("We have", inventory["bread"], "loaves of bread in stock.")
else:
    print("Sorry, that item is not available.")