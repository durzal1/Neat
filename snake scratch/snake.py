import pygame
import time
import random
import os
import math
from Genome import *
import pickle
import gzip

# variables

time_grew = time.time()
height = 100
width = 100
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
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
        # initializes the snake
        self.snake_head = [[x, y]]
        self.snake_parts = []
        self.size = 1
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = GREEN
        # self.draw()
        self.turn = 1
        self.moves = 200
        self.dead = False
        self.direction = 0  # 0 = none | 1 = up | 2 = right | 3= down | 4 = left

    def draw(self):
        # draws the rectangle to represent snake
        pygame.draw.rect(win, BLACK, (0, 0, 1000, 1000))
        pygame.draw.rect(win, self.color, (self.x, self.y, width, height))
        if self.direction1 != 0:
            for i in range(len(snake.snake_parts)):
                x = snake.snake_parts[i][0]
                y = snake.snake_parts[i][1]
                pygame.draw.rect(win, self.color, (x, y, width, height))

    def move(self):
        # checks to see what direction the snake is moving
        # variables like up and down are set in the events section of the program;
        if up:
            # adds first part of snake
            self.snake_parts.insert(0, [self.x, self.y])

            self.direction = 1
            self.turn += 1
            # resets the screen so it looks like the square is moving
            # pygame.draw.rect(win, BLACK, (self.x, self.y, width, height))
            try:
                # removes the old snake head from list
                self.snake_head.remove([self.x, self.y])
            except Exception:
                pass
            self.y -= height
            self.snake_head.append([self.x, self.y])
            # deletes last square of snake
            self.snake_parts.pop(-1)
        elif down:
            self.snake_parts.insert(0, [self.x, self.y])

            self.direction = 3
            self.turn += 1
            # resets the screen so it looks like the square is moving
            # pygame.draw.rect(win, BLACK, (self.x, self.y, width, height))
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
            # pygame.draw.rect(win, BLACK, (self.x, self.y, width, height))
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
            # pygame.draw.rect(win, BLACK, (self.x, self.y, width, height))
            try:
                # removes the old moves from list
                self.snake_head.remove([self.x, self.y])
            except Exception:
                pass

                # pygame.draw.rect(win, BLACK, (self.x + height, self.y, width, height))
            self.x -= height
            self.snake_head.append([self.x, self.y])
            self.snake_parts.pop(-1)
        x1 = str(self.snake_head[0][0])
        y1 = str(self.snake_head[0][1])
        # checks to see if the head hits the body
        if len(self.snake_parts) != 0:
            len_snake = len(self.snake_parts)
            for i in range(len_snake):
                xp1 = str(self.snake_parts[i][0])
                yp1 = str(self.snake_parts[i][1])
                if xp1 + yp1 == x1 + y1:
                    self.die()
                    break
        #     checks to see if the snake goes out of bounds
        xh1 = (self.snake_head[0][0])
        yh1 = (self.snake_head[0][1])
        if self.x < 0 or self.y < 0 or self.x >= 1000 or self.y >= 1000:
            self.die()

        # self.draw()
        if self.turn > 0:
            self.direction1 = 3

    def die(self):
        global bench
        self.snake_parts.clear()
        self.x = 500
        self.y = 500
        self.dead = True
        self.snake_head.clear()
        self.direction = 0
        # pygame.draw.rect(win, BLACK, (0, 0, 1000, 1000))
        self.size = 1
        self.snake_head = [[self.x, self.y]]
        self.draw()



    def collosion(self, apple):
        x_cord = self.snake_head[0][0]
        y_cord = self.snake_head[0][1]
        if x_cord == apple.x and y_cord == apple.y:
            self.grow()
        # for apple in apples:
        #     apples[0] = apple
        #     if x_cord == apple.x and y_cord == apple.y:
        #         self.grow()

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
        x = random.randrange(0, 1000, width)
        y = random.randrange(0, 1000, width)
        self.x = x
        self.y = y
        self.color = RED
        # self.draw()

    def draw(self):
        # draws the circle to represent apple
        pygame.draw.circle(win, self.color, (self.x + (width // 2), self.y + (width // 2)), width // 2)
        # pygame.draw.rect(win, WHITE, (self.x , self.y, width, height))


class main_snake():
    def __init__(self, genome):
        # initilizes variables
        self.gen = 0
        self.snake = []
        self.moves = []
        self.apple = Apple()
        self.bench = [-2, -2]
        self.run = True
        for i in range(1):
            self.snake.append(Snake(500, 500))
            self.moves.append([])
            # self.apple.append(Apple())

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
        run = True
        while run:
            clock.tick(27)
            events = pygame.event.get()
            # checks to see if specific buttons are pressed
            for x, snake in enumerate(self.snake):
                snake.moves -= 1
                apple = self.apple
                important_number = x
                elapsed_time = time.time() - start_time
                elapsed_time_grew = time.time() - time_grew

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
                # up
                # checks if wall is one space of the direction above
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
                            if snake.x == x_body and snake.y - height == y_body:
                                space_up = 1
                            if x_cord_ == x_body and y_cord_ == y_body:
                                distance_itself_up_squared = (((snake.x // height) - (x_cord_ // height)) ** 2) + (
                                            ((snake.y // height) - (y_cord_ // height)) ** 2)
                                distance_itself_up_ = (1 / (2 ** (round(math.sqrt(distance_itself_up_squared)))))
                    if y_cord_ < 0:
                        break
                # right
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
                            if snake.x + height == x_body and snake.y == y_body:
                                space_right = 1
                            if x_cord_ == x_body and y_cord_ == y_body:
                                distance_itself_right_squared = (((snake.x // height) - (x_cord_ // height)) ** 2) + (
                                            ((snake.y // height) - (y_cord_ // height)) ** 2)
                                distance_itself_right_ = (1 / (2 ** (round(math.sqrt(distance_itself_right_squared)))))
                    if x_cord_ >= 1000:
                        break
                # down
                # checks if wall is one space of the direction above
                if snake.y + height >= 1000:
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
                                distance_itself_bottom_squared = (((snake.x // height) - (x_cord_ // height)) ** 2) + (
                                            ((snake.y // height) - (y_cord_ // height)) ** 2)
                                distance_itself_bottom_ = (
                                            1 / (2 ** (round(math.sqrt(distance_itself_bottom_squared)))))
                    if y_cord_ >= 1000:
                        break
                # left
                # checks if wall is one space of the direction above
                if snake.x - height < 0:
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
                                distance_itself_left_squared = (((snake.x // height) - (x_cord_ // height)) ** 2) + (
                                            ((snake.y // height) - (y_cord_ // height)) ** 2)
                                distance_itself_left_ = (1 / (2 ** (round(math.sqrt(distance_itself_left_squared)))))
                    if x_cord_ < 0:
                        break
                # set variables
                # distance_wall_up = (1 / (2 ** (snake.y // height)))
                # distance_wall_right = (1 / 2 ** (round( (1000 - snake.x) // height)))
                # distance_wall_down = (1 / 2 ** (round( (1000 - snake.y) // height)))
                # distance_wall_left = (1 / (2 ** (snake.x // height)))
                # todo make sure walls and food dist works
                # sets direction to food 1 up 1.5 top right etc
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
                # sees if the apple is to the left or to the right of it
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
                output_info_next_to = [space_up, space_right, space_down, space_left]  # removed space_down
                output = genome.calculate(output_info_next_to)
                benchmark = [-1, -99999]
                vals = []
                for out in output:
                    vals.append(out)
                vals.sort()
                for i in range(len(output)):
                    if output[i] == vals[-1]:
                        winner = [i,output[i]]
                self.moves[x].append([winner[0]])
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
                # for event in events:
                #     if event.type == pygame.KEYDOWN:
                #         if event.key == pygame.K_SPACE:
                #
                #
                #         if event.key == pygame.K_UP:
                #             run = False
                snake.move()
                snake.collosion(apple)

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

                if snake.dead == True:
                    steps = abs(abs((((snake.size - 1) // 3) * 100) - snake.moves) - 200)
                    apples_ = ((snake.size - 1) // 3)
                    fit = steps + ((2 ** apples_) + (apples_ ** 2.1) * 500) - ((apples_ ** 1.2) * (0.25 * steps) ** 1.3)
                    genome.fitness = fit
                    run = False
                # snake.draw()
                # apple.draw()
                pygame.display.update()

#
# def run(config_path, genome_path="best.pickle"):
#     global second
#     config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
#                                 neat.DefaultSpeciesSet, neat.DefaultStagnation,
#                                 config_path)
#
#     # Create the population, which is the top-level object for a NEAT run.
#     p = neat.Population(config)
#
#     # Add a stdout reporter to show progress in the terminal.
#     p.add_reporter(neat.StdOutReporter(True))
#     stats = neat.StatisticsReporter()
#     p.add_reporter(stats)
#     # p.add_reporter(neat.Checkpointer(5))
#
#     # Unpickle saved winner
#     # def restore_checkpoint():
#     #     with open(genome_path, "rb") as f:
#     #         genome = pickle.load(f)
#     #         print(genome)
#     #         return main(genome, (config))
#
#     # def restore_checkpoint():
#     #     """Resumes the simulation from a previous saved point."""
#     #     with open(genome_path, "r") as f:
#     #         # generation, config, population, species_set, rndstate = pickle.load(f)
#     #         # random.setstate(rndstate)
#     #         genome_ = pickle.load(f)
#     #         print(genome_)
#     #         return main(s, (config))
#
#     winner_ = p.run(main, 2000)
#
#     print('\nBest genome:\n{!s}'.format(winner_))
#     net = neat.nn.FeedForwardNetwork.create(winner_, config)
#     keep = True
#     events = pygame.event.get()
#     second = True
#
#     main2(net, config)
#     check = neat.Checkpointer(5)
#
#     ## restore checkpoint
#     # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-22')
#     # p.run(main, 100)
#
#
# if __name__ == "__main__":
#     local_Dir = os.path.dirname(__file__)
#     config_path = os.path.join(local_Dir, "config-feedforward.txt")
#     run(config_path)
