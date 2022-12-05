import turtle
import socket

# here we made a socket object with the parameters passed to it.
# socket.AF_INET refers to the ip4 address and the socket.SOCK_STREAM refers to the connection oriented TCP protocol.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# we are declaring the port we need to connect.
# port = 8888
# here we bind the port.
s.bind(('0.0.0.0', 8888))
# this is the listening mode of the server to accept the incoming client
s.listen(3)
# describing the connection with the client.
clientSocket, address = s.accept()
# we are closing the connection here

# We are creating here the screen with a green background color, size, and screen title name.
sc = turtle.Screen()
sc.title("Two players Pong game")
sc.bgcolor("green")
sc.setup(width=800, height=400)

# Border to bounce off of

Border = turtle.Turtle()
Border.shape("square")
Border.color("black")
Border.shapesize(stretch_wid=25, stretch_len=52)
Border.penup()
Border.goto(0, 0)

# we are defining the left paddle shape, color, and shape size.
left_paddle = turtle.Turtle()
left_paddle.speed(1)
left_paddle.shape("square")
left_paddle.color("yellow")
left_paddle.shapesize(stretch_wid=12, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-400, 0)

# This is defining the right paddle shape, color, and shape size.
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("yellow")
right_paddle.shapesize(stretch_wid=12, stretch_len=2)
right_paddle.penup()
right_paddle.goto(400, 0)

# This is showing the ball shape and color.
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# here we initialize the score for both players.
Player_A = 0
Player_B = 0

# Outputting the score with blue color
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Player_A : 0    Player_B: 0",
             align="center", font=("Courier", 24, "normal"))


# This is the functions to move the paddle vertically or up and down.
def paddleaup():
    y = left_paddle.ycor()
    if y >= 120:
        y = y
    else:
        y += 20
    left_paddle.sety(y)


def paddleadown():
    y = left_paddle.ycor()
    if y <= -120:
        y = y
    else:
        y -= 20
    left_paddle.sety(y)


def paddlebup():
    y = right_paddle.ycor()
    if y >= 120:
        y = y
    else:
        y += 20
    right_paddle.sety(y)


def paddlebdown():
    y = right_paddle.ycor()
    if y <= -120:
        y = y
    else:
        y -= 20
    right_paddle.sety(y)


sc.listen()
sc.onkeypress(paddleaup, "u")
sc.onkeypress(paddleadown, "d")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

while True:
    sc.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)
    # Bounce the ball off the top of the screen
    if hit_ball.ycor() > 240:
        hit_ball.sety(240)
        hit_ball.dy *= -1
    # Bounce the ball off the bottom of the screen
    if hit_ball.ycor() < -240:
        hit_ball.sety(-240)
        hit_ball.dy *= -1
    # Detect if ball goes too far to the right, and increase score if so
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        Player_A += 1
        sketch.clear()
        sketch.write("Player_A : {}    Player_B: {}".format(
            Player_A, Player_B), align="center",
            font=("Courier", 24, "normal"))
    # Detect if ball goes too far to the left, and increase score if so
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        Player_B += 1
        sketch.clear()
        sketch.write("Player_A : {}    Player_B: {}".format(
            Player_A, Player_B), align="center",
            font=("Courier", 24, "normal")

        )
    # If the ball is going to hit the right paddle, reverse its direction upon impact
    if hit_ball.xcor() > 380 and right_paddle.distance(hit_ball.xcor(), hit_ball.ycor()) < 100:
        hit_ball.setx(380)
        hit_ball.dx *= -1
    # If the ball is going to hit the left paddle, reverse its direction upon impact
    if hit_ball.xcor() < -380 and left_paddle.distance(hit_ball.xcor(), hit_ball.ycor()) < 100:
        hit_ball.setx(-380)
        hit_ball.dx *= -1
