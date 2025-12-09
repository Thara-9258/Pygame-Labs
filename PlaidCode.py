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
DARK_PURPLE = (62, 37, 99)
VIOLET_PURPLE = (157, 60, 201)
DARK_PINK = (184, 66, 154)
PERWINKLE = (181, 190, 245)

#---------Declaring width and Height--------------#
windowWidth = 720
windowHeight = 720
#---------Game Loop----------------------#

running = True
while running:
    
#-------------------------------EVENTS----------------------------------# 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       

    window.fill(LAVENDAR)
#---------------Horizontal Lines------------#
    y = 0

    while y <= windowHeight:

        pygame.draw.line(window, DARK_PINK, (0, y,), (windowWidth, y), 20)

        y += 40 #spacing of the pattern


#-------------Vertical Lines----------------#
    x = 0
    
    while x <= windowWidth:
        
        pygame.draw.line(window, DARK_PURPLE, (x, 0), (x, windowHeight), 20)
        pygame.draw.line(window, VIOLET_PURPLE, (x+20, 0), (x+20, windowHeight), 5)
        
        x += 40 #spacing of then pattern
#------------Diaganol Lines------------------#

#    start_x = 0
#    start_y = 0 

#    while start_x <= windowWidth:
#        pygame.draw.line(window, PERWINKLE, (start_x,0), (start_x+windowHeight, windowHeight), 10)

#        start_x += 40

#---------Display------------------------#
    pygame.display.flip()
    clock.tick(60)
   
pygame.quit()



