import pygame
from pygame import draw

# define a main function

def main():
    speed = 2
    x= 30
    y= 30
    done = False
    pygame.display.set_caption("Blamo")
    screen = pygame.display.set_mode((900,600))
    is_blue= True
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()
        if is_blue: 
            color = (0, 128, 255)
        else: 
            color = (255, 100, 0)
        blu = pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_v]: speed+=.25
        if pressed[pygame.K_c]: speed-=.25
        if pressed[pygame.K_UP]: y -= speed 
        if pressed[pygame.K_DOWN]:y += speed
        if pressed[pygame.K_LEFT]: x -= speed 
            
        if pressed[pygame.K_RIGHT]: x += speed

        if x > 1900:
            x = 1800
        if x < 0:
            x = 120
        if y > 1000:
            y= 880
        if y < 0:
            y= 120
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
        
        pygame.display.flip()
        clock.tick(60)

        
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()