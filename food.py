from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)

    def change_color(self):
        color = ['#4E8CA1', '#F9C1E7', '#933D05', '#595697', '#417D22', '#7D8377',
                 '#624F7B', '#C25D39', '#A24AFD', '#2AED9E']
        self.color(random.choice(color))
