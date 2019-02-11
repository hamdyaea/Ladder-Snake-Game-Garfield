# Developer : Hamdy Abou El Anein

from easygui import *
import random
import sys


dice = 0
picture = " "


def win():
    image = "./pictures/garfieldwin.jpg"
    msg = "You win the game"
    choices = ["Ok"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Ok":
        sys.exit(0)
    else:
        sys.exit(0)

def game():
    global case, picture
    dice = random.randint(1,6)
    case = case + dice

    if case == 2:
        case = 37
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif case == 11:
        case = 33
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif case == 25:
        case = 7
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif case == 43:
        case = 21
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif case == 55:
        case = 27
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif case == 57:
        case = 79
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif case == 65:
        case = 87
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif case == 68:
        case = 31
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif case == 71:
        case = 93
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif case == 98:
        case = 76
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)


    elif case == 100:
        win()

    else:
        if case > 100:
            case = case - dice - (dice-1)
        picture = str("./pictures/") + str(case) + str(".jpg")
        image = picture
        msg = "The result of the dice roll is " + str(dice) + str("\n\nyou are on the place ") + str(case)
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)


def begin():
    global case
    case = 1
    image = "./pictures/1.jpg"
    msg = "Start the game"
    choices = ["Start"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Start":
        game()
    else:
        sys.exit(0)

begin()
