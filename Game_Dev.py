import pygame
import os
# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 740))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
running = True
dt = 0
end= 0
thelist = []
os.system(".\winMain.exe")
# os.system("./main.exe")
file = open("main.txt", "r")
content = file.read()
won = 0.5
ans = int(content[0])*10+int(content[1])
for k in range(3, 67):
    thelist.append(int(content[k]))
file.close()
print(thelist)
Headimg = pygame.image.load("rsc/Head.png")
Tailimg = pygame.image.load("rsc/Tail.png")
Keyimg = pygame.image.load("rsc/Key.png")
j_ans = ans//8+1
i_ans = ans%8+1
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
button_rect = pygame.Rect(8+(i_ans-1)*88, 8+(j_ans-1)*88, 88 , 88)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                won =1
            else:
                won = 0
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
    if end:
        pygame.time.wait(3000)
        running = 0
    if won==1:
        pygame.draw.polygon(screen, "#000000",  [(8+(i_ans-1)*88, 8+(j_ans-1)*88), (96+(i_ans-1)*88, 8+(j_ans-1)*88), (96+(i_ans-1)*88, 96+(j_ans-1)*88), (8+(i_ans-1)*88, 96+(j_ans-1)*88)])
        rect = Keyimg.get_rect()
        rect.topleft = (8+(i_ans-1)*88, 8+(j_ans-1)*88) 
        screen.blit(Keyimg, rect)
        screen.blit(font.render('You Won!',True,"#FFFFFF"),(323.5,720))
        end = 1
    if won==0:
        screen.blit(font.render('You Lost!',True,"#FFFFFF"),(321,720))
        end = 1
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()