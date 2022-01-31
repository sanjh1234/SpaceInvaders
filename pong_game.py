import turtle
import random


wn= turtle.Screen()
wn.title = ("pong game")
wn.setup(width=410,height=610)
wn.bgcolor("#5CACEE")
turtle.tracer(0)
turtle.hideturtle()
score_1=0
score_2=0


# 1st paddle
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.penup()
paddle1.goto(-190,0)
paddle1.shapesize(stretch_wid=5,stretch_len=0.5)


# 2nd paddle
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.penup()
paddle2.goto(190,0)
paddle2.shapesize(stretch_wid=5,stretch_len=0.5)

y_ch=20


# ball
ball = turtle.Turtle()
ball.color("white")
ball.shapesize(1)
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.goto(-5,0)
# dx=delta x
ball.dx=0.05
ball.dy=0.1


#writing score
pen = turtle.Turtle()
pen.penup()
pen.goto(0,0)
pen.hideturtle()



# moving paddle1
def paddle1_up():
	paddle1.sety(paddle1.ycor()+y_ch)
		
def paddle1_down():
	paddle1.sety(paddle1.ycor()-y_ch)


# moving paddle2
def paddle2_up():
	paddle2.sety(paddle2.ycor()+y_ch)
	
def paddle2_down():
	paddle2.sety(paddle2.ycor()-y_ch)
	

# keyboard binding
turtle.listen()
turtle.onkeypress(paddle1_up,"w")
turtle.onkeypress(paddle1_down,"s")
turtle.onkeypress(paddle2_up,"Up")
turtle.onkeypress(paddle2_down,"Down")



#main game loop
while True:
    turtle.update()
	
	#moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
	

	#border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1
        ball.sety(-290)
    if ball.xcor() > 190:	
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write(f"Player_1 = {score_1}    Player_2 = {score_2}", align="center", font=("courier",12,"bold"))

    if ball.xcor() < -190:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write(f"Player_1 = {score_1}    Player_2 = {score_2}", align="center", font=("courier",12,"bold"))
	
    
    #border checking paddlele
    if paddle1.ycor()> 250:
        paddle1.sety(250)

    if paddle1.ycor()< -250:
        paddle1.sety(-250)

    if paddle2.ycor()> 250:
        paddle2.sety(250)

    if paddle2.ycor()< -250:
        paddle2.sety(-250)


    #paddle and ball collisions
    if ball.xcor() > 175 and ball.xcor() < 200 and ball.ycor() < paddle2.ycor()+50 and ball.ycor() > paddle2.ycor()-50:
        ball.setx(175)
        ball.dx *= -1
				
    if ball.xcor() < -175 and ball.xcor() > -200 and ball.ycor() < paddle1.ycor()+50 and ball.ycor() > paddle1.ycor()-50:
        ball.setx(-175)
        ball.dx *= -1
	

turtle.done()