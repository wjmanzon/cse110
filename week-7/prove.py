print("Welcome to the word guessing game!")
print()

guesses = 1
answer = "mosiah"
print("Your hint is _ _ _ _ _ _")
word = input("What is your guess? ").lower()

while word != answer :
    print("Your hint is _ _ _ _ _ _")
    word = input("What is your guess? ").lower()
    guesses += 1
print("Congratulations! You guessed it!")
print(f"It took you {guesses} guesses.")