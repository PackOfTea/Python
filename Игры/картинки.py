import pygame

WIDTH = 400
HEIGHT = 550
FPS = 30

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mario/left1.png")
        self.rect = self.image.get_rect()
        self.rect.centery = (WIDTH / 2)
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < 400:
            self.rect.x += 5
                
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

background = pygame.image.load("mario/Spyfall.png").convert()
p = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(p)

running = True
while running:
    
    clock.tick(FPS)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
    screen.fill(WHITE)
    screen.blit(background, [0,0])
    
    all_sprites.update()
    all_sprites.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()