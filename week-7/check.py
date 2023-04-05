# Ask the user for a number
number = int(input("Please type a positive number: "))

# If the number if negative, loop as long as it's negative.
while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))

print(f"The number is: {number}")

answer = ""

while answer != "yes":
    # This could be written as: 'while answer == "no":'
    # The difference would be how it treats other words, besides yes and no
    answer = input("May I have a piece of candy? ")

print ("Thank you.")
