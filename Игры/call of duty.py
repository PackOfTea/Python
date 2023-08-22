import pygame
import random

WIDTH = 400
HEIGHT = 550
FPS = 30

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()



class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mario/EN0F.gif")
        self.image = pygame.transform.scale(self.image, (50,38))
        #self.image.set_colorkey(BLACK)
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.jmp = False
        self.jc = 0
        
    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.speedx = -10    
            
        if keys[pygame.K_RIGHT] and self.rect.right < 400:
            self.speedx = 10
            
        self.rect.x += self.speedx
                
        if keys[pygame.K_SPACE]:
            if len(all_bull.sprites()) < 15:
                bull = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bull)
                all_bull.add(bull)
        
        if keys[pygame.K_UP]:
            self.jmp = True
            
        if self.jmp:
            if self.jc < 3:
                self.rect.y -= 30
                self.jc += 1
            elif 3 <= self.jc < 6:
                self.rect.y += 30
                self.jc += 1
            else:
                self.jmp = False
                self.jc = 0
                
                

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        
        
    def update(self):
        self.rect.y -= 15
        if self.rect.bottom < 0:
            pygame.draw.circle(screen, (255,255,0), (self.rect.centerx, self.rect.bottom), 20)
            self.kill()
            

class Targ(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mario/left5.png").convert()
        self.image = pygame.transform.scale(self.image, (30,33))
        self.image.set_colorkey(WHITE)
        #self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.top = random.randrange(10,300)
        self.rect.left = random.randrange(WIDTH, WIDTH + 300)
        
    def update(self):
        self.rect.x -= 10
        if self.rect.left < 0:
            self.rect.left = WIDTH



            
            


background = pygame.image.load("mario/Spyfall.png").convert()



all_sprites = pygame.sprite.Group()
all_bull = pygame.sprite.Group()
all_tars = pygame.sprite.Group()

player = Player()

all_sprites.add(player)
for i in range (5):
    target = Targ()
    all_sprites.add(target)
    all_tars.add(target)
    
    
running = True
while running:
    
    clock.tick(FPS)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            
    screen.fill(WHITE)
    
    all_sprites.update()
    hits = pygame.sprite.groupcollide(all_tars, all_bull, True, True)
    #for it in hits:
        #all_hits.add()
    all_sprites.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()