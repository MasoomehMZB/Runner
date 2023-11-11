import pygame
import pygame
import sys

# initializing the constructor
pygame.init()
# screen resolution
res = (800, 550)

# opens up a window
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

test_font = pygame.font.Font('font/Crang.ttf', 50)

background_surface = pygame.image.load('graphics/background1.jpg').convert()
ground_surface = pygame.surface.Surface((0, -440))
ground_surface.fill('Blue', .,0)
text_surface = test_font.render('My game', False,'Black')

wizard_surface = pygame.image.load('graphics/Character.png').convert_alpha()
wizard_Xpos = 600

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0, 0))
    screen.blit(text_surface, (300, 50))
    wizard_Xpos -= 3
    if wizard_Xpos < -200:
       wizard_Xpos = 900

    screen.blit(wizard_surface, (wizard_Xpos, 250))

    pygame.display.update()
    clock.tick(60)
