import pygame

pygame.init()
win = pygame.display.set_mode((600, 400))

b = 0
x = 0
run = True
while run:
    pygame.time.delay(60)
    win.fill((255,255,0))
    
    if b == 0:
        x += 25
        if x == 500:
            b=1
        
        pygame.draw.rect(win, (255,0,0), (x,10,100,30))
        pygame.display.update()


    if b == 1:
        x -= 25
        
        
        if x == 0:
            b = 0        
    
        pygame.draw.rect(win, (255,0,0), (x,10,100,30))
        pygame.display.update()    
    
    

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            
            

pygame.quit()