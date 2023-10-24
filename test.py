import numpy as np
import pygame


pygame.init()
while True:
    for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                            print('1')
                    elif event.button ==2:
                            print('2')
                    elif event.button == 3:
                            print('3')