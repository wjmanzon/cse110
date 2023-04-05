import random

# header
print("Wordle")
print("Can you guess this five-letter word in five attempts?")

# declare some variables
number_of_guesses = 0
hint = ""
index = 0

# store the answers in a list
list = ["pizza", "pilot", "vague", "grass", "third", "sleep"]
answer = random.choice(list)

# show the user initial hint
print("Your hint is: " + " _ " * len(answer))

# get guess from user
guess = input("What's your guess? ")
number_of_guesses += 1

# continue looping until 
# the user guesses the right 
# word or consumes all five attempts
while guess.lower() != answer and number_of_guesses < 6:
    print("Incorrect. Please try again!")  
    
    # compare user's guess to correct answer
    for letter in guess:
        
        # use error handling
        try:
            if letter == answer[index]:
                hint +=  " " + letter.upper() + " "
            
            elif letter in answer:
                hint +=  " " + letter.lower() + " "

            else:
                hint += " _ " 

        except:

            print("Oops... Please enter five letters only.")
            hint = " _ " * len(answer)
            break

        index += 1

    # print the hint and ask for input
    print(f"Your hint is: {hint}")        
    guess = input("What's your guess? ")
    
    # redeclare the variables
    hint = ""
    index = 0
    number_of_guesses += 1

if number_of_guesses > 5:
    print("You have consumed your five attempts. Please restart!")

else:
    print("That's correct! You guessed it right!")
    print(f"It took you {number_of_guesses} guesses!")