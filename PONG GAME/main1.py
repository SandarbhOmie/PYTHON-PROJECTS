# PONG 
# Part 1: Getting Started

import turtle        # for graphics.
from playsound import playsound   # version 1.2.2

# creating windows
wn= turtle.Screen()
wn.title("Pong by Sandy") 
wn.bgcolor("black")
wn.setup(width = 800,height=600)
wn.tracer(0)     # speed up the game.

# SCORE
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)     #set the spped to maximum. to make game faster.
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)     #set the spped to maximum. to make game faster.
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)     #set the spped to maximum. to make game faster.
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)


# Pen
pen = turtle.Turtle()
pen.speed(0)         # animation spped
pen.color("white")
pen.penup() # to clear the line between two points
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : 0   Player B : 0",align = 'center',font=("Courier",24,"bold"))



# ball movement
# this means every time our ball moves it will move 0.1 pixels at a time
ball.dx = 0.1
ball.dy = -0.1


# Function
# here we will define moving of the paddles and balls.
def paddle_a_up():
    y=paddle_a.ycor()  # this is turtle mudule "ycor" means y cordinate.
    y=y+20  # adding 20 pixels to y cordibate
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()  # this is turtle mudule "ycor" means y cordinate.
    y=y-20  # adding 20 pixels to y cordibate
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()  # this is turtle mudule "ycor" means y cordinate.
    y=y+20  # adding 20 pixels to y cordibate
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()  # this is turtle mudule "ycor" means y cordinate.
    y=y-20  # adding 20 pixels to y cordibate
    paddle_b.sety(y)




# Keyboard binding
wn.listen()
    # for paddle A
wn.onkeypress(paddle_a_up,"w")   # here we are using keyboard keys for controlling.
wn.onkeypress(paddle_a_down,"s")

    # for paddle B
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# main game loop

while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1
        playsound("D:\PYTHON\projects\PONG GAME\mixkit-quick-jump-arcade-game-239.wav")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        playsound("D:\PYTHON\projects\PONG GAME\mixkit-quick-jump-arcade-game-239.wav")

    
    if ball.xcor()>390 :
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(score_a,score_b),align = 'center',font=("Courier",24,"bold"))


    if ball.xcor()<-390 :
        ball.goto(0,0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A : {}   Player B : {}".format(score_a,score_b),align = 'center',font=("Courier",24,"bold"))
    
    # Paddle and ball collisions
    if (ball.xcor() >340 and ball.xcor()<350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50)):
        ball.setx(340)
        ball.dx *=-1
        playsound("D:\PYTHON\projects\PONG GAME\mixkit-quick-jump-arcade-game-239.wav")

    if (ball.xcor() <-340 and ball.xcor()> -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50)):
        ball.setx(-340)
        ball.dx *=-1
        playsound("D:\PYTHON\projects\PONG GAME\mixkit-quick-jump-arcade-game-239.wav")

