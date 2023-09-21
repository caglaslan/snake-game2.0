from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def score_count(self):
        self.clear()
        self.write(arg=f"Score = {self.score} High Score = {self.high_score}", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.hideturtle()
        self.home()
        self.color("white")
        self.write(arg='GAME OVER', align= ALIGNMENT, font= FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0

