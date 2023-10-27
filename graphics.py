import turtle

primaryColor = "white"
secundaryColor = "Black"

class gameWindow():
    def __init__(self,left_name, right_name):
        self.left_name = left_name
        self.right_name = right_name
        self.screen = self.createScreen()
        self.left_pad, self.right_pad = self.createPlayers()
        self.hit_ball = self.createBall()
        self.showScore(0, 0)
        
    def createScreen(self):
        sc = turtle.Screen()
        sc.title("Pong game")
        sc.bgcolor(primaryColor)
        sc.setup(width=1000, height=600)
        return sc
    
    def createPlayers(self):
        left_pad = turtle.Turtle()
        left_pad.speed(0)
        left_pad.shape("square")
        left_pad.color(secundaryColor)
        left_pad.shapesize(stretch_wid=6, stretch_len=2)
        left_pad.penup()
        left_pad.goto(-400, 0)
        
        right_pad = turtle.Turtle()
        right_pad.speed(0)
        right_pad.shape("square")
        right_pad.color(secundaryColor)
        right_pad.shapesize(stretch_wid=6, stretch_len=2)
        right_pad.penup()
        right_pad.goto(400, 0)
        
        return left_pad, right_pad

    def createBall(self):
        hit_ball = turtle.Turtle()
        hit_ball.speed(40)
        hit_ball.shape("circle")
        hit_ball.color("red")
        hit_ball.penup()
        hit_ball.goto(0, 0)
        hit_ball.dx = 5
        hit_ball.dy = -5
        return hit_ball
    
    def showScore(self, left_player = 0, right_player = 0):
        sketch = turtle.Turtle()
        sketch.clear()
        sketch.speed(0)
        sketch.color("blue")
        sketch.penup()
        sketch.hideturtle()
        sketch.goto(0, 260)
        sketch.write(f"{self.left_name} : {left_player} {self.right_name}:{right_player}", align="center", font=("Courier", 24, "normal"))
        return sketch