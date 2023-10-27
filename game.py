# Import required library
import asyncio
import websockets
import turtle
import json
from pynput.keyboard import Listener
from  client import client
from graphics import gameWindow

#starting client and game
client = client("pedro", 8765)
game = gameWindow("pedro", "jobs")
#init scores
left_player = 0
right_player = 0

#message
message = {}
message['player_name'] = "pedro"
# Functions to move paddle vertically
def paddleaup():
	y = game.left_pad.ycor()
	y += 20
	game.left_pad.sety(y)


def paddleadown():
	y = game.left_pad.ycor()
	y -= 20
	game.left_pad.sety(y)


def paddlebup():
	y = game.right_pad.ycor()
	y += 20
	game.right_pad.sety(y)


def paddlebdown():
	y = game.right_pad.ycor()
	y -= 20
	game.right_pad.sety(y)

#keyListeners

def onPress(key):
    if key == "Key.up":
        message['move'] = 1
        client.sendMessage(json.dumps(message))
    elif key == "Key.down":
        message['move'] = 0
        client.sendMessage(json.dumps(message))

def onRelease(key):
    pass

with Listener(on_press= onPress, on_release= onRelease) as listener:
    listener.join()

while True:
	game.screen.update()

	game.hit_ball.setx(game.hit_ball.xcor()+game.hit_ball.dx)
	game.hit_ball.sety(game.hit_ball.ycor()+game.hit_ball.dy)

	# Checking borders
	if game.hit_ball.ycor() > 280:
		game.hit_ball.sety(280)
		game.hit_ball.dy *= -1

	if game.hit_ball.ycor() < -280:
		game.hit_ball.sety(-280)
		game.hit_ball.dy *= -1

	if game.hit_ball.xcor() > 500:
		game.hit_ball.goto(0, 0)
		game.hit_ball.dy *= -1
		left_player += 1
		game.showScore(left_player, right_player)

	if game.hit_ball.xcor() < -500:
		game.hit_ball.goto(0, 0)
		game.hit_ball.dy *= -1
		right_player += 1
		game.showScore(left_player, right_player)

	# Paddle ball collision
	if (game.hit_ball.xcor() > (game.right_pad.xcor() - 13) and game.hit_ball.xcor() < (game.right_pad.xcor() + 13)) and (game.hit_ball.ycor() < game.right_pad.ycor()+40 and game.hit_ball.ycor() > game.right_pad.ycor()-40):
		game.hit_ball.setx(game.right_pad.xcor()-13)
		game.hit_ball.dx *= -1
		
	if (game.hit_ball.xcor() > (game.left_pad.xcor() - 13) and game.hit_ball.xcor() < (game.left_pad.xcor() + 13)) and (game.hit_ball.ycor()<game.left_pad.ycor()+40 and game.hit_ball.ycor()>game.left_pad.ycor()-40):
		game.hit_ball.setx(game.left_pad.xcor()+13)
		game.hit_ball.dx *= -1
