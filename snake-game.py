#!/usr/bin/env python3
#
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com
#
#

from easygui import *
import random
import sys


class Garfield:
    def __init__(self):
        self.dice
        self.picture
        self.case


Garfield.dice = 0
Garfield.picture = " "


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
    Garfield.dice = random.randint(1, 6)
    Garfield.case = Garfield.case + Garfield.dice

    if Garfield.case == 2:
        Garfield.case = 37
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 11:
        Garfield.case = 33
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 25:
        Garfield.case = 7
        Garfield.picture = str("./pictures/") + str(garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 43:
        Garfield.case = 21
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 55:
        Garfield.case = 27
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 57:
        Garfield.case = 79
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 65:
        Garfield.case = 87
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 68:
        Garfield.case = 31
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 71:
        Garfield.case = 93
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 98:
        Garfield.case = 76
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)

    elif Garfield.case == 100:
        win()

    else:
        if Garfield.case > 100:
            Garfield.case = Garfield.case - Garfield.dice - (Garfield.dice - 1)
        Garfield.picture = str("./pictures/") + str(Garfield.case) + str(".jpg")
        image = Garfield.picture
        msg = (
            "The result of the dice roll is "
            + str(Garfield.dice)
            + str("\n\nyou are on the place ")
            + str(Garfield.case)
        )
        choices = ["Continue"]
        reply = buttonbox(msg, image=image, choices=choices)
        if reply == "Continue":
            game()
        else:
            sys.exit(0)


def begin():
    Garfield.case = 1
    image = "./pictures/1.jpg"
    msg = "Start the game"
    choices = ["Start"]
    reply = buttonbox(msg, image=image, choices=choices)
    if reply == "Start":
        game()
    else:
        sys.exit(0)


begin()
