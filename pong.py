#normal ping pong game created using turtlebot
import turtle
import os
pongg = turtle.Screen()
pongg.title("Pong")
pongg.bgcolor("blue")
pongg.setup(width=800, height=600)
pongg.tracer(0)


# score

score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(100)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# score displaying


pen = turtle.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0   Player B: 0", align="center",
          font=("Courier", 24, "normal"))


# Keyboard bindings
pongg.listen()
pongg.onkeypress(paddle_a_up, "w")
pongg.onkeypress(paddle_a_down, "s")
pongg.onkeypress(paddle_b_up, "Up")
pongg.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    pongg.update()

    # Move the ball
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay pong.wav&")

    if ball.ycor() < (-290):
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay pong.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < (-390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(
            score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # ball and padle collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay pong.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay pong.wav&")
