import pygame

pygame.init()

screen=pygame.display.set_mode((700,500))
white=(255,255,255)
green=(0,255,0)
# blue=(0,125,225)
# pygame.draw.rect(screen,blue,pygame.Rect(30,60,30,60))
# screen.fill(white)
# pygame.draw.circle(screen,green,(300,300),50)
# pygame.draw.circle(screen,green,(200,200),25,1)
colors={"red":pygame.Color("red"),"yellow":pygame.Color("yellow"),"blue":pygame.Color("blue"),"green":pygame.Color("green")}
c=colors["yellow"]
clock=pygame.time.Clock()
x,y=50,50
while True:
    
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
         pygame.quit()
    press=pygame.key.get_pressed()
    if press[pygame.K_LEFT]:x-=3
    if press[pygame.K_RIGHT]:x+=3
    if press[pygame.K_UP]:y-=3
    if press[pygame.K_DOWN]:y+=3
    x=min(max(0,x),350)
    y=min(max(0,y),350)
    if x==0:c=colors["blue"]
    elif x==340:colors["green"]
    elif y==0:colors["red"]
    elif y==340:colors["yellow"]
    pygame.draw.rect(screen,c,(x,y,60,60),0,0)
    clock.tick(90)   
    
    pygame.display.flip()

