# -----------------------------------------------------------------------------
# IMAGE LAB - IMAGE COLLAGE
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different images to create a collage
# You can repeat the same images must use other commands to change the look (example, tint)

# LEVEL 4
# Everything listed in level 3 
# Create a scene with images

# LEVEL 4+
# Everything listed in level 4
# Randomize or animate something

# Recommended Lessons:
# P5.js intro
# P5.js drawing
# P5.js colour
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to githun when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

#--------------------------------SETUP----------------------------------------
import pygame
pygame.init()

windowWidth = 640
windowHeight = 640
window =pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  #will allow us to set framerate

#-------------------------Images------------------------------------------

elevenPic = pygame.image.load("images/Eleven copy.jpg")
maxPic = pygame.image.load("images/Max Mayfield copy.jpg")
willPic = pygame.image.load("images/Will Byers.jpg")
stPic = pygame.image.load("images/STPIC copy.jpg")



# -----------------------------GAME LOOP--------------------------------------

frame_count = 0
running = True
while True:
    # --------EVENTS--------------------------
    ev = pygame.event.poll()    # Look for any event
    if ev.type == pygame.QUIT:  # windowow close button clicked?
        break                   # leave game loop
    window.fill((255,255,255))
    frame_count += 1
    
    
    #----------Eleven Pic--------------#
    if frame_count > 0:
        window.blit(elevenPic, (0,0))
        red_tint = pygame.Surface(elevenPic.get_size(), pygame.SRCALPHA)
        red_tint.fill((255,0,0,100))
        window.blit(red_tint, (0,0))

    #----------Max Pic--------------#
    if frame_count > 120:
        window.blit(maxPic, (0,0))
        blue_tint = pygame.Surface(maxPic.get_size(), pygame.SRCALPHA)
        blue_tint.fill((0,0,255,100))
        window.blit(blue_tint, (0,0))

    #---------- Will Pic--------------#
    if frame_count > 240:
        window.blit(willPic, (0,0))
        green_tint = pygame.Surface(willPic.get_size(), pygame.SRCALPHA)
        green_tint.fill((0,0,255,100))
        window.blit(green_tint, (0,0))

    #----------ST Pic--------------#
    if frame_count > 360:
        window.blit(stPic, (0,0))
        purple_tint = pygame.Surface(stPic.get_size(), pygame.SRCALPHA)
        purple_tint.fill((255,0,255,100))
        window.blit(purple_tint, (0,0))


    # -------SHOW THE FRAME TO THE USER-------
    pygame.display.flip()
    clock.tick(60) #Force frame rate to 60fps or lower


pygame.quit()


 