import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle - The Road Crosser")
screen.tracer(0)

cars = []
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(key="Up", fun=player.go_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # the code inside the while loop is going to be refreshed every 0.1s
    screen.update()

    car_manager.generate_car()  # generates a new car every 0.1 seconds
    car_manager.move_cars()

    # Detect Collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Successful crossing
    # if player.ycor() > 280:
    #     player.go_to_start()
    #     scoreboard.level_up()
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level_up()
        car_manager.level_up()

screen.exitonclick()
