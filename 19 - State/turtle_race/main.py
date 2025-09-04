from turtle import Turtle, Screen
import random

class TurtleRacer:
    def __init__(self, color, start_position):
        self.turtle = Turtle(shape='turtle')
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto(x=-380, y=start_position)
        self.turtle.pendown()
        self.color = color

    def move_forward(self):
        """Move the turtle forward by a random distance."""
        distance = random.randint(1, 10)
        self.turtle.forward(distance)

# Set up the screen
screen = Screen()
screen.setup(height=500, width=800)
screen.title("Turtle Race")

# Initialize turtles
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
start_positions = [-100, -60, -20, 20, 60, 100]
turtles = []

for index in range(len(colors)):
    new_turtle = TurtleRacer(colors[index], start_positions[index])
    turtles.append(new_turtle)

# Main Race program
user_bet = screen.textinput(title='Guess?', prompt='Which turtle will win the race? Enter a color! (red, orange, yellow, green, blue, purple)').lower()

if user_bet:
    race_on =True
    
while race_on:
    for turtle in turtles:
        turtle.move_forward()
        
        if turtle.turtle.xcor() >= 380:
            race_on = False
            winning_color = turtle.color
            if winning_color == user_bet:
                screen.textinput(title='You Win!', prompt=f'Congratulations! The {winning_color} turtle is the winner! Type anything to exit.')
            else:
                screen.textinput(title='You Lose!', prompt=f'Sorry, the {winning_color} turtle is the winner. Better luck next time! Type anything to exit.')
                
screen.exitonclick()