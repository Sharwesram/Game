import pygame
import random
pygame.init()
random_color=((random.randint(50,251)),(random.randint(50,251)),(random.randint(50,251)))


sprite_color_change1=pygame.USEREVENT  +1
sprite_color_change1=pygame.USEREVENT  +1 
bg_change=pygame.USEREVENT+2

random_color=((random.randint(50,251)),(random.randint(50,251)),(random.randint(50,251)))
random_color1=((random.randint(50,251)),(random.randint(50,251)),(random.randint(50,251)))

class sprite1(pygame.sprite.Sprite):
    def __init__(self,color,w,l):
        super().__init__()
        self.image=pygame.Surface([w,l])
        self.image.fill(color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        bh=False
        if self.rect.left<=0 and self.rect.right>=700:
            self.velocity[0]=-self.velocity[0]

        if self.rect.top <=0 and self.rect.bottom>=500:
            self.velocity[1]=-self.velocity[1]
            bh = True
        if bh:
            pygame.event.post(pygame.event.Event(sprite_color_change1))
            pygame.event.post(pygame.event.Event(bg_change))
    def c(self):
            self.image.fill(((random.randint(50,251)),(random.randint(50,251)),(random.randint(50,251))))
def bg():
     global b
     b=((random.randint(50,251)),(random.randint(50,251)),(random.randint(50,251)))
a=pygame.sprite.Group()
s=sprite1((pygame.Color("yellow")),20,30)
s1=sprite1((pygame.Color("yellow")),20,30)
s.rect.x=random.randint(0,680)
s.rect.y=random.randint(0,480)
s1.rect.x=random.randint(0,680)
s1.rect.y=random.randint(0,480)

a.add(s)
screen=pygame.display.set_mode((700,500))
b_g=random_color1
screen.fill(b_g)
exit= False
clock=pygame.time.Clock()
while not exit:
     for event in pygame.event.get():
          if event.type==pygame.QUIT:
               pygame.quit()
          elif event.type==sprite_color_change1:
               s.c()
          elif event.type==bg_change:
               bg()
     a.update()
     screen.fill(b_g)
     a.draw(screen)
     pygame.display.flip()
     clock.tick(300)
pygame.quit()
