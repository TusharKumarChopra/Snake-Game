from turtle import Turtle 
ALLIGNMENT = "center"
FONT = ('Courier', 14, 'bold    ')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align = ALLIGNMENT,  font = FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
      
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"Game Over", align = ALLIGNMENT,  font = FONT)


    def update_score(self):
        self.score += 1
        self.update_scoreboard()
        