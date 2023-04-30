import turtle


avatar = turtle.Turtle()
def onUpKeyPressed():
    avatar.direction = "up"
def onDownKeyPressed():
    avatar.direction = "down"
def onLeftKeyPressed():
    avatar.direction = "left"
def onRightKeyPressed():
    avatar.direction = "right"

# Set Window Bindingsz
screen = turtle.Screen()
screen.listen()
screen.onkeypress(onUpKeyPressed, "Up")
screen.onkeypress(onDownKeyPressed, "Down")
screen.onkeypress(onLeftKeyPressed, "Left")
screen.onkeypress(onRightKeyPressed, "Right")


nums = [1, 2, 3, 4, 5]

for num in nums:
    print(f"number {num} is on")
    print(f"number {num} is on")
    print(f"number {num} is on")
    print(f"number {num} is on")
    print(f"number {num} is on")

turtle.Screen().bgcolor("black")
freddy = turtle.Turtle()
freddy.penup()
freddy.shape("circle")
freddy.color("green")
freddy.back(100)
freddy.penup()

avatar.penup()
avatar.color("white")
avatar.shape("square")


bonny = turtle.Turtle()
bonny.penup()
bonny.color("blue")
bonny.shape("circle")
bonny.forward(200)
bonny.penup()


chika = turtle.Turtle()
chika.penup()
chika.color("yellow")
chika.shape("circle")
chika.left(90)
chika.forward(200)



avatar.direction = "right"

def move_avatar_one_frame():
    if avatar.direction == "up":
        y = avatar.ycor()
        y += 0.7
        avatar.sety(y)
    elif avatar.direction == "down":
        y = avatar.ycor()
        y -= 0.7
        avatar.sety(y)
    elif avatar.direction == "left":
        x = avatar.xcor()
        x -= 0.7
        avatar.setx(x)
    elif avatar.direction == "right":
        x = avatar.xcor()
        x += 0.7
        avatar.setx(x)

def wall_hit():
    if avatar.xcor() > 280:
        avatar.direction = "left"
    elif avatar.xcor() < -280:
        avatar.direction = "right"
    elif avatar.ycor() > 280:
        avatar.direction = "down"
    elif avatar.ycor() < -280:
        avatar.direction = "up"

    screen.setup(600, 600)


while True:
    move_avatar_one_frame()
    wall_hit()
