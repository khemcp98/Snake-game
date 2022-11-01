from turtle import Turtle

FONT = ('Arial', 15, 'normal')
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0

        # Reading the data from data.txt
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def display_score(self):
        self.clear()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.write(f"Score : {self.score} | Highscore : {self.high_score}", align=ALIGN, move=False, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

            # Writing the new score in data.txt
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.display_score()

    def score_refresh(self):
        self.score += 1
        self.display_score()
