
import math
from pygame_functions import *


# define a main function
def cars():
    done = False
    x = 20
    y= 20
    o = 30
    p = 30
    speed = 2
    speed_2 = 2
    clock = pygame.time.Clock()
    viper = makeSprite('Black_viper.png')
    transformSprite(viper,90, .1)
    popo = makeSprite('cool_car.png')
    transformSprite(popo,90, .1)
    angle = 0
    angle_dos = 0
    while not done:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        done = True
        showSprite(viper)
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
        showSprite(popo)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_e]: speed_2+=.25
        if pressed[pygame.K_r]: speed_2-=.25
        if pressed[pygame.K_w]:
            o +=speed_2* math.cos(angle_dos*math.pi/180)
            p += speed_2* math.sin(angle_dos*math.pi/180)
        if pressed[pygame.K_s]:
            o -=speed_2* math.sin(angle_dos*math.pi/180)
            p -=speed_2* math.cos(angle_dos*math.pi/180)
        if pressed[pygame.K_a]: 
            angle_dos+= -4
            transformSprite(popo, angle_dos+90, .1)
        if pressed[pygame.K_d]: 
            angle_dos+= 4
            transformSprite(popo, angle_dos+90, .1)
        if o > 900:
            o = 880
        if o < 0:
            o = 20
        if p > 600:
            p= 580
        if p < 0:
            p= 20
        moveSprite(popo,o,p)
        angle_dos = angle_dos%360
        angle = angle%360

        # if is_blue: color = (0, 128, 255)
        # else: color = (255, 100, 0)
        # pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10)

        clock.tick(60)

    
    
def main():
    screenSize(1000,560)
    setBackgroundImage('racetrack.png')
    cars()
   

        
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()