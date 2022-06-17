import random
import pygame
from datetime import datetime
import re

global rat
global consume_hor
global consume_ver
global hits




def main():
    pygame.init()
    # arbitrary board size
    board = pygame.display.set_mode((600, 600))
    pygame.display.update()

    hits = 0
    horizontal = 300
    vertical = 320
    horizontal_change = 0
    vertical_change = 0
    consume_hor = 300
    consume_ver = 100
    near_one = near_two = near_three = near_four = near_five = 0
    far_one = far_two = far_three = far_four = far_five = 20

    line_one = pygame.draw.line(board, (0, 0, 0), (0, 0), (0, 0), 0) 
    line_two = pygame.draw.line(board, (0, 0, 0), (0, 0), (0, 0), 0)
    line_three = pygame.draw.line(board, (0, 0, 0), (0, 0), (0, 0), 0)
    line_four = pygame.draw.line(board, (0, 0, 0), (0, 0), (0, 0), 0)
    line_five = pygame.draw.line(board, (0, 0, 0), (0, 0), (0, 0), 0)
    



    truth = True
    moving_right = True

    clock_slow = pygame.time.Clock()


    while truth: 


        for action in pygame.event.get():
        

            # had break statement here but only broke for loop, not while    
            if action.type == pygame.QUIT: truth = False

            # mention moving by one block problem, so had to change from this to adding clock and stuff
            if action.type == pygame.KEYDOWN:

                if action.key == pygame.K_UP: vertical_change = -7
                elif action.key == pygame.K_RIGHT: horizontal_change = 7
                elif action.key == pygame.K_DOWN: vertical_change = 7 
                elif action.key == pygame.K_LEFT: horizontal_change = -7


        # slows down framerate so icon does not move at the speed of light
        clock_slow.tick(22)
        horizontal += horizontal_change
        vertical += vertical_change


        if far_one >= 600 and moving_right: 
            near_one -= 10
            far_one -= 10
            moving_right = False
        elif moving_right:
            near_one += 10
            far_one += 10
        elif not moving_right:
            near_one -= 10
            far_one -= 10  
        
        if near_one < 0 and not moving_right:
            near_one += 10
            far_one += 10
            moving_right = True       


        if hits == 1: 
            line_one = pygame.draw.line(board, (255, 0, 0), (near_one, 100), (far_one, 100), 3) 
        elif hits == 2:
            line_one = pygame.draw.line(board, (255, 0, 0), (near_one, 100), (far_one, 100), 3) 
            line_two = pygame.draw.line(board, (255, 0, 0), (near_one, 200), (far_one, 200), 3)
        elif hits == 3: 
            line_one = pygame.draw.line(board, (255, 0, 0), (near_one, 100), (far_one, 100), 3) 
            line_two = pygame.draw.line(board, (255, 0, 0), (near_one, 200), (far_one, 200), 3)
            line_three = pygame.draw.line(board, (255, 0, 0), (near_one, 300), (far_one, 300), 3)
        elif hits == 4: 
            line_one = pygame.draw.line(board, (255, 0, 0), (near_one, 100), (far_one, 100), 3) 
            line_two = pygame.draw.line(board, (255, 0, 0), (near_one, 200), (far_one, 200), 3)
            line_three = pygame.draw.line(board, (255, 0, 0), (near_one, 300), (far_one, 300), 3)
            line_four = pygame.draw.line(board, (255, 0, 0), (near_one, 400), (far_one, 400), 3)
        elif hits == 5: 
            line_one = pygame.draw.line(board, (255, 0, 0), (near_one, 100), (far_one, 100), 3) 
            line_two = pygame.draw.line(board, (255, 0, 0), (near_one, 200), (far_one, 200), 3)
            line_three = pygame.draw.line(board, (255, 0, 0), (near_one, 300), (far_one, 300), 3)
            line_four = pygame.draw.line(board, (255, 0, 0), (near_one, 400), (far_one, 400), 3)
            line_five = pygame.draw.line(board, (255, 0, 0), (near_one, 500), (far_one, 500), 3)
        elif hits > 0:
            line_one = pygame.draw.line(board, (255, 0, 0), (near_one, 100), (far_one, 100), 3) 
            line_two = pygame.draw.line(board, (255, 0, 0), (near_one, 200), (far_one, 200), 3)
            line_three = pygame.draw.line(board, (255, 0, 0), (near_one, 300), (far_one, 300), 3)
            line_four = pygame.draw.line(board, (255, 0, 0), (near_one, 400), (far_one, 400), 3)
            line_five = pygame.draw.line(board, (255, 0, 0), (near_one, 500), (far_one, 500), 3)




        # look up colors here. mention first two pos. on board, last two width and height
        snake = pygame.draw.rect(board, (255, 0, 255), pygame.Rect(horizontal, vertical, 20, 20))

        for pixel in range(20):
            if pixel + horizontal >= 600 or pixel + vertical >= 600 or horizontal < 0 or \
                vertical < 0: truth =- False
        # drawing consumed piece, show looking 
        # rat = pygame.draw.rect(board, (0, 255, 0), 
        # pygame.Rect(consume_hor, consume_ver, 12, 12))
        rat = rat_reload(consume_hor, consume_ver, board)

        # updates board
        pygame.display.flip()
        # reset board, show what happens when this is not present
        board = pygame.display.set_mode((600, 600))


        if hits > 0 and (snake.colliderect(line_one) or snake.colliderect(line_two) or \
            snake.colliderect(line_three) or snake.colliderect(line_four) or \
            snake.colliderect(line_five)): truth = False


        # tried using a for loop to check pixel by pixel but this function
        # allowed for me to not have to change frame rate
        if snake.colliderect(rat): 
            curr_time = datetime.now().time()
            # a = curr_time.strftime("%H:%M:%S")
            # print(a)
            # strftime() is time objects to string method
            # note time is represemted like 19:39:05
            first_set = re.findall("^[\d]([\d]):[\d]([\d]):[\d]([\d])$", curr_time.strftime("%H:%M:%S"))
            second_set = re.findall("^([\d])[\d]:([\d])[\d]:([\d])[\d]$", curr_time.strftime("%H:%M:%S"))

            # second 2, 5, 5  (one + two + three * 48 -mod magic for this num)
            # first 9, 9, 9  ((one + two + three) * 21) + 15
            print(curr_time.strftime("%H:%M:%S"))
            print(first_set)
            print(second_set)
            random_one = 0
            for integer_first in first_set[0]:
                random_one += int(integer_first)
                # if integer_first == 0: random_one *= 1
                # else: random_one *= int(integer_first)

            random_two = 0
            for integer_second in second_set[0]:
                random_two += int(integer_second)
                # if integer_second == 0: random_two *= 1
                # else: random_two *= int(integer_second)
            
            print("one{}",random_one)
            print("two{}",random_two)

            consume_hor = (random_one * random.randint(1, 21)) + 15
            consume_ver = random_two * random.randint(1, 48)

            hits += 1

            # if consume_hor % 10 = 0: 

            # print(consume_hor)
            # print(consume_ver)


def rat_reload(horizontal, vertical, board):
    rat = pygame.draw.rect(board, (0, 255, 0), pygame.Rect(horizontal, vertical, 12, 12))
    return rat


main()
pygame.quit()