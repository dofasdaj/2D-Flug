import pygame
import sys
import random
import time
from pygame.locals import *
from pygame import *
def main():
    displaygröße = (1200,700)
    display = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("2D")
    while 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                print(1)
        pygame.display.flip()
        bild = pygame.image.load("Spielwelt.bmp")
        display.blit(bild, (0,0))
        
main()
