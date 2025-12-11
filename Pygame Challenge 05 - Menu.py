# -------------------------Set Up---------------------------------#
import pygame
pygame.init()

#------------Window---------#
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Restaurant Game Menu")
#---------------------------#

#-----------Fonts------------#
font = pygame.font.SysFont("arial", 36)
big_font = pygame.font.SysFont("arial", 60)
#-----------------------------#

#----------Game State---------#
state = "HOME"
#-----------------------------#
#------------------------------------------------------------------#


#--------------------------------Buttons---------------------------#
home_buttons = [
    pygame.Rect(WIDTH//2 - 150, 280, 300, 70),  # Instructions
    pygame.Rect(WIDTH//2 - 150, 380, 300, 70),  # Choose Character
    pygame.Rect(WIDTH//2 - 150, 480, 300, 70)   # Kitchen
]

back_button = pygame.Rect(30, 30, 150, 60)

#--------Colors--------------#
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
DARKGRAY = (150,150,150)
#----------------------------#
#-------------------------------------------------------------------#


# -------------------------Screens----------------------------------#
home_bg = pygame.image.load("ImagesM/home_bg.jpg")
instructions_bg = pygame.image.load("ImagesM/Instructions_bg.png")
character_bg = pygame.image.load("ImagesM/character_bg.png")
kitchen_bg = pygame.image.load("ImagesM/kitchen_bg.png")
#-------------------------------------------------------------------#

# ------------------ Scaling images --------------------------------#
home_bg = pygame.transform.scale(home_bg, (WIDTH, HEIGHT))
instructions_bg = pygame.transform.scale(instructions_bg, (WIDTH, HEIGHT))
character_bg = pygame.transform.scale(character_bg, (WIDTH, HEIGHT))
kitchen_bg = pygame.transform.scale(kitchen_bg, (WIDTH, HEIGHT))
# -------------------------------------------------------------------#

#-------------------Game Loops---------------------------------------#
running = True
while running:
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

    # ---------------States---------------#
            if state == "HOME":
                if home_buttons[0].collidepoint(mx, my): #Checks if mouse clicks button
                    state = "INSTRUCTIONS"
                elif home_buttons[1].collidepoint(mx, my):
                    state = "CHARACTER"
                elif home_buttons[2].collidepoint(mx, my):
                    state = "KITCHEN"

            else:
                if back_button.collidepoint(mx, my):
                    state = "HOME"
    #------------------------------------#

    # ---------- DRAW SCREENS ----------#
    if state == "HOME":
        screen.blit(home_bg, (0,0))
        title = big_font.render("Welcome to Kitchen Craze!", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))

        labels = ["Instructions", "Choose Character", "Enter Kitchen"]
        for i, rect in enumerate(home_buttons):
            color = DARKGRAY if rect.collidepoint(mx,my) else GRAY
            pygame.draw.rect(screen, color, rect)
            text = font.render(labels[i], True, BLACK)
            screen.blit(text, text.get_rect(center=rect.center))

    elif state == "INSTRUCTIONS":
        screen.blit(instructions_bg, (0,0))
        pygame.draw.rect(screen, GRAY, back_button)
        screen.blit(font.render("Back", True, BLACK), back_button)

    elif state == "CHARACTER":
        screen.blit(character_bg, (0,0))
        pygame.draw.rect(screen, GRAY, back_button)
        screen.blit(font.render("Back", True, BLACK), back_button)

    elif state == "KITCHEN":
        screen.blit(kitchen_bg, (0,0))
        pygame.draw.rect(screen, GRAY, back_button)
        screen.blit(font.render("Back", True, BLACK), back_button)
    #------------------------------------#

    #-----------SHowing User-------------#
    pygame.display.flip()
    #------------------------------------#

pygame.quit()
#--------------------------------------------------------------------#
