from turtle import Turtle, Screen

etchy = Turtle()
screen = Screen()

colors = ['black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple']
color = 0

def move_forward():
    """Move the turtle forward by 10 units.
    
    For: Pressing W
    """
    etchy.forward(10)
    
def move_backward():
    """Move the turtle backward by 10 units.

    For: Pressing S
    """
    etchy.backward(10)

def turn_clockwise():
    """Turn the turtle clockwise by 10 degrees.

    For: Pressing D
    """
    etchy.right(10)

def turn_counter_clockwise():
    """Turn the turtle counter-clockwise by 10 degrees.

    For: Pressing A
    """
    etchy.left(10)

def clear_canvas():
    """Clear the canvas and reset the turtle position.

    For: Pressing C
    """
    etchy.clear()
    etchy.penup()
    etchy.home()
    etchy.pendown()

def change_color_forward():
    """Changes the color of the turtle to the next color in the list.
    
    For: Pressing E
    """
    global color
    if color == len(colors) - 1:
        color = 0
    else:
        color += 1
    etchy.color(colors[color])

def change_color_backward():
    """Changes the color of the turtle to the previous color in the list.
    
    For: Pressing Q
    """
    global color
    if color == 0:
        color = len(colors) - 1
    else:
        color -= 1
    etchy.color(colors[color])
    
screen.listen()

# MApping out the functions to their keys.
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_clockwise, "d")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(clear_canvas, "c")
screen.onkey(change_color_forward, "e")
screen.onkey(change_color_backward, "q")

screen.exitonclick()