
import math
from pygame_functions import *

# define a main function

def main():
    done = False
    x= 20
    y = 20
    speed = 2
    clock = pygame.time.Clock()
    screenSize(1000,560)
    setBackgroundImage('racetrack.png')
    viper = makeSprite('Black_viper.png')
    transformSprite(viper,90, .1)
    angle = 0
    while not done:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        done = True
        
        # pygame.display.flip()
        # if is_blue: 
        #     color = (0, 128, 255)
        # else: 
        #     color = (255, 100, 0)
        showSprite(viper)
        
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     is_car = pygame.image.load('Audi.png')
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_v]: speed+=.25
        if pressed[pygame.K_c]: speed-=.25
        if pressed[pygame.K_UP]:
            x +=speed* math.cos(angle*math.pi/180)
            y += speed* math.sin(angle*math.pi/180)
        if pressed[pygame.K_DOWN]:
            y -=speed* math.sin(angle*math.pi/180)
            x -=speed* math.cos(angle*math.pi/180)
        if pressed[pygame.K_LEFT]: 
            angle += -4
            transformSprite(viper, angle+90, .1)
        if pressed[pygame.K_RIGHT]: 
            angle+= 4
            transformSprite(viper, angle+90, .1)

        if x > 900:
            x = 880
        if x < 0:
            x = 20
        if y > 600:
            y= 580
        if y < 0:
            y= 20
        moveSprite(viper,x,y)
        angle = angle%360

        # if is_blue: color = (0, 128, 255)
        # else: color = (255, 100, 0)
        # pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10)

        clock.tick(60)

        
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()