import random

def processGuess(theAnswer, theGuess):
    position = 0
    clue =""
    for letter in theGuess:
        if letter == theAnswer[position]:
            clue += "G"
        elif letter in theAnswer:
            clue += "Y"
        else:
            clue += "-"
        position += 1
    print(clue)
    return clue == "GGGGG" # TRUE if correct, FALSE if not

# store words in a list
word_list = []
word_file = open("words.txt")

for word in word_file:
    word_list.append(word.strip())

# pick a word
answer = random.choice(word_list)

number_of_guesses = 0
guessed_correctly = False

while number_of_guesses < 6 and not guessed_correctly:
    # get guess from user
    guess = input("Input a 5-letter word and press enter: ")
    print(f"Your guess is {guess}")
    number_of_guesses += 1

    # process guess
    guessed_correctly = processGuess(answer, guess)

# display end of game message
if guessed_correctly:
    print("Congrats! You guessed it right.")
    print(f"It took you {number_of_guesses} guesses")
else:
    print("You have used up your guesses and the correct word is:")
    print(answer)