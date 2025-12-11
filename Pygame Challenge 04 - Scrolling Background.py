# -----------------------------------------------------------------------------
# ANIMATION LAB - SCROLLING BACKGROUND WITH PLANE
# -----------------------------------------------------------------------------

import pygame
pygame.init()

# ----------------------SETUP---------------------------------
windowWidth = 640
windowHeight = 300
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()  # allows us to control framerate

# ----------------------LOAD IMAGES---------------------------
background = pygame.image.load("images SBG/Scrolling background.jpg").convert()
plane = pygame.image.load("images SBG/plane.png").convert_alpha()  # plane with transparency

# Optional: Resize plane if too big
plane = pygame.transform.scale(plane, (80, 40))  # adjust width & height

# ----------------------INITIAL POSITIONS---------------------
bg_speed = 5
plane_speed = 1

bg_x1 = 0
bg_x2 = background.get_width()

plane_x = 0  # starting X position for plane
plane_y = 100  # adjust Y position

# ----------------------GAME LOOP-----------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------------------UPDATE POSITIONS----------------------
    # Background scrolls left
    bg_x1 -= bg_speed
    bg_x2 -= bg_speed
    if bg_x1 <= -background.get_width():
        bg_x1 = background.get_width()
    if bg_x2 <= -background.get_width():
        bg_x2 = background.get_width()

    # Plane moves right
    plane_x += plane_speed
    if plane_x > windowWidth:  # wrap around
        plane_x = -plane.get_width()

    # -------------------DRAW----------------------
    window.blit(background, (bg_x1, 0))
    window.blit(background, (bg_x2, 0))
    window.blit(plane, (plane_x, plane_y))

    pygame.display.flip()
    clock.tick(60)  # 60 fps

pygame.quit()
