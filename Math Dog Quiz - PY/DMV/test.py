#!/usr/bin/env

from random import randint

encouragements = {
    "correct": [
        "Way to go!",
        "Awesome job!",
        "Great!",
        "Keep up the good work!",
        "Another one correct!",
        "You're on fire!",
        "Well done!"
    ],
    "incorrect": [
        "Better luck next time.  ",
        "Close, but not quite.  ",
        "Nope, but keep going.  ",
        "You'll get the next one.  ",
        "So close.  ",
        "Wrong, but don't give up.  "
    ]
}

def get_encouragement():
    correct_message = encouragements["correct"][randint(0, len(encouragements["correct"])-1)]
    print(correct_message)
