# -----------------------------------------------------------------------------
# TEXT & FONT LAB - RANSOM NOTE
# 
# Use your new knowledge of text in Pygame to make a ransom note similar to the picture above.
# 
# You use whatever fonts you want as long as you use at least 1 custom font.
# 
# The message can say whatever you want as long as it is school safe (remember the code of conduct).
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different font styles
# Use 3 different colours
# Write a message that is school safe and does not have anyone’s personal information (including names)

# LEVEL 4
# Everything listed in level 3 
# Use at least 4 different font styles
# Use 4 different colours

# LEVEL 4+
# Everything listed in level 4
# Use a custom downloaded font
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Text & Fonts
# 
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to github when finished
# 
# Good luck!
#-----------------------------------------------------------------------------#



#-------------------Setup-----------------------------------------------------#
import pygame
pygame.init ()

window = pygame.display.set_mode((720, 470))
clock = pygame.time.Clock()
#----------------------------------------#


#----------Declaring Colors---------------------------------------------------#
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
#-----------------------------------------#


#---------Declaring width and Height------------------------------------------#
windowWidth = 720
windowHeight = 720
#-----------------------------------------#


#---------Game Loop-----------------------------------------------------------#
running = True
while running:
#----------------------------------------#


#-------------------------------EVENTS----------------------------------------# 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    window.fill(WHITE)
#-----------------------------------------#

#-----------------------------SHAPES-------------------------------------#

#------------------LIVE CODE--------------#

    pygame.draw.rect(window, GREEN, (100,70,120,100)) #Draws Rectangle

    pygame.draw.polygon(window, BLACK, ((235, 60),(400, 80),(300,160))) #Draws Triangle

    pygame.draw.circle(window, BLUE, (480, 60), 60) #Draws Circle

    pygame.draw.polygon(window, RED, ((600, 60), (660, 90), (700,160), (580, 160))) #Draws Trapezoid

#----------------------------------------#

#----------------LOVE CODE-------------------#

    pygame.draw.cicle()
    pygame.draw.rect(window, RED, (100,180,60,50))
    pygame.draw.polygon()
    pygame.draw.rect()

#------------------------------------------#

#------------LAUGH CODE--------------------#

    pygame.draw.rect(window, BLUE, (100,y,120,100))
    pygame.draw.polygon()
    pygame.draw.polygon()
    pygame.draw.circle ()
    pygame.draw.rect ()
                     

#------------------------------------------#

#---------Display-------------------------------------------------------------#
    pygame.display.flip()
    clock.tick(60)
#----------------------------------------#
   
