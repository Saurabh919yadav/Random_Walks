import numpy as np
from turtle import *
import random


def walking(colo):
    # Setting up the turtle
    setposition(0,0)
    shape("turtle")
    color(colo)
    screensize(500, 500)
    speed(30)
    # Initiate the steps
    steps = 0

    while True:
        choice = np.random.randint(5, size = 1)
        if choice == 1:
            fd(10)
            steps += 1
        elif choice == 2:
            rt(90)
            fd(10)
            steps += 1
        elif choice == 3:
            left(90)
            fd(10)
            steps += 1
        else:
            backward(10)
            steps += 1

    done()

if __name__ == "__main__":
    walking("mediumturquoise")
