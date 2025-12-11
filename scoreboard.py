from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0,315) 
        self.write(arg=f"Score:{self.score} ",move=False,align = "center",font=("Monocraft", 22, "normal"))

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score:{self.score} ",move=False,align = "center",font=("Monocraft", 22, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER!",move=False,align = "center",font=("Monocraft", 30, "normal"))