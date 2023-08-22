import pygame

pygame.init()
win = pygame.display.set_mode((600, 400))

x = 10
run = True
while run:
    pygame.time.delay(60)
    win.fill((255,255,0))
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= 25
    if keys[pygame.K_RIGHT]:
        x += 25
        
        
    pygame.draw.rect(win, (255,0,0), (x,10,100,30))
    
    
    
    
    #if x < 475:
        #x += 25
        #pygame.draw.rect(win, (255,0,0), (x,10,100,30))
        #pygame.display.update()


    #if x > 475:
        #x -= 25
        
        pygame.display.update()
    
    
    
    

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            
            

pygame.quit()