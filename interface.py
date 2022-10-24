# The Display portion of the program
import pygame
from pygame.locals import *

pygame.init()

array_width = 150
array_height = 150
positionX = 5
positionY = 5
main_display_2D_array = [[255] * array_width for i in range(array_height)]


if __name__ == "__main__":
    run = True
    pygame.display.init()
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode([screen_width, screen_height])

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        for i in range(len(main_display_2D_array)):
            for j in range(len(main_display_2D_array[0])):
                pygame.draw.rect(screen, (main_display_2D_array[i][j],main_display_2D_array[i][j],main_display_2D_array[i][j]), (positionX, positionY, 5, 5))
                positionX += 6
                if positionX >= screen_width - 10:
                    positionX = 5
                    positionY += 6
        positionX = 5
        positionY = 5
        pygame.display.update()
