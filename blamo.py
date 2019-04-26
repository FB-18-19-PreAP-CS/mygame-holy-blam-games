import pygame

from pygame_functions import *

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
    image = pygame.image.load('Black_viper.png')
    while not done:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        done = True
        
        # pygame.display.flip()
        # if is_blue: 
        #     color = (0, 128, 255)
        # else: 
        #     color = (255, 100, 0)
        screen.blit(image,(x,y))
        
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     is_car = pygame.image.load('Audi.png')
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_v]: speed+=.25
        if pressed[pygame.K_c]: speed-=.25
        if pressed[pygame.K_UP]: y -= speed 
        if pressed[pygame.K_DOWN]:y += speed
        if pressed[pygame.K_LEFT]: 
            x -= speed 
            rotateSprite(image, 3)
            
        if pressed[pygame.K_RIGHT]: 
            x += speed

        if x > 900:
            x = 880
        if x < 0:
            x = 20
        if y > 600:
            y= 580
        if y < 0:
            y= 20
        # if is_blue: color = (0, 128, 255)
        # else: color = (255, 100, 0)
        # pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10))
        
        pygame.display.flip()
        screen.fill((0, 0, 0))

        clock.tick(60)

        
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()