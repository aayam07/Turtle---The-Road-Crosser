from turtle import Turtle

TURTLE_COLOR = "black"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color(TURTLE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(-170, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="right", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(220, 260)
        self.write("Game Over", align="center", font=FONT)
