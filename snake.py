from turtle import Turtle
STARTING_POSITIONS = [-20,0,20]
class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    
    def create_snake(self):
        for position in range(0,3):
            segment = Turtle()
            segment.shape("square")
            segment.goto(x=STARTING_POSITIONS[position],y=0)
            segment.penup()
            self.turtles.append(segment)
            segment.color("green")

    def move_snake(self):
        for turtle in range(len(self.turtles)-1,0,-1): # looping backwards in the lists squares/segments created or added
                self.turtles[turtle].goto(self.turtles[turtle-1].pos()) # moving last square to position of second last square and so on 
                 
        self.turtles[0].forward(20)

    def forwards(self):
        self.turtles[0].setheading(90)

    def backwards(self):
            self.turtles[0].setheading(270)

    def left(self):
            self.turtles[0].setheading(180)

    def right(self):
            self.turtles[0].setheading(0)