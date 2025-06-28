# Example file showing a circle moving on screen
import pygame
import os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
dt = 0
thelist = []
os.system(".\winMain.exe")
file = open("main.txt", "r")
content = file.read()
ans = int(content[0])*10+int(content[1])
for k in range(3, 67):
    thelist.append(int(content[k]))
file.close()
print(thelist)
Headimg = pygame.image.load("Head.png")
Tailimg = pygame.image.load("Tail.png")

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    for i in range(1,9):
        for j in range(1,9):
            if ((i+j)%2==0):
                color = "#769656"
            else:
                color = "#008000"
            pygame.draw.polygon(screen, color,  [(8+(i-1)*88, 8+(j-1)*88), (96+(i-1)*88, 8+(j-1)*88), (96+(i-1)*88, 96+(j-1)*88), (8+(i-1)*88, 96+(j-1)*88)])
            if thelist[8*(j-1)+i-1]==1:
                rect = Headimg.get_rect()
                rect.topleft = (8+(i-1)*88, 8+(j-1)*88) 
                screen.blit(Headimg, rect)
            else:
                rect = Tailimg.get_rect()
                rect.topleft = (8+(i-1)*88, 8+(j-1)*88) 
                screen.blit(Tailimg, rect)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()