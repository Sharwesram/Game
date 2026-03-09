import pygame

pygame.init()

screen=pygame.display.set_mode((640,480))

pygame.display.set_caption("My first game screen")

color=(0,125,255)
w=(0,0,0)
screen.fill(pygame.Color("white"))

pygame.draw.rect(screen,color,pygame.Rect(80,70,80,70))
text=pygame.font.Font(None,36).render("Created by Sharwesram!",True,pygame.Color("Yellow"))
place=text.get_rect(center=(320,210))
running=True
while running:
    screen.blit(text,place)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running=False
    pygame.display.flip()
