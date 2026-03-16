import pygame
import random
pygame.init()

sprite_color_change=pygame.USEREVENT+1
bg_color=pygame.USEREVENT+2
y=pygame.Color("yellow")
r=pygame.Color("red")
lb=pygame.Color("lightblue")
o=pygame.Color("orange")
g=pygame.Color("grey")
class sprite(pygame.sprite.Sprite):
    def __init__(self,color,l,w):
        super().__init__()
        self.image=pygame.Surface([w,l])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        bh=False
        if self.rect.left  <=0 or self.rect.right >=700:
            self.velocity[0]=-self.velocity[0]
            bh=True
        if self.rect.top  <=0 or self.rect.bottom >=500:
            self.velocity[1]=-self.velocity[1]
            bh=True
        if bh :
            pygame.event.post(pygame.event.Event(sprite_color_change))
            pygame.event.post(pygame.event.Event(bg_color))
    def c(self):
        self.image.fill(random.choice([y,r,lb,o,g]))
def bg():
        global b_g
        b_g=random.choice([y,r,lb,o,g])
a=pygame.sprite.Group()
s=sprite(y,20,30)
s.rect.x=random.randint(0,680)   
s.rect.y=random.randint(0,480)
a.add(s)
screen=pygame.display.set_mode((700,500))
b_g=r
screen.fill(b_g)
exit=False
clock=pygame.time.Clock()
while not exit:
     for events in pygame.event.get():
          if events.type==pygame.QUIT:
               exit = True
          elif events.type==sprite_color_change:
               s.c()
          elif events.type==bg_color:
               bg()
     a.update()
     screen.fill(b_g)
     a.draw(screen)
     pygame.display.flip()
     clock.tick(240)
pygame.quit()