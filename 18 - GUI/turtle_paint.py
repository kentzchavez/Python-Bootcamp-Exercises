import turtle
import colorgram as cg
import random

# Initialize objects
tim = turtle.Turtle()
screen = turtle.Screen()

# Customize timmy the turtle
tim.shape('turtle')

def draw_polygon(sides):
    """Draw a polygon based from x number of sides"""
    rotation = 360/sides
    for n in range(sides):
        tim.color(get_color()) #Get a randOM color
        tim.left(rotation)
        tim.forward(40)

def get_color():
    """Generate random hex color code"""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def random_walk(change_colors=False):
    """Generate a random walk"""
    dir = [0, 90, 180, 270]
    steps = random.randint(10,100)
    print(f'[!] Random walking for {steps} steps...')
    for x in range(steps):
        tim.seth(random.choice(dir))
        tim.forward(40) 
        if change_colors:
            tim.color(get_color())

def draw_spirograph(num_circles, change_colors=False):
    """Draws a spirograph depending on the number of circles."""
    tilt = 360/num_circles
    tim.speed(0.01)
    for x in range(num_circles):
        if change_colors:
            tim.color(get_color())
        tim.circle(100)
        tim.left(tilt)
        
def extract_rgb_from_img(img_relative_path, num):
    """Extracts certain number of RGB tuples from image"""
    colors = []
    for color in cg.extract(img_relative_path, num):
        # Sample path '18 - GUI/extract_color.png'
        colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    return colors

def hirst_painting(color_list, rows, circle_per_rows):
    """Draws a hirst painting based from a list of colors, number of rows and circle per rows"""
    # Initialize Tim
    tim.hideturtle()
    screen.colormode(255)
    tim.penup()
    tim.setpos(-250, -250)
    
    movement_x = 500/circle_per_rows
    movement_y = 500/rows
    for row in range(1,rows+1):
        for dot in range(circle_per_rows):
            tim.dot(20, random.choice(color_list))
            tim.forward(movement_x)
        tim.setpos(-250, (-250 + movement_y*row) )
    
    

colors = extract_rgb_from_img('18 - GUI/extract_color.png', 10)
hirst_painting(colors, 10, 10)
 
screen.exitonclick()