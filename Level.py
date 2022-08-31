from turtle import Turtle
import time
import random
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score=0
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 260)
        self.write(arg=f"Level={self.score}", move=True, align='left', font=('Arial', 8, 'normal'))

    def score_growing(self):
        self.score=self.score+1
        self.update()




class Barriers(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.penup()
        self.shapesize(1, 2, 1)
        self.goto(380,0)
        self.backward(30)
        self.sleep=1
        self.step_factor=0.1


    def position(self):
        random_y = random.randint(-200, 260)
        self.goto(380, random_y)
    def move(self):
       factor=1+self.step_factor
       step=random.randint(10,round(20*factor))*self.step_factor
       self.backward(step)
    def speed_increase(self, speed_counter):
        self.step_factor=speed_counter

