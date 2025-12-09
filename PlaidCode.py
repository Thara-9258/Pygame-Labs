#-------------- Setup ------------------#

import pygame
pygame.init()

window = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()

#------------Declaring Colors------------#

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
LAVENDAR = (212, 197, 235)
DARK_PRUPLE = (62, 37, 99)

#---------Declaring width and Height--------------#
windowWidth = 720
windowHeight = 720
#---------Game Loop----------------------#

running = True
while running:
    
#---------EVENTS----------------------------------# 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       

    window.fill(LAVENDAR)

    x = 0
    while x <= windowWidth:
        pygame.draw.line(window, DARK_PRUPLE, (x, 0), (x, windowHeight), 20)
        # pygame.draw.line(window, GREEN, (x+4, 0), (x+4, windowHeight), 2)
        x += 40 #spacing of pattern


#---------Display------------------------#
    pygame.display.flip()
    clock.tick(60)
   
pygame.quit()



