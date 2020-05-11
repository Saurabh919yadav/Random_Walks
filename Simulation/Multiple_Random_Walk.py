import numpy as np
from turtle import *
import random

turtles = 5
delay(0)
screensize(500,500)


class Walker():
    def __init__(self, colo, pos):
        self.pos = pos
        self.tur = Turtle()
        self.tur.shape("turtle")
        self.tur.setpos(pos)
        self.tur.speed(30)
        self.tur.color(colo)
        self.tur.penup()
        self.tur.setheading(90)

    def walking(self):
        choice = np.random.randint(4, size=1)[0]
        actionofchoice = [(self.pos[0]+5, self.pos[1]), (self.pos[0], self.pos[1]+5), (self.pos[0]-5, self.pos[1]), (self.pos[0], self.pos[1]-5)]
        headsup = [90, 180, 270, 360]
        self.pos = actionofchoice[choice]
        self.tur.right(headsup[choice])
        self.tur.pendown()
        self.tur.goto(self.pos)


def starttowalk():
    allwalker = []
    colors = ['red', 'yellow', 'mediumturquoise', 'blue', 'orange']
    for x in range(turtles):
        allwalker.append(Walker(colors[x], (0,0)))
        allwalker[x].tur.showturtle()

    while True:
        for x in allwalker:
            x.walking()

if __name__ == "__main__":
    starttowalk()
