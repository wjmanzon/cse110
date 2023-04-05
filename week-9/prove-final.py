items = []
prices = []
quantities = []

action = 0

# ask the user for action as long as he doesn't quit
while action != 5:
    print()
    print("-------------------------------------")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove last item")
    print("4. Compute total")
    print("5. Quit")
    print("")
    action = int(input("Please enter an action: "))
    if action == 1:
        # add the item in the items list and cart
        item = input("What item would you like to add? ").capitalize()
        items.append(item)

        # add the price in the price list and cart
        price = float(input(f"What is the price of the {item}? "))
        prices.append(price)

        # add the quantity in the price list and cart
        quantity = int(input(f"How many {item} do you wish to buy? "))
        quantities.append(quantity)

        # show message to user
        print()
        print("SUCCESS!")
        print(f"You added {quantity} {item} to the cart.")
        print()

    elif action == 2:
        print()
        print("YOUR CART")
        print("These are the items in your cart:")
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            quantity = quantities[i]

            print(f"{[i+1]} {item} @ ${price: .2f} * {quantity} pc/s")


    elif action == 3:
        items.pop()
        prices.pop()
        quantities.pop()
        print()
        print("SUCCESS!")
        print("You removed the last item.")
        print("These are the items in your cart:")
        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            quantity = quantities[i]

            print(f"{i+1} {item} @ ${price: .2f} * {quantity} pc/s")


    elif action == 4:
        sum = 0
        price_per_item = 0

        for i in range(len(items)):
            item = items[i]
            price = prices[i]
            quantity = quantities[i]

            price_per_item = price * quantity
            sum += price_per_item
        print()
        print("TOTAL")
        print(f"The total price of all items in your cart is ${sum: .2f}")

    elif action == 5:
        print("")
        print("EXIT")
        print("Thank you. Goodbye!")


    else:
        print("Please choose a valid option.")


