from turtle import Turtle
import random

COLORS = ["red", "orange", "pink", "green", "blue", "purple", "cyan", "darkblue", "darkgreen"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_choince = random.randint(1, 6)

        if random_choince == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            self.y_cor = random.randint(-250, 250)
            new_car.goto((300, self.y_cor))
            self.all_cars.append(new_car)


    def drive(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    def speedup(self):
        self.car_speed += MOVE_INCREMENT
        
    
