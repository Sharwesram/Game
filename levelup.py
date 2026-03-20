import pygame
import random
pygame.init()
sw,sl=700,700
ms=10
fs=72
bg=pygame.transform.scale(pygame.image.load("yl.png"),(sw,sl))
class sprite(pygame.sprite.Sprite):
    def __init__(self,color,w,l):
      super().__init__()
      self.image=pygame.Surface([w,l])
      self.image.fill(pygame.Color("yellow"))
      pygame.draw.rect(self.image,color,pygame.Rect(0,0,w,l))
      self.rect=self.image.get_rect()
    def move(self,x_c,y_c):
       self.rect.x=max(min(self.rect.x +x_c,sw-self.rect.width),0)
       self.rect.y=max(min(self.rect.y +y_c,sl-self.rect.height),0)
screen=pygame.display.set_mode((sw,sl))
pygame.display.set_caption("Sprite collision")
s=pygame.sprite.Group()
s1=sprite((pygame.Color("red")),20,30)
s2=sprite((pygame.Color("black")),20,30)
s1.rect.x,s1.rect.y=random.randint(0,sw-s1.rect.width),random.randint(0,sl-s1.rect.height)
s.add(s1)
s2.rect.x,s2.rect.y=random.randint(0,sw-s2.rect.width),random.randint(0,sw-s2.rect.height)
s.add(s2)
r=True
w=False
clock=pygame.time.Clock()
while r:
       for event in pygame.event.get():
          if event.type==pygame.QUIT:
            pygame.quit()
       if not w:
        press=pygame.key.get_pressed()
        x_c=(press[pygame.K_RIGHT]-press[pygame.K_LEFT])*ms
        y_c=(press[pygame.K_DOWN]-press[pygame.K_UP])*ms
        s1.move(x_c,y_c)
       if s1.rect.colliderect(s2):
          s.remove(s2)
          w=True
       screen.blit(bg,(0,0))
       s.draw(screen)
       if w:
          font=pygame.font.SysFont(None,fs)
          wt=font.render("you win!",True,pygame.Color("black"))
          screen.blit(wt,((sw-wt.get_width())//2,(sl-wt.get_height())//2))
       pygame.display.flip()
       clock.tick(90)        