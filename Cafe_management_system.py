menu = {
    "espresso": 3.00,
    "americano": 3.50,
    "cappuccino": 4.00,
    "latte": 4.50,
    "mocha": 5.00,
    "hot chocolate": 4.00,
    "chai latte": 4.00,
    "flat white": 4.50,
    "iced americano": 3.75,
    "iced latte": 4.75,
    "iced mocha": 5.25,
    "iced tea": 3.00,
    "cold brew": 4.00,
    "lemonade": 3.50,
    "berry blast": 6.00,
    "tropical nango": 6.00,
    "green detox": 6.50,
    "banana & oat": 5.50,
    "croissant": 3.00,
    "muffin ": 3.50,
    "bagel with cream cheese": 4.00,
    "scone with jam": 3.50,
    "chocolate brownie": 4.00,
    "grilled cheese sandwich": 5.50,
    "turkey club sandwich": 7.00,
    "chicken caesar salad": 8.50,
    "veggie wrap": 6.50
}

value = []


def take_order():

    order_total = 0
    item = input("\nEnter the name of item you want to order: ")
    item = item.lower()
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added.")
    else:
        print(f"Ordered item is not available yet!")

    print(f"Amount of {item} is {order_total}")
    return value.append(order_total)


# welcome
print("Welcome to our Cafe")
a = input("Enter 1 to see menu (0 to exit) :")
if a == "1":
    print("\n\tHot Beverages\nEspresso : $3.00\nAmericano : $3.50\nCappuccino : $4.00\nLatte : $4.50\nMocha : $5.00"
          "\nHot Chocolate : $4.00\nChai Latte : $4.00\nFlat White : $4.50\n\n\tCold Beverages\nIced Americano : $3.75"
          "\nIced Latte : $4.75\nIced Mocha : $5.25\nIced Tea : $3.00\nCold Brew : $4.00\nLemonade : $3.50"
          "\n\n\tSmoothies\nBerry Blast : $6.00\nTropical Mango : $6.00\nGreen Detox : $6.50\nBanana & Oat : $5.50"
          "\n\n\tPastries & Snacks\nCroissant : $3.00\nMuffin : $3.50\nBagel with Cream Cheese : $4.00"
          "\nScone with Jam : $3.50\nChocolate Brownie : $4.00\n\n\tSandwiches & Salads\n"
          "Grilled Cheese Sandwich : $5.50\nTurkey Club Sandwich : $7.00\nChicken Caesar Salad : $8.50"
          "\nVeggie Wrap : $6.50")
    take_order()
    while True:
        add = input("Would you like to add another item (yes/no) ?")
        if add.lower() == "no":
            break
        elif add.lower() == "yes":
            print(take_order())
        else:
            print("Invalid input!")

    amount = sum(value)
    print(f"Your total amount to pay is ${amount}")
    print("Hope you enjoy!")

elif a == "0":
    print("Hope you enjoy! Thanks for coming.")
else:
    print("Enter a valid number.")
