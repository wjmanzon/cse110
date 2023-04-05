"""
1. Ask the user for the price of a child and 
an adult meal and store these values properly 
into variables as floating point numbers.

2. Ask the user for the number of adults and 
children and store these values properly 
into variables as integers.

3. Ask the user for the sales tax rate and 
store the value properly as a floating point number.
"""
child_meal_price = float(input("What's the price of the child's meal? "))
child_drink_price = float(input("What's the price of the child's drink? "))
adult_meal_price = float(input("What's the price of an adult's meal? "))
adult_drink_price = float(input("What's the price of an adult's drink? "))
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

"""
4. Compute and display the subtotal 
(don't worry about rounding to two 
decimals at this point).
"""
subtotal = (number_children * (child_meal_price + child_drink_price)) + (number_adults * (adult_meal_price + adult_drink_price))
print(f"Your subtotal is ${subtotal:.2f}")

"""
5. Compute and display the sales tax.
6. Compute and display the total.
"""
sales_tax = subtotal * sales_tax_rate / 100
total_price = subtotal + sales_tax
print(f"The sales tax is ${sales_tax:.2f}.")
print(f"The total price is ${total_price:.2f}")

"""
7. Ask the user for the payment amount and 
store the value properly as a floating point number.
8. Compute and display the change.
9. Include a dollar sign ($) before each displayed value.
10. Display each value to two decimals.
11. Double check that the calculations are correct.
12. Show creativity and exceed the core requirements by adding additional features. 
--> added drinks
13. Use good style in your program, including variable names and whitespace.
"""
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total_price
print(f"Your change is ${change:.2f}")