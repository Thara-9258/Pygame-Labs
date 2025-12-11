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



#-------------------Setup----------------------------------------------------------------------------------#
import pygame
pygame.init ()

window = pygame.display.set_mode((780, 470))
clock = pygame.time.Clock()
#----------------------------------------------------------------------------------------------------------#


#----------Declaring Colors--------------------------------------------------------------------------------#
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
PALE = (232, 195, 146)
#----------------------------------------------------------------------------------------------------------#


#---------Declaring width and Height------------------------------------------------------------------------#
windowWidth = 780
windowHeight = 470
#-----------------------------------------------------------------------------------------------------------#


#---------Game Loop-----------------------------------------------------------------------------------------#
running = True
while running:
#-----------------------------------------------------------------------------------------------------------#


#-------------------------------EVENTS----------------------------------------------------------------------# 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       
    window.fill(PALE)
#-----------------------------------------------------------------------------------------------------------#

#-----------------------------SHAPES------------------------------------------------------------------------#

#------------------LIVE CODE--------------#

    pygame.draw.rect(window, GREEN, (100,70,120,100)) #Draws Rectangle

    pygame.draw.polygon(window, BLACK, ((235, 60),(400, 80),(300,160))) #Draws Triangle

    pygame.draw.circle(window, BLUE, (480, 60), 60) #Draws Circle

    pygame.draw.polygon(window, RED, ((600, 60), (660, 90), (700,160), (580, 160))) #Draws Trapezoid

#----------------------------------------#

#----------------LOVE CODE-------------------#

    pygame.draw.circle(window, BLUE, (250, 240), 80) #Draws Circle
    pygame.draw.rect(window, RED, (80,180,60,50)) #Draws Rectangle
    pygame.draw.polygon(window, GREEN, ((350,170), (500, 170), (540, 230), (350, 330))) #Draws Trapezoid

#------------------------------------------#

#------------LAUGH CODE--------------------#

    pygame.draw.rect(window, BLACK, (240,340,300,100))

#------------------------------------------#

#-----------------------------------------------------------------------------------------------------------#

#---------------------------------------FONTS----------------------------------------------------------------#

    font = pygame.font.Font('Christmas Buttermilk.otf', 106)
    Letter = "L"
    renderedText = font.render(Letter, 1, pygame.Color("blue"))
    window.blit(renderedText, (145,84))
    #prints letter "L" in Christmas Buttermilk font

    font = pygame.font.Font('Super Chiby.ttf', 80)
    Letter = "I"
    renderedText = font.render(Letter, 1, pygame.Color("green"))
    window.blit(renderedText, (290,64))
    #prints letter "I" in Super Chiby Font

    font = pygame.font.Font('JMH Typewriter-Black.otf', 80)
    Letter = "V"
    renderedText = font.render(Letter, 1, pygame.Color("red"))
    window.blit(renderedText, (450,24))
    #prints letter "V" in JMH Typewriter-Black Font

    font = pygame.font.Font('LEMON.otf', 80)
    Letter = "E"
    renderedText = font.render(Letter, 1, pygame.Color("green"))
    window.blit(renderedText, (610,64))
    #prints letter "E" in LEMON Font

    font = pygame.font.Font('Christmas Buttermilk.otf', 67)
    Letter = "L"
    renderedText = font.render(Letter, 1, pygame.Color("green"))
    window.blit(renderedText, (100,180))
    #prints letter "L" in Christmas Buttermilk font

    font = pygame.font.Font('LEMON.otf', 130)
    Letter = "O"
    renderedText = font.render(Letter, 1, pygame.Color("green"))
    window.blit(renderedText, (210,164))
    #prints letter "O" in LEMON Font

    font = pygame.font.Font('Super Chiby.ttf', 80)
    Letter = "V"
    renderedText = font.render(Letter, 1, pygame.Color("red"))
    window.blit(renderedText, (390,180))
    #prints letter "V" in Super Chiby Font

    font = pygame.font.Font('JMH Typewriter-Black.otf', 80)
    Letter = "E"
    renderedText = font.render(Letter, 1, pygame.Color("blue"))
    window.blit(renderedText, (580,200))
    #prints letter "E" in JMH Typewriter-Black Font

    font = pygame.font.Font('Christmas Calling-Personal Use.otf', 80)
    Letter = "LAUGH"
    renderedText = font.render(Letter, 1, pygame.Color("purple"))
    window.blit(renderedText, (300,355))
    #prints "LAUGH" in Chrisstmas Calling Font

#---------Display--------------------------------------------------------------------------------------------#
    pygame.display.flip()
    clock.tick(60)
#------------------------------------------------------------------------------------------------------------#

   
