import time
from turtle import Screen, Turtle
from Level import *
import random
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Game")
timy=Turtle()
timy.shape("turtle")
screen.tracer(0)
timy.penup()
timy.goto(0,-280)
timy.left(90)
color_list=["yellow","green","red","purple","orange","black","gray","blue"]
screen.listen()
def up():
 timy.forward(20)
def down():
    timy.backward(20)
def left():
 timy.left(90)
def right():
    timy.right(90)
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(right,"Right")
screen.onkey(left,"Left")
scoreboard=Scoreboard()
barriers_list=[]

def barrier_generation():
      barriers= Barriers()
      color_ra=random.randint(0,7)
      barriers.color(color_list[color_ra])
      barriers.position()
      return barriers
def collision():
    for b in range(0,len(barriers_list)):
      if timy.distance(barriers_list[b])<16:
          return 10
def start():
      for i in range(3):
         barriers_list.append(barrier_generation())

game_is_on=True
counter=-1
speed_counter=0.1
start()
while game_is_on:
    screen.update()
    r=random.randint(0,80)
    if r==1:
      barriers_list.append(barrier_generation())
    counter=counter+1
    barriers_list[counter].move()
    barriers_list[counter].speed_increase(speed_counter)
    for c1 in range(len(barriers_list)-1):
        if barriers_list[c1].xcor()<-400:
            barriers_list[c1].hideturtle()
            barriers_list.remove(barriers_list[c1])


    if counter==(len(barriers_list)-1):
        counter=-1
    coll=collision()
    if coll==10:
        print("game_over")
        break
    position_x=timy.xcor()
    position_y=timy.ycor()
    if position_y>=298:

        timy.goto(0,-280)
        scoreboard.score_growing()
        barrier_size=len(barriers_list)

        for i in range(barrier_size):

             barriers_list[i].hideturtle()

        barriers_list = []
        counter = -1
        speed_counter = speed_counter + 0.03
        start()







screen.exitonclick()