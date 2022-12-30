from turtle import Screen
from snake import Snake
import time
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        scoreboard.increase_score()
        snake.extend()
        food.refresh()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280 or \
            snake.segments[0].ycor() > 280:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
