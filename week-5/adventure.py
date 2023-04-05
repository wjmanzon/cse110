print("Welcome to the adventure!")
user = input("What's your name? ").capitalize()
print(f"Good luck, {user}!")


one = input("You are walking through a dark forest and find two items: \
    a MATCH and a FLASHLIGHT. Which one do you want to pick up? ").lower()

print(one)
if one == "match":

    two_match = input("You pick up the match and strike it, and for an instant, \
    the forest around you is illuminated. You see a large grizzly bear, \
    and then the match burns out. Do you want to FIGHT with the bear, RUN, or HIDE behind a tree? ").lower()

    print(two_match)

    if two_match == "run":
        three_run = input("You started running and the grizzly bear followed you. You feel nervous, afraid, and tired. \
        While running, you see a tree house. What do you do? CONTINUE running or CLIMB the treehouse? ").lower()

        print(three_run)
        if three_run == "continue":
            print("You're dead.")
        elif three_run == "climb":
            print("Good choice! You're safe!")
        else:
            print("Incorrect input")

    elif two_match == "fight":
        print("Oh no, you're dead man!")

    elif two_match == "hide":
        three_hide = input("You hid behind the tree and the grizzly bear didn't see you. However, you smelled a pepper and you're about to sneeze. \
        What do you do? SNEEZE or HOLD your sneeze? ").lower()

        print(three_hide)
        if three_hide == "sneeze":
            print("You're dead.")
        elif three_hide == "hold":
            print("Good choice! You're safe!")
        else:
            print("Incorrect input")
    else:
        print("Incorrect input")

elif one == "flashlight":
    two_flashlight = input("You pick up the flashlight and turn it on. \
    You see the pathway lit up in front of you, \
    but you thought you also heard something off to the side. \
    Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? ").lower()

    print(two_flashlight)

    if two_flashlight == "follow":

        three_follow = input("You followed the path in front of you and suddenly, \
        you see a large snake sleeping on the side. What do you do? WALK slowly on the path or TAKE a different route? ").lower()

        print(three_follow)
        if three_follow == "walk":
            print("You're dead.")
        elif three_follow == "take":
            print("Good choice! You're safe!")
        else:
            print("Incorrect input")

    elif two_flashlight == "look":
        three_look = input("You looked in the trees for the thing that made the noise and you realized it was a cute little talking dog. \
        It is wiggling its tail to you and it tells you to go back. What do you do? go BACK or continue to move FORWARD? ").lower()

        print(three_look)
        if three_look == "forward":
            print("You're dead.")
        elif three_look == "back":
            print("Good choice! You're safe!")
        else:
            print("Incorrect input")

    else:
        print("Incorrect input")

else:
    print("Wrong input. Try again!")