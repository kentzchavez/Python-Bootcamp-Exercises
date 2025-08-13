import turtle
import random
# Initialize objects
tim = turtle.Turtle()
screen = turtle.Screen()

# Customize timmy the turtle
tim.shape('turtle')
tim.color('aquamarine4')

def draw_polygon(sides):
    """Draw a polygon based from x number of sides"""
    rotation = 360/sides
    for n in range(sides):
        tim.color(get_color()) #Get a randOM color
        tim.left(rotation)
        tim.forward(40)

def get_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def random_walk(change_colors=False):
    dir = [0, 90, 180, 270]
    steps = random.randint(10,100)
    print(f'[!] Random walking for {steps} steps...')
    for x in range(steps):
        tim.seth(random.choice(dir))
        tim.forward(40) 
        if change_colors:
            tim.color(get_color())

tim.width(10)
random_walk(True)

screen.exitonclick()