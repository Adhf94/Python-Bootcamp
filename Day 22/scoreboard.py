from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 220)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f" {self.l_score}  :  {self.r_score} ", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def l_increase_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_increase_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()


class Midline(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.pencolor("white")
        self.penup()
        self.goto(400,0)

    def write_line(self):
        for _ in range(50):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)