#!/usr/bin/env python
#
# U.S. Flag
# by Adam Sommer
#

import os
import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (253, 255, 0)

pygame.init()

window = pygame.display.set_mode((600, 400))
window.fill(WHITE)


def ribbon_text_setup(text, pos, rot):
    ribbon_font = pygame.font.Font('freesansbold.ttf', 16)

    text = ribbon_font.render(text, True, BLACK)
    text_rect = text.get_rect()
    text_rect.center = pos
    text = pygame.transform.rotate(text, rot)

    return (text, text_rect)

while True:

    blue_union = pygame.draw.rect(window, BLUE, (0, 0, 200, 400))
    red_union = pygame.draw.rect(window, RED, (200, 0, 400, 200))

    # The Star.
    pygame.draw.polygon(window, WHITE, [
        (80, 195),  # left arm
        (95, 195),  # left upper corner
        (105, 170),  # peak
        (110, 195),  # right upper corner
        (125, 195),  # right arm
        (110, 205),  # right hip
        (115, 230), # bottom right 
        (103, 205),  # bottom middle
        (85, 230), # bottom left
        (95, 205),  # left hip
    ])

    # Add the N and C.
    letter_font = pygame.font.Font('freesansbold.ttf', 70)
    n = letter_font.render('N', True, YELLOW)
    n_rect = n.get_rect()
    n_rect.center = (40, 205)
    c = letter_font.render('C', True, YELLOW)
    c_rect = c.get_rect()
    c_rect.center = (155, 205)
    window.blit(c, c_rect)
    window.blit(n, n_rect)


    # Add the ribbons.
    top_ribbon = pygame.image.load(os.path.join('images', 'ribbon_top.png'))
    window.blit(top_ribbon, (20, 100))
    bottom_ribbon = pygame.image.load(os.path.join('images', 'ribbon_bottom.png'))
    window.blit(bottom_ribbon, (20, 230))

    # Ribbon text.
    may_text = ribbon_text_setup('May', (60, 115), 20)
    window.blit(may_text[0], may_text[1])
    twentieth_text = ribbon_text_setup('20th', (103, 115), 0)
    window.blit(twentieth_text[0], twentieth_text[1])
    seventyfive_text = ribbon_text_setup('1775', (140, 115), -20)
    window.blit(seventyfive_text[0], seventyfive_text[1])

    april_text = ribbon_text_setup('April', (65, 265), -17)
    window.blit(april_text[0], april_text[1])
    twelve_text = ribbon_text_setup('12th', (106, 276), -3)
    window.blit(twelve_text[0], twelve_text[1])
    seventysix_text = ribbon_text_setup('1776', (143, 265), 20)
    window.blit(seventysix_text[0], seventysix_text[1])

    pygame.display.update()
