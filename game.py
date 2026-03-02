import pygame

pygame.init()

screen=pygame.display.set_mode((750,700))

# done=False

# while not done:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
            
#     pygame.display.flip()

pygame.display.set_caption("ADDING IMAGE TO THE BACKGROUND!")
background_image=pygame.transform.scale(pygame.image.load("image.png").convert(),(750,700))
image=pygame.transform.scale(pygame.image.load("image.png").convert_alpha(),(700,600))
abc=image.get_rect(center=(600//2,700//2-30))
text=pygame.font.Font(None,36).render("Hello World !",True,pygame.Color("black"))
a=text.get_rect(center=(600//2,700//2+110))
def game():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.blit(background_image,(0,0))
        screen.blit(image,abc)
        screen.blit(text,a)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__== "__main__":
    game()
