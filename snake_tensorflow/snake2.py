import neat
from neat.population import Population
import pygame
import time
import random
import os
import math
import pickle

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
    start_time = time.time()

    # initilizes variables
    gen += 1
    nets = []
    ge = []
    snakes = []
    moves = []
    apples = []
    run = True
    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        snakes.append(Snake(500, 500))
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
            distance_itself = 0
            direction_food = 0
            space_left = 1
            space_right = 1
            space_down = 1
            space_up = 1
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
            distance_food_squared = ((snake.x - apple.x) ** 2) + ((snake.y - apple.y) ** 2)
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
                space_up = 0
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
                            space_up = 0
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_up_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
                            distance_itself_up_ = round(math.sqrt(distance_itself_up_squared))
                if y_cord_ < 0:
                    break
            # right
            # checks if wall is one space of the direction above
            if snake.x + height >= 1000:
                space_right = 0
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
                            space_right = 0
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_right_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
                            distance_itself_right_ = round(math.sqrt(distance_itself_right_squared))
                if x_cord_ >= 1000:
                    break
            # down
            # checks if wall is one space of the direction above
            if snake.y + height >= 1000:
                space_down = 0
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
                            space_down = 0
                        if x_cord_ == x_body and y_cord_ == y_body:
                            distance_itself_bottom_squared = ((snake.x - x_cord_) ** 2) + ((snake.y - y_cord_) ** 2)
                            distance_itself_bottom_ = round(math.sqrt(distance_itself_bottom_squared))
                if y_cord_ >= 1000:
                    break
            # left
            # checks if wall is one space of the direction above
            if snake.x - height < 0:
                space_left = 0
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
                            space_left = 0
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
            if apple.x == snake.x and apple.y < snake.y:
                direction_food = 0
            elif apple.x > snake.x and apple.y < snake.y:
                direction_food = 1
            elif apple.x > snake.x and apple.y == snake.y:
                direction_food = 1
            elif apple.x > snake.x and apple.y > snake.y:
                direction_food = 1
            elif apple.x == snake.x and apple.y > snake.y:
                direction_food = 0
            elif apple.x < snake.x and apple.y > snake.y:
                direction_food = -1
            elif apple.x < snake.x and apple.y == snake.y:
                direction_food = -1
            elif apple.x < snake.x and apple.y < snake.y:
                direction_food = -1
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
            output_info_next_to = [space_up, space_right, space_down, space_left, direction_food]
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
            random_num = random.randint(0, len(tie) - 1)
            for i in range(len(tie)):
                if i == random_num:
                    winner = tie[i]
            moves[x].append([winner[0]])
            # todo have to add the exception with if its going up it cant go down
            if winner[0] == 0:
                try:
                    if snake.size > 1 and snake.direction == 2:
                        ge[important_number].fitness -= 2
                        nets.pop(important_number)
                        ge.pop(important_number)
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
                        ge[important_number].fitness -= 2
                        nets.pop(important_number)
                        ge.pop(important_number)
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
                        ge[important_number].fitness -= 2
                        nets.pop(important_number)
                        ge.pop(important_number)
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
                        ge[important_number].fitness -= 2
                        nets.pop(important_number)
                        ge.pop(important_number)
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
                    ge[x].fitness -= snake.size + 3
                    nets.pop(important_number)
                    ge.pop(important_number)
                    snakes.pop(important_number)
                    moves.pop(important_number)
                    apples.pop(important_number)
                    print("d")
                except Exception:
                    pass

            try:
                if ge[important_number].fitness >= 100:
                    pickle.dump(nets[important_number], open("best.pickle", 'wb'))
                    # pickle.dump(genome, open("best1.pickle", 'w'))
                    # pickle.dump(genomes, open("best2.pickle", 'w'))

            except Exception:
                pass
            if len(snakes) == 0:
                run = False

            pygame.display.update()