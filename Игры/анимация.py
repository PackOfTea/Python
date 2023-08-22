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
        self.images_left = ["mario/left1.png", "mario/left2.png", "mario/left3.png", "mario/left4.png", "mario/left5.png"]
        self.images_right = ["mario/right1.png", "mario/right2.png", "mario/right3.png", "mario/right4.png", "mario/right5.png"]
        self.image = pygame.image.load(self.images_left[0])
        self.image = pygame.image.load(self.images_right[0])
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.c = 0
        self.kuda = ""
        
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            if self.c == len(self.images_left):
                self.c = 0
            self.image = pygame.image.load(self.images_left[self.c])
            self.image.set_colorkey(WHITE)
            self.c += 1
            self.rect.x -= 5
            self.kuda = "levo"
        elif self.kuda == "levo":
            if self.kuda == "levo":
                self.image = pygame.image.load(self.images_left[0])
                self.image.set_colorkey(WHITE)
            
        if keys[pygame.K_RIGHT] and self.rect.right < 400:
            if self.c == len(self.images_right):
                self.c = 0
            self.image = pygame.image.load(self.images_right[self.c])
            self.image.set_colorkey(WHITE)
            self.c += 1
            self.rect.x += 5
            self.kuda = "pravo"
        elif self.kuda == "pravo":
            if self.kuda == "pravo":
                self.image = pygame.image.load(self.images_right[0])
                self.image.set_colorkey(WHITE)
            
            
            
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