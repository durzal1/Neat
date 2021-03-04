import neat
from neat.population import Population
import pygame
import time
import random
import os
import math
import pickle
from snake2 import *
import gzip
#variables

time_grew = time.time()
height = 100
width = 100
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255,255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)
gen = 0
second = False
pygame.init()
down_ = 1
up_ = 1
right_ = 1
left_ = 1
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
class Snake:
    direction1 = 0
    def __init__(self, x, y):
        #initializes the snake
        self.snake_head = [[x, y]]
        self.snake_parts = []
        self.size = 1
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = GREEN
        self.draw()
        self.turn = 1
        self.moves = 200
        self.direction = 0 # 0 = none | 1 = up | 2 = right | 3= down | 4 = left


    def draw(self):
        # draws the rectangle to represent snake
        if second == True:
            pygame.draw.rect(win, BLACK, (0, 0, 1000, 1000))
            for apple in apples:
                apple.draw()
            pygame.draw.rect(win, self.color, (self.x, self.y, width, height))
            if self.direction1 != 0:
                for i in range(len(snake.snake_parts)):
                    x = snake.snake_parts[i][0]
                    y = snake.snake_parts[i][1]
                    pygame.draw.rect(win, self.color, (x, y, width, height))




            # todo draw blue circles for safe places and red for dangerous  and put a bunch of sleeps
            # todo then analyze board to see if the inputs are correct


    def move(self):
        #checks to see what direction the snake is moving
        # variables like up and down are set in the events section of the program;
        if up:
            #adds first part of snake
            self.snake_parts.insert(0,[self.x, self.y])

            self.direction = 1
            self.turn += 1
            #resets the screen so it looks like the square is moving
            pygame.draw.rect(win, BLACK, (self.x, self.y , width, height))
            try:
                #removes the old snake head from list
                self.snake_head.remove([self.x, self.y ])
            except Exception:
                pass
            self.y -= height
            self.snake_head.append([self.x, self.y])
            #deletes last square of snake
            self.snake_parts.pop(-1)
        elif down:
            self.snake_parts.insert(0,[self.x, self.y])

            self.direction = 3
            self.turn += 1
            # resets the screen so it looks like the square is moving
            pygame.draw.rect(win, BLACK, (self.x, self.y, width, height))
            try:
                # removes the old moves from list
                self.snake_head.remove([self.x, self.y])
            except Exception:
                pass
            self.y += height
            self.snake_head.append([self.x, self.y])
            self.snake_parts.pop(-1)


        elif right:
            self.snake_parts.insert(0, [self.x, self.y])

            self.direction = 2
            self.turn += 1
            # resets the screen so it looks like the square is moving
            pygame.draw.rect(win, BLACK, (self.x, self.y, width, height))
            try:
                # removes the old moves from list
                self.snake_head.remove([self.x, self.y])
            except Exception:
                pass

            self.x += height
            self.snake_head.append([self.x, self.y])
            self.snake_parts.pop(-1)

        elif left:
            self.snake_parts.insert(0, [self.x, self.y])
            self.direction = 4
            self.turn += 1
            # resets the screen so it looks like the square is moving
            pygame.draw.rect(win, BLACK, (self.x, self.y, width, height))
            try:
                # removes the old moves from list
                self.snake_head.remove([self.x, self.y])
            except Exception:
                pass

                pygame.draw.rect(win, BLACK, (self.x +  height, self.y , width, height))
            self.x -= height
            self.snake_head.append([self.x, self.y])
            self.snake_parts.pop(-1)
        x1 =  str(self.snake_head[0][0])
        y1 =  str(self.snake_head[0][1])
        # checks to see if the head hits the body
        if len(self.snake_parts) != 0:
            len_snake = len(self.snake_parts)
            for i in range(len_snake):
                xp1 = str(self.snake_parts[i][0])
                yp1 = str(self.snake_parts[i][1])
                if xp1 + yp1 == x1+y1:
                    self.die()
                    break
        #     checks to see if the snake goes out of bounds
        xh1 = (self.snake_head[0][0])
        yh1 = (self.snake_head[0][1])
        if self.x < 0 or self.y < 0 or self.x >= 1000 or self.y >= 1000:
            self.die()

        self.draw()
        if self.turn > 0:
            self.direction1 = 3
    def die(self):
        global bench
        self.snake_parts.clear()
        self.x = 500
        self.y = 500
        self.snake_head.clear()
        self.direction = 0
        pygame.draw.rect(win, BLACK, (0, 0, 1000, 1000))
        self.size = 1
        self.snake_head = [[self.x, self.y]]
        self.draw()
        try:
            steps = abs(abs((((self.size - 1) // 3) * 100) - self.moves) - 200)
            apples_ = ((self.size - 1) // 3)
            fit = steps + ((2 ** apples_) + (apples_ ** 2.1) * 500) - ((apples_ ** 1.2) * (0.25 * steps) ** 1.3)
            ge[important_number].fitness = fit

            if ge[important_number].fitness > bench[0]:
                bench = [ge[important_number].fitness, nets[important_number]]

            nets.pop(important_number)
            ge.pop(important_number)
            snakes.pop(important_number)
            moves.pop(important_number)
            apples.pop(important_number)

        except Exception:
            try:
                snakes.pop(important_number)
                moves.pop(important_number)
                apples.pop(important_number)
            except Exception:
                pass

    def collosion(self):
        x_cord = self.snake_head[0][0]
        y_cord = self.snake_head[0][1]
        for apple in apples:
            apples[0] = apple
            if x_cord == apple.x and y_cord == apple.y:
                self.grow()


    def grow(self):
        global time_grew
        self.size += 3
        self.moves += height

        try:
            if self.size != 4:
                x_cord = self.snake_parts[-1][0]
                y_cord = self.snake_parts[-1][1]
                for i in range(4):
                    if i != 0:
                        if self.direction == 1:
                            self.snake_parts.append([x_cord, y_cord + (width * i)])
                        elif self.direction == 3:
                            self.snake_parts.append([x_cord, y_cord - (width * i)])
                        elif self.direction == 2:
                            self.snake_parts.append([x_cord - (width * i), y_cord])
                        elif self.direction == 4:
                            self.snake_parts.append([x_cord + (width * i), y_cord])
            else:
                x_cord = self.snake_head[0][0]
                y_cord = self.snake_head[0][1]
                for i in range(4):
                    if i != 0:
                        if self.direction == 1:
                            self.snake_parts.append([x_cord, y_cord + (width * i)])
                        elif self.direction == 3:
                            self.snake_parts.append([x_cord, y_cord - (width * i)])
                        elif self.direction == 2:
                            self.snake_parts.append([x_cord - (width * i), y_cord])
                        elif self.direction == 4:
                            self.snake_parts.append([x_cord + (width * i), y_cord])
            self.draw()
            pygame.display.update()
            apples.pop(important_number)
            apples.insert(important_number, Apple())
            time_grew = time.time()
        except Exception:
            pass

        return True
class Apple:
    def __init__(self):
        x = random.randrange(0,1000, width)
        y = random.randrange(0,1000, width)
        self.x = x
        self.y = y
        self.color = RED
        self.draw()
    def draw(self):
        if second == True:
            # draws the circle to represent apple
            pygame.draw.circle(win, self.color, (self.x   + (width//2),self.y  + (width//2) ), width // 2)
            # pygame.draw.rect(win, WHITE, (self.x , self.y, width, height))

def main(genomes, config):
    global up
    global down
    global right
    global left
    global snakes
    global bench
    global important_number
    global snake
    global gen
    global ge
    global nets
    global moves
    global time_grew
    global apples
    global apple
    global second
    start_time = time.time()

    # initilizes variables
    gen += 1
    nets = []
    ge = []
    snakes = []
    moves = []
    apples = []
    bench = [-2, -2]
    run = True
    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        snakes.append(Snake(500,500))
        ge.append(genome)
        moves.append([])
        apples.append(Apple())

    # # ## if running traning data
    # # #
    # snakes.append(Snake(500,500))
    # moves.append([])
    # apples.append(Apple())
    # # remove code thats helps train like fitness
    # # make sure to set the pickle data to net

    


    test = False
    up= False
    down = False
    left = False
    right = False

    while run:
        clock.tick(27)

        events = pygame.event.get()
        #checks to see if specific buttons are pressed
        for x,snake in enumerate(snakes):
            snake.moves -= 1
            apple = apples[x]
            important_number = x
            elapsed_time = time.time() - start_time
            elapsed_time_grew = time.time() - time_grew



                # nets.pop(important_number)
                # ge.pop(important_number)
                # snakes.pop(important_number)
            important_number = x
            first_dir = []
            #program checks 8 directions and looks for distance between it and food(if there)
            #distance between it and wall
            #distance between it and x body piece(if there)
            #this code sets all of the data
            #sets variables
            distance_itself = 0
            direction_food = 0
            space_left = 0
            space_right = 0
            space_down = 0
            space_up = 0
            dist_food_up = 0
            dist_food_top_right = 0
            dist_food_right = 0
            dist_food_bottom_right = 0
            dist_food_bottom = 0
            dist_food_bottom_left = 0
            dist_food_left = 0
            dist_food_top_left = 0
            distance_itself_left_ = 0
            distance_itself_up_ = 0
            distance_itself_bottom_ = 0
            distance_itself_right_ = 0
            distance_itself_top_left_ = 0
            distance_itself_top_right_ = 0
            distance_itself_bottom_right_ = 0
            distance_itself_bottom_left_= 0
            #sets apple distances
            # if apple.x == snake.x and apple.y < snake.y:
            #     dist_food_up_squared =  (((snake.x // height) - (apple.x // height)) ** 2) + (((snake.y // height) - (apple.y // height)) ** 2)
            #     dist_food_up = (1/ (2 **round(math.sqrt(dist_food_up_squared))))
            # elif apple.x > snake.x and apple.y < snake.y:
            #     dist_food_top_right_squared = (((snake.x // height) - (apple.x // height)) ** 2) + (((snake.y // height) - (apple.y // height)) ** 2)
            #     dist_food_top_right = (1/ (2 ** round(math.sqrt(dist_food_top_right_squared))))
            # elif apple.x > snake.x and apple.y == snake.y:
            #     dist_food_right_squared = (((snake.x // height) - (apple.x // height)) ** 2) + (((snake.y // height) - (apple.y // height)) ** 2)
            #     dist_food_right = (1/ (2 **round(math.sqrt(dist_food_right_squared))))
            # elif apple.x > snake.x and apple.y > snake.y:
            #     dist_food_bottom_right_squared = (((snake.x // height) - (apple.x // height)) ** 2) + (((snake.y // height) - (apple.y // height)) ** 2)
            #     dist_food_bottom_right = (1/ (2 ** round(math.sqrt(dist_food_bottom_right_squared))))
            # elif apple.x == snake.x and apple.y > snake.y:
            #     dist_food_bottom_squared = (((snake.x // height) - (apple.x // height)) ** 2) + (((snake.y // height) - (apple.y // height)) ** 2)
            #     dist_food_bottom = (1/ (2 ** round(math.sqrt(dist_food_bottom_squared))))
            # elif apple.x < snake.x and apple.y > snake.y:
            #     dist_food_bottom_left_squared = (((snake.x // height) - (apple.x // height)) ** 2) + (((snake.y // height) - (apple.y // height)) ** 2)
            #     dist_food_bottom_left = (1/ (2 ** round(math.sqrt(dist_food_bottom_left_squared))))
            # elif apple.x < snake.x and apple.y == snake.y:
            #     dist_food_left_squared = (((snake.x // height) - (apple.x // height)) ** 2) + (((snake.y // height) - (apple.y // height)) ** 2)
            #     dist_food_left = (1/ (2  ** round(math.sqrt(dist_food_left_squared))))
            # elif apple.x < snake.x and apple.y < snake.y:
            #     dist_food_top_left_squared = (((snake.x // height) - (apple.x // height)) ** 2) + (((snake.y // height) - (apple.y // height)) ** 2)
            #     dist_food_top_left = (1/ (2 ** (round(math.sqrt(dist_food_top_left_squared))))   )
            # distance_food_squared =(((snake.x // height) - (apple.x // height)) ** 2) + (((snake.y // height) - (apple.y // height)) ** 2)
            # distance_food = (1 / (2 ** round(math.sqrt(distance_food_squared))))
            #
            # #top right
            # x_cord_ = snake.x
            # y_cord_ = snake.y
            # while y_cord_ >= 0 or x_cord_ <= 1000:
            #     y_cord_ -= height
            #     x_cord_ += height
            #     if len(snake.snake_parts) >= 1:
            #         for i in range(len(snake.snake_parts)):
            #             x_body = snake.snake_parts[i][0]
            #             y_body = snake.snake_parts[i][1]
            #             x_head = snake.snake_head[0][0]
            #             y_head = snake.snake_head[0][1]
            #             if x_cord_ == x_body and y_cord_ == y_body:
            #                 distance_itself_top_right_squared = (( (snake.x // height) - (x_cord_ // height)) ** 2) + (( (snake.y //height) - (y_cord_ // height)) ** 2)
            #                 distance_itself_top_right_ = ( 1/ (2 ** (round(math.sqrt(distance_itself_top_right_squared)))))
            #     if y_cord_ < 0 or x_cord_ >= 1000:
            #         break
            # distance_wall_top_right_squared = (abs(( snake.x // height) - (x_cord_ // height) ** 2)) + (abs( (snake.y //height) - (y_cord_ //height) ** 2))
            # distance_wall_top_right_ = 1/ (2 ** round(math.sqrt(distance_wall_top_right_squared)  ) )
            # #bottom right
            # x_cord_ = snake.x
            # y_cord_ = snake.y
            # while y_cord_ >= 0 or x_cord_ <= 1000:
            #     y_cord_ += height
            #     x_cord_ += height
            #     if len(snake.snake_parts) >= 1:
            #         for i in range(len(snake.snake_parts)):
            #             x_body = snake.snake_parts[i][0]
            #             y_body = snake.snake_parts[i][1]
            #             x_head = snake.snake_head[0][0]
            #             y_head = snake.snake_head[0][1]
            #             if x_cord_ == x_body and y_cord_ == y_body:
            #                 distance_itself_bottom_right_squared = (( (snake.x // height) - (x_cord_ // height)) ** 2) + (( (snake.y //height) - (y_cord_ // height)) ** 2)
            #                 distance_itself_bottom_right_ = ( 1/ (2 ** (round(math.sqrt(distance_itself_bottom_right_squared)))))
            #     if y_cord_ >= 1000 or x_cord_ >= 1000:
            #         break
            # distance_wall_bottom_right_squared = ((( snake.x // height) - (x_cord_ // height) ** 2)) + (( (snake.y //height) - (y_cord_ //height) ** 2))
            # distance_wall_bottom_right_ = (1 / (2 ** round(math.sqrt(distance_wall_bottom_right_squared))))
            # #bottom left
            # x_cord_ = snake.x
            # y_cord_ = snake.y
            # while y_cord_ >= 0 or x_cord_ < 1000:
            #     y_cord_ += height
            #     x_cord_ -= height
            #     if len(snake.snake_parts) >= 1:
            #         for i in range(len(snake.snake_parts)):
            #             x_body = snake.snake_parts[i][0]
            #             y_body = snake.snake_parts[i][1]
            #             x_head = snake.snake_head[0][0]
            #             y_head = snake.snake_head[0][1]
            #             if x_cord_ == x_body and y_cord_ == y_body:
            #                 distance_itself_bottom_left_squared = (( (snake.x // height) - (x_cord_ // height)) ** 2) + (( (snake.y //height) - (y_cord_ // height)) ** 2)
            #                 distance_itself_bottom_left_ = ( 1/ (2 ** (round(math.sqrt(distance_itself_bottom_left_squared)))))
            #     if y_cord_ >= 1000 or x_cord_ < 0:
            #         break
            # distance_wall_bottom_left_squared = ((( snake.x // height) - (x_cord_ // height) ** 2)) + (( (snake.y //height) - (y_cord_ //height) ** 2))
            # distance_wall_bottom_left_ = (1 / (2 ** round(math.sqrt(distance_wall_bottom_left_squared))))
            # #top left
            # x_cord_ = snake.x
            # y_cord_ = snake.y
            # while y_cord_ >= 0 or x_cord_ <= 1000:
            #     y_cord_ -= height
            #     x_cord_ -= height
            #     if len(snake.snake_parts) >= 1:
            #         for i in range(len(snake.snake_parts)):
            #             x_body = snake.snake_parts[i][0]
            #             y_body = snake.snake_parts[i][1]
            #             x_head = snake.snake_head[0][0]
            #             y_head = snake.snake_head[0][1]
            #             if x_cord_ == x_body and y_cord_ == y_body:
            #                 distance_itself_top_left_squared = (( (snake.x // height) - (x_cord_ // height)) ** 2) + (( (snake.y //height) - (y_cord_ // height)) ** 2)
            #                 distance_itself_top_left_ = ( 1/ (2 ** (round(math.sqrt(distance_itself_top_left_squared)))))
            #     if y_cord_ < 0 or x_cord_ < 0:
            #         break
            # distance_wall_top_left_squared = ((( snake.x // height) - (x_cord_ // height) ** 2)) + (( (snake.y //height) - (y_cord_ //height) ** 2))
            # distance_wall_top_left_ = (1 / (2 ** round(math.sqrt(distance_wall_top_left_squared))))
            #up
            #checks if wall is one space of the direction above
            if snake.y - height < 0:
                space_up = 1
                # checks to see if food is next to it
            #
            # if snake.x == apple.x and snake.y - height == apple.y:
            #     space_left = 2
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ <= 1000:
                y_cord_ -= height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if snake.x  == x_body and snake.y - height == y_body:
                            space_up = 1
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_up_squared = (( (snake.x // height) - (x_cord_ // height)) ** 2) + (( (snake.y //height) - (y_cord_ // height)) ** 2)
                            distance_itself_up_ = ( 1/ (2 ** (round(math.sqrt(distance_itself_up_squared)))))
                if y_cord_ < 0:
                    break
            #right
            # checks if wall is one space of the direction above
            if snake.x + height >= 1000:
                space_right = 1
            # cecks to see if food is next to it
            #
            #    if snake.x + height == apple.x and snake.y == apple.y:
            #        space_left = 2
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ <= 1000:
                x_cord_ += height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if snake.x + height == x_body and snake.y  == y_body:
                            space_right = 1
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_right_squared = (( (snake.x // height) - (x_cord_ // height)) ** 2) + (( (snake.y //height) - (y_cord_ // height)) ** 2)
                            distance_itself_right_ = ( 1/ (2 ** (round(math.sqrt(distance_itself_right_squared)))))
                if x_cord_ >= 1000:
                    break
            #down
            # checks if wall is one space of the direction above
            if snake.y + height >=1000:
                space_down = 1
            # checks to see if food is next to it
            # if snake.x == apple.x and snake.y + height == apple.y:
            #     space_left = 2
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ <= 1000:
                y_cord_ += height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if snake.x == x_body and snake.y + height == y_body:
                            space_down = 1
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_bottom_squared = (( (snake.x // height) - (x_cord_ // height)) ** 2) + (( (snake.y //height) - (y_cord_ // height)) ** 2)
                            distance_itself_bottom_ = ( 1/ (2 ** (round(math.sqrt(distance_itself_bottom_squared)))))
                if y_cord_ >= 1000:
                    break
            #left
            # checks if wall is one space of the direction above
            if snake.x - height < 0:
                space_left =1
            # checks to see if food is next to it
            # if snake.x - height == apple.x and snake.y == apple.y:
            #     space_left = 2
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ > 0 or x_cord_ <= 1000:
                x_cord_ -= height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if snake.x - height == x_body and snake.y  == y_body:
                            space_left = 1
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_left_squared = (( (snake.x // height) - (x_cord_ // height)) ** 2) + (( (snake.y //height) - (y_cord_ // height)) ** 2)
                            distance_itself_left_ = ( 1/ (2 ** (round(math.sqrt(distance_itself_left_squared)))))
                if x_cord_ < 0:
                    break
            #set variables
            # distance_wall_up = (1 / (2 ** (snake.y // height)))
            # distance_wall_right = (1 / 2 ** (round( (1000 - snake.x) // height)))
            # distance_wall_down = (1 / 2 ** (round( (1000 - snake.y) // height)))
            # distance_wall_left = (1 / (2 ** (snake.x // height)))
            #todo make sure walls and food dist works
            #sets direction to food 1 up 1.5 top right etc
            # if apple.x == snake.x and apple.y < snake.y:
            #     direction_food = 0
            # elif apple.x > snake.x and apple.y < snake.y:
            #     direction_food = 1
            # elif apple.x > snake.x and apple.y == snake.y:
            #     direction_food = 1
            # elif apple.x > snake.x and apple.y > snake.y:
            #     direction_food = 1
            # elif apple.x == snake.x and apple.y > snake.y:
            #     direction_food = 0
            # elif apple.x < snake.x and apple.y > snake.y:
            #     direction_food = -1
            # elif apple.x < snake.x and apple.y == snake.y:
            #     direction_food = -1
            # elif apple.x < snake.x and apple.y < snake.y:
            #     direction_food = -1
            #sees if the apple is to the left or to the right of it
            if apple.x < snake.x:
                direction_food_hor = -1
            elif apple.x == snake.x:
                direction_food_hor = 0
            elif apple.x > snake.x:
                direction_food_hor = 1
            ## sees if the apple is above or below it
            if apple.y < snake.y:
                direction_food_vert = -1
            elif apple.y == snake.y:
                direction_food_vert = 0
            elif apple.y > snake.y:
                direction_food_vert = 1

            #
            # if apple.y < snake.y:
            #     direction_food = 1
            #
            # elif apple.x > snake.x and apple.y == snake.y:
            #     direction_food = 2
            #
            # elif apple.y > snake.y:
            #     direction_food = 3
            # elif apple.x < snake.x and apple.y == snake.y:
            #     direction_food = 4
            # if len(snake.snake_parts) >=1:
            #     for i in range(len(snake.snake_parts)):
            #         x_body = snake.snake_parts[i][0]
            #         y_body = snake.snake_parts[i][1]
            #         x_head = snake.snake_head[0][0]
            #         y_head = snake.snake_head[0][1]
            #         if snake.direction == 1:
            #             if x_head == x_body and y_body < y_head:
            #                 distance_itself = y_head - y_body
            #         elif snake.direction == 2:
            #             if y_head == y_body and x_body > x_head:
            #                 distance_itself = x_body - x_head
            #         elif snake.direction == 3:
            #             if x_head == x_body and y_body > y_head:
            #                 distance_itself = y_body - y_head
            #         elif snake.direction == 4:
            #             if y_head == y_body and x_body < x_head:
            #                 distance_itself = x_head - x_body
            # output_info_24 = [(dist_food_up),(distance_itself_up_),(distance_wall_up),
            #                    (dist_food_top_right),(distance_itself_top_right_),(distance_wall_top_right_),
            #                    (dist_food_right),(distance_itself_right_),(distance_wall_right),
            #                    (dist_food_bottom_right),(distance_itself_bottom_right_),(distance_wall_bottom_right_),
            #                    (dist_food_bottom),(distance_itself_bottom_),(distance_wall_down),
            #                    (dist_food_bottom_left),(distance_itself_bottom_left_),(distance_wall_bottom_left_),
            #                    (dist_food_left),(distance_itself_left_),(distance_wall_bottom_left_),
            #                    (dist_food_top_left),(distance_itself_top_left_),(distance_wall_top_left_)]
            # output_info_walls = [distance_wall_left, distance_wall_up, distance_wall_down, distance_wall_right, direction_food]
            output_info_next_to = [space_up, space_right,space_down, space_left, direction_food_vert, direction_food_hor] #removed space_down
            f = genomes
            output = nets[x].activate(output_info_next_to)
            benchmark = [-1, -99999]

            tie = []
            out = []
            for i in range(4):

                out.append([i, output[i]])
            for i in range(len(output)):
                if out[i][1] > benchmark[1]:
                    tie.clear()
                    benchmark = out[i]
                    tie.append(benchmark)
                elif out[i][1] == benchmark[1]:
                    tie.append(out[i])
            random_num = random.randint(0,len(tie) - 1)
            for i in range(len(tie)):
                if i == random_num:
                    winner = tie[i]
            moves[x].append([winner[0]])
            #todo fix the 24 inputs, the formula i did doesnt really work give neg numbers
            if winner[0] == 0:
                try:
                    if snake.size > 1 and snake.direction == 2:
                        snake.die()

                except Exception:
                    pass
                up = False
                down = False
                left = True
                right = False
                snake.direction = 4
            elif winner[0] == 1:
                try:
                    snake.die()

                except Exception:
                    pass
                up = True
                down = False
                left = False
                right = False
                snake.direction = 1
            elif winner[0] == 2:
                try:
                    snake.die()


                except Exception:
                    pass
                up = False
                down = False
                left = False
                right = True
                snake.direction = 2
            elif winner[0] == 3:
                try:
                    snake.die()
                except Exception:
                    pass
                up = False
                down = True
                left = False
                right = False
                snake.direction = 3
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print(output_info_next_to)
                        # print(snake.size)
                        print(snake.snake_head)
                        print(apple.x, apple.y)
                        # print(snake.snake_parts)
                        print(snake.moves)
                        print(len(snakes))
                        print(len(apples))


                    if event.key == pygame.K_UP:
                        run = False


            snake.move()
            snake.collosion()

            if snake.moves <= 0:
                try:
                    snake.die()
                except Exception:
                    pass

            # try:
            #     if ge[important_number].fitness >= 100:
            #         pickle.dump(nets[important_number], open("best.pickle", 'wb'))
            #         # pickle.dump(genome, open("best1.pickle", 'w'))
            #         # pickle.dump(genomes, open("best2.pickle", 'w'))
            #
            # except Exception:
            #     pass


            if len(snakes) == 0:
                if (gen - 1) % 10 == 0:
                    print("f")
                    second = True
                    print(bench)
                    main2(bench[1], config)
                    second = False
                run = False


            pygame.display.update()


def main2(genomes, config):
    global up
    global down
    global right
    global left
    global snakes
    global important_number
    global snake
    global gen
    global ge
    global nets
    global moves
    global time_grew
    global apples
    global apple
    global left_
    global up_
    global down_
    global right_
    start_time = time.time()

    # initilizes variables
    nets = []
    ge = []
    snakes = []
    moves = []
    apples = []
    run = True
    snakes.append(Snake(500, 500))
    moves.append([])
    apples.append(Apple())

    # # ## if running traning data
    # # #
    # snakes.append(Snake(500,500))
    # moves.append([])
    # apples.append(Apple())
    # # remove code thats helps train like fitness
    # # make sure to set the pickle data to net

    test = False
    up = False
    down = False
    left = False
    right = False

    while run:
        clock.tick(27)

        events = pygame.event.get()
        # checks to see if specific buttons are pressed
        for x, snake in enumerate(snakes):

            snake.moves -= 1
            apple = apples[x]
            important_number = x
            elapsed_time = time.time() - start_time
            elapsed_time_grew = time.time() - time_grew


            # if elapsed_time <= 30:
            #     try:
            #         ge[x].fitness += 1/2000
            #     except Exception:
            #         pass
            # else:
            #     try:
            #         ge[x].fitness += 1/3000
            #     except Exception:
            #         pass
            # nets.pop(important_number)
            # ge.pop(important_number)
            # snakes.pop(important_number)
            important_number = x
            first_dir = []
            # program checks 8 directions and looks for distance between it and food(if there)
            # distance between it and wall
            # distance between it and x body piece(if there)
            # this code sets all of the data
            # sets variables
            down_ = 1
            up_ = 1
            right_ = 1
            left_ = 1
            distance_itself = 0
            direction_food = 0
            space_left = 0
            space_right = 0
            space_down = 0
            space_up = 0
            dist_food_up = 0
            dist_food_top_right = 0
            dist_food_right = 0
            dist_food_bottom_right = 0
            dist_food_bottom = 0
            dist_food_bottom_left = 0
            dist_food_left = 0
            dist_food_top_left = 0
            distance_itself_left_ = 0
            distance_itself_up_ = 0
            distance_itself_bottom_ = 0
            distance_itself_right_ = 0
            distance_itself_top_left_ = 0
            distance_itself_top_right_ = 0
            distance_itself_bottom_right_ = 0
            distance_itself_bottom_left_ = 0
            # sets apple distances
            if apple.x == snake.x and apple.y < snake.y:
                dist_food_up_squared = ((snake.x - apple.x) ** 2) + ((snake.y - apple.y) ** 2)
                dist_food_up = round(math.sqrt(dist_food_up_squared))
            elif apple.x > snake.x and apple.y < snake.y:
                dist_food_top_right_squared = ((snake.x - apple.x) ** 2) + ((snake.y - apple.y) ** 2)
                dist_food_top_right = round(math.sqrt(dist_food_top_right_squared))
            elif apple.x > snake.x and apple.y == snake.y:
                dist_food_right_squared = ((snake.x - apple.x) ** 2) + ((snake.y - apple.y) ** 2)
                dist_food_right = round(math.sqrt(dist_food_right_squared))
            elif apple.x > snake.x and apple.y > snake.y:
                dist_food_bottom_right_squared = ((snake.x - apple.x) ** 2) + ((snake.y - apple.y) ** 2)
                dist_food_bottom_right = round(math.sqrt(dist_food_bottom_right_squared))
            elif apple.x == snake.x and apple.y > snake.y:
                dist_food_bottom_squared = ((snake.x - apple.x) ** 2) + ((snake.y - apple.y) ** 2)
                dist_food_bottom = round(math.sqrt(dist_food_bottom_squared))
            elif apple.x < snake.x and apple.y > snake.y:
                dist_food_bottom_left_squared = ((snake.x - apple.x) ** 2) + ((snake.y - apple.y) ** 2)
                dist_food_bottom_left = round(math.sqrt(dist_food_bottom_left_squared))
            elif apple.x < snake.x and apple.y == snake.y:
                dist_food_left_squared = ((snake.x - apple.x) ** 2) + ((snake.y - apple.y) ** 2)
                dist_food_left = round(math.sqrt(dist_food_left_squared))
            elif apple.x < snake.x and apple.y < snake.y:
                dist_food_top_left_squared = ((snake.x - apple.x) ** 2) + ((snake.y - apple.y) ** 2)
                dist_food_top_left = round(math.sqrt(dist_food_top_left_squared))
            distance_food_squared = (((snake.x // height) - (apple.x // height)) ** 2) + (
                        ((snake.y // height) - (apple.y // height)) ** 2)
            distance_food = round(math.sqrt(distance_food_squared))
            # top right
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ <= 1000:
                y_cord_ -= height
                x_cord_ += height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_top_right_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
                            distance_itself_top_right_ = round(math.sqrt(distance_itself_top_right_squared))
                if y_cord_ < 0 or x_cord_ >= 1000:
                    break
            distance_wall_top_right_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
            distance_wall_top_right_ = round(math.sqrt(distance_wall_top_right_squared))
            # bottom right
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ <= 1000:
                y_cord_ += height
                x_cord_ += height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_bottom_right_squared = ((snake.x - x_cord_) ** 2) + (
                                        (snake.y - y_cord_) ** 2)
                            distance_itself_bottom_right_ = round(math.sqrt(distance_itself_bottom_right_squared))
                if y_cord_ >= 1000 or x_cord_ >= 1000:
                    break
            distance_wall_bottom_right_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
            distance_wall_bottom_right_ = round(math.sqrt(distance_wall_bottom_right_squared))
            # bottom left
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ < 1000:
                y_cord_ += height
                x_cord_ -= height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_bottom_left_squared = ((snake.x - x_cord_) ** 2) + (
                                        (snake.y - y_cord_) ** 2)
                            distance_itself_bottom_left_ = round(math.sqrt(distance_itself_bottom_left_squared))
                if y_cord_ >= 1000 or x_cord_ < 0:
                    break
            distance_wall_bottom_left_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
            distance_wall_bottom_left_ = round(math.sqrt(distance_wall_bottom_left_squared))
            # top left
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ <= 1000:
                y_cord_ -= height
                x_cord_ -= height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_top_left_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
                            distance_itself_top_left_ = round(math.sqrt(distance_itself_top_left_squared))
                if y_cord_ < 0 or x_cord_ < 0:
                    break
            distance_wall_top_left_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
            distance_wall_top_left_ = round(math.sqrt(distance_wall_top_left_squared))
            # up
            # checks if wall is one space of the direction above
            if snake.y - height < 0:
                up_ = 0
                space_up = 1
                # checks to see if food is next to it
            #
            # if snake.x == apple.x and snake.y - height == apple.y:
            #     space_left = 2
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ <= 1000:
                y_cord_ -= height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if snake.x == x_body and snake.y - height == y_body:
                            space_up = 1
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_up_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
                            distance_itself_up_ = round(math.sqrt(distance_itself_up_squared))
                if y_cord_ < 0:
                    break
            # right
            # checks if wall is one space of the direction above
            if snake.x + height >= 1000:
                right_ = 0
                space_right =1
            # cecks to see if food is next to it
            #
            #    if snake.x + height == apple.x and snake.y == apple.y:
            #        space_left = 2
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ <= 1000:
                x_cord_ += height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if snake.x + height == x_body and snake.y == y_body:
                            space_right = 1
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_right_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
                            distance_itself_right_ = round(math.sqrt(distance_itself_right_squared))
                if x_cord_ >= 1000:
                    break
            # down
            # checks if wall is one space of the direction above
            if snake.y + height >= 1000:
                down_ = 0
                space_down = 1
            # checks to see if food is next to it
            # if snake.x == apple.x and snake.y + height == apple.y:
            #     space_left = 2
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ >= 0 or x_cord_ <= 1000:
                y_cord_ += height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if snake.x == x_body and snake.y + height == y_body:
                            space_down = 1
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_bottom_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
                            distance_itself_bottom_ = round(math.sqrt(distance_itself_bottom_squared))
                if y_cord_ >= 1000:
                    break
            # left
            # checks if wall is one space of the direction above
            if snake.x - height < 0:
                left_ = 0
                space_left = 1
            # checks to see if food is next to it
            # if snake.x - height == apple.x and snake.y == apple.y:
            #     space_left = 2
            x_cord_ = snake.x
            y_cord_ = snake.y
            while y_cord_ > 0 or x_cord_ <= 1000:
                x_cord_ -= height
                if len(snake.snake_parts) >= 1:
                    for i in range(len(snake.snake_parts)):
                        x_body = snake.snake_parts[i][0]
                        y_body = snake.snake_parts[i][1]
                        x_head = snake.snake_head[0][0]
                        y_head = snake.snake_head[0][1]
                        if snake.x - height == x_body and snake.y == y_body:
                            space_left = 1
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_left_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
                            distance_itself_left_ = round(math.sqrt(distance_itself_left_squared))
                if x_cord_ < 0:
                    break
            # set variables
            distance_wall_up = snake.y
            distance_wall_right = 1000 - snake.x
            distance_wall_down = 1000 - snake.y
            distance_wall_left = snake.x
            # sets direction to food 1 up 1.5 top right etc
            # if apple.x == snake.x and apple.y < snake.y:
            #             #     direction_food = 0
            #             # elif apple.x > snake.x and apple.y < snake.y:
            #             #     direction_food = 1
            #             # elif apple.x > snake.x and apple.y == snake.y:
            #             #     direction_food = 1
            #             # elif apple.x > snake.x and apple.y > snake.y:
            #             #     direction_food = 1
            #             # elif apple.x == snake.x and apple.y > snake.y:
            #             #     direction_food = 0
            #             # elif apple.x < snake.x and apple.y > snake.y:
            #             #     direction_food = -1
            #             # elif apple.x < snake.x and apple.y == snake.y:
            #             #     direction_food = -1
            #             # elif apple.x < snake.x and apple.y < snake.y:
            #             #     direction_food = -1

            # sees if the apple is to the left or to the right of it
            if apple.x < snake.x:
                print("left")
                direction_food_hor = -1
            elif apple.x == snake.x:
                print("same x")
                direction_food_hor = 0
            elif apple.x > snake.x:
                print("right")
                direction_food_hor = 1
            ## sees if the apple is above or below it
            if apple.y < snake.y:
                print("above")
                direction_food_vert = -1
            elif apple.y == snake.y:
                print("same y")
                direction_food_vert = 0
            elif apple.y > snake.y:
                print("below")
                direction_food_vert = 1

            if up_ == 1: # if there is nothing above
                pygame.draw.rect(win, BLUE, (snake.x, snake.y - height, width, height))
            else:
                pygame.draw.rect(win, RED, (snake.x + (height //2), snake.y , width// 3, height// 3))

            if down_ == 1: # if there is nothing above
                pygame.draw.rect(win, BLUE, (snake.x, snake.y + height, width, height))
            else:
                pygame.draw.rect(win, RED, (snake.x + (height // 2), snake.y + (height - 10), width// 3, height// 3))
            if right_ == 1: # if there is nothing above
                pygame.draw.rect(win, BLUE, (snake.x + height, snake.y , width, height))
            else:
                pygame.draw.rect(win, RED, (snake.x +height - 10, snake.y + (height // 2), width// 3, height// 3))
            if left_ == 1: # if there is nothing above
                pygame.draw.rect(win, BLUE, (snake.x - height, snake.y , width, height))
            else:
                pygame.draw.rect(win, RED, (snake.x, snake.y + (height // 2), width // 3, height // 3))

            pygame.display.update()
            time.sleep(0.2)
            #
            # if apple.y < snake.y:
            #     direction_food = 1
            #
            # elif apple.x > snake.x and apple.y == snake.y:
            #     direction_food = 2
            #
            # elif apple.y > snake.y:
            #     direction_food = 3
            # elif apple.x < snake.x and apple.y == snake.y:
            #     direction_food = 4
            if len(snake.snake_parts) >= 1:
                for i in range(len(snake.snake_parts)):
                    x_body = snake.snake_parts[i][0]
                    y_body = snake.snake_parts[i][1]
                    x_head = snake.snake_head[0][0]
                    y_head = snake.snake_head[0][1]
                    if snake.direction == 1:
                        if x_head == x_body and y_body < y_head:
                            distance_itself = y_head - y_body
                    elif snake.direction == 2:
                        if y_head == y_body and x_body > x_head:
                            distance_itself = x_body - x_head
                    elif snake.direction == 3:
                        if x_head == x_body and y_body > y_head:
                            distance_itself = y_body - y_head
                    elif snake.direction == 4:
                        if y_head == y_body and x_body < x_head:
                            distance_itself = x_head - x_body
            output_info_24 = [(dist_food_up), (distance_itself_up_), (distance_wall_up),
                              (dist_food_top_right), (distance_itself_top_right_), (distance_wall_top_right_),
                              (dist_food_right), (distance_itself_right_), (distance_wall_right),
                              (dist_food_bottom_right), (distance_itself_bottom_right_), (distance_wall_bottom_right_),
                              (dist_food_bottom), (distance_itself_bottom_), (distance_wall_down),
                              (dist_food_bottom_left), (distance_itself_bottom_left_), (distance_wall_bottom_left_),
                              (dist_food_left), (distance_itself_left_), (distance_wall_bottom_left_),
                              (dist_food_top_left), (distance_itself_top_left_), (distance_wall_top_left_)]
            output_info_walls = [distance_wall_left, distance_wall_up, distance_wall_down, distance_wall_right,
                                 direction_food]
            output_info_next_to = [space_up, space_right, space_down, space_left, direction_food_vert, direction_food_hor]

            output = genomes.activate(output_info_next_to)
            benchmark = [-1, -99999]
            tie = []
            out = []
            for i in range(4):
                out.append([i, output[i]])
            for i in range(len(output)):
                if out[i][1] > benchmark[1]:
                    tie.clear()
                    benchmark = out[i]
                    tie.append(benchmark)
                elif out[i][1] == benchmark[1]:
                    tie.append(out[i])
            random_num = random.randint(0, len(tie) - 1)
            for i in range(len(tie)):
                if i == random_num:
                    winner = tie[i]
            moves[x].append([winner[0]])
            # todo have to add the exception with if its going up it cant go down
            if winner[0] == 0:
                try:
                    if snake.size > 1 and snake.direction == 2:

                        snakes.pop(important_number)
                        moves.pop(important_number)
                        apples.pop(important_number)

                except Exception:
                    pass
                up = False
                down = False
                left = True
                right = False
                snake.direction = 4
            elif winner[0] == 1:
                try:
                    if snake.size > 1 and snake.direction == 3:

                        snakes.pop(important_number)
                        moves.pop(important_number)
                        apples.pop(important_number)

                except Exception:
                    pass
                up = True
                down = False
                left = False
                right = False
                snake.direction = 1
            elif winner[0] == 2:
                try:
                    if snake.size > 1 and snake.direction == 4:

                        snakes.pop(important_number)
                        moves.pop(important_number)
                        apples.pop(important_number)


                except Exception:
                    pass
                up = False
                down = False
                left = False
                right = True
                snake.direction = 2
            elif winner[0] == 3:
                try:
                    if snake.size > 1 and snake.direction == 1:

                        snakes.pop(important_number)
                        moves.pop(important_number)
                        apples.pop(important_number)
                except Exception:
                    pass
                up = False
                down = True
                left = False
                right = False
                snake.direction = 3
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print(output_info_next_to)
                        # print(snake.size)
                        print(snake.snake_head)
                        print(apple.x, apple.y)
                        # print(snake.snake_parts)
                        print(snake.moves)
                        print(len(snakes))
                        print(len(apples))

                    if event.key == pygame.K_UP:
                        run = False

            snake.move()
            snake.collosion()
            if snake.moves <= 0:
                try:
                    snakes.pop(important_number)
                    moves.pop(important_number)
                    apples.pop(important_number)
                except Exception:
                    pass


            if len(snakes) == 0:
                run = False

            pygame.display.update()


def run(config_path, genome_path="best.pickle"):
    global second
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)


    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(5))



    # Unpickle saved winner
    # def restore_checkpoint():
    #     with open(genome_path, "rb") as f:
    #         genome = pickle.load(f)
    #         print(genome)
    #         return main(genome, (config))

    # def restore_checkpoint():
    #     """Resumes the simulation from a previous saved point."""
    #     with open(genome_path, "r") as f:
    #         # generation, config, population, species_set, rndstate = pickle.load(f)
    #         # random.setstate(rndstate)
    #         genome_ = pickle.load(f)
    #         print(genome_)
    #         return main(s, (config))

    winner_ = p.run(main,2000)

    print('\nBest genome:\n{!s}'.format(winner_))
    net = neat.nn.FeedForwardNetwork.create(winner_, config)
    keep = True
    events = pygame.event.get()
    second = True

    main2(net, config)
    check = neat.Checkpointer(5)

    ## restore checkpoint
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-22')
    # p.run(main, 100)
if __name__ == "__main__":
    local_Dir = os.path.dirname(__file__)
    config_path = os.path.join(local_Dir,"config-feedforward.txt")
    run(config_path)
