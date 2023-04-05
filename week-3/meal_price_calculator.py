child_meal_price = float(input("What's the price of the child's meal? "))
adult_meal_price = float(input("What's the price of an adult's meal? "))
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

#compute the subtotal
subtotal = (number_children * child_meal_price) + (number_adults * adult_meal_price)
print(f"Your subtotal is ${subtotal:.2f}")

#compute the sales tax
sales_tax = subtotal * sales_tax_rate / 100
total_price = subtotal + sales_tax
print(f"The sales tax is ${sales_tax:.2f}.")
print(f"The total price is ${total_price:.2f}")

#ask for payment amount
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total_price
print(f"Your change is ${change:.2f}")