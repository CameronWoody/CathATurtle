# a121_catch_a_turtle.py
#-----import statements-----
import turtle
import random


#-----game configuration----
turtle_color = ["red","blue","pink","yellow","black","purple"]
turtle_size = 2
turtle_shape = "turtle"
#new_xpos = random.randint(-200,200)
#new_ypos = random.randint(-125,125)
def change_position():
  new_xpos = random.randint(-200,200)
  new_ypos = random.randint(-125,125)
  trtl.goto(new_xpos,new_ypos)
  trtl.speed(100)
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000 #1000 represents 1 second
timer_up = False


#-----initialize turtle-----
trtl = turtle.Turtle()
trtl.fillcolor(random.choice(turtle_color))
trtl.shapesize(turtle_size)
trtl.shape(turtle_shape)
trtl.penup()

score_writer = turtle.Turtle()
score_writer.penup()
score_writer.goto(0,250)
score_writer.hideturtle()

time_writer = turtle.Turtle()
time_writer.penup()
time_writer.goto(-200, 250)
time_writer.hideturtle()

#-----game functions--------
def turtle_clicked(x,y):
  score_writer.clear()
  trtl.fillcolor(random.choice(turtle_color))
  if timer_up:     #when the timer is up, hide the turtle.
    trtl.hideturtle()

  else: # if the timer is NOT up. Kepp going.
    update_score()
    score_writer.write(score, font=font_setup)
    change_position()

def update_score():
  global score
  score += 1
  print(score)

def countdown():
  global timer, timer_up
  time_writer.clear()
  if timer <= 0:
    time_writer.write("Time's Up", font=font_setup)
    timer_up = True
    trtl.hideturtle()

  else:
    time_writer.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    new_xpos = random.randint(-200,200)
    new_ypos = random.randint(-125,125)
    trtl.goto(new_xpos,new_ypos)
    time_writer.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
trtl.onclick(turtle_clicked)


wn = turtle.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()
