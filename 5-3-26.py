import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))
c=(58,58,58)
background=pygame.transform.scale(pygame.image.load("image.png").convert(),(500,500))
image=pygame.transform.scale(pygame.image.load("image.png").convert_alpha(),(300,300))
cer=image.get_rect(center=(600//2-30,700//2-115))
def game():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.blit(background,(0,0))
        screen.blit(image,cer)
        
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__== "__main__":
    game()
