
import math
from pygame_functions import *
from tutorial import *


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
            
        my_map = create_map()
        draw_map(my_map)
        showSprite(viper)
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_m]: speed-=.25
        if pressed[pygame.K_UP]:
            speed+=.5
            x +=speed* math.cos(angle*math.pi/180)
            y += speed* math.sin(angle*math.pi/180)
        if pressed[pygame.K_DOWN]:
            y -=speed* math.sin(angle*math.pi/180)
            x -=speed* math.cos(angle*math.pi/180)
        if pressed[pygame.K_LEFT]: 
            angle += -7
            transformSprite(viper, angle+90, .1)
        if pressed[pygame.K_RIGHT]: 
            angle+= 7
            transformSprite(viper, angle+90, .1)

        if x > 1200:
            x = 1100
            speed-=10
        if x < 0:
            x = 20
            speed-=10
        if y > 900:
            y= 880
            speed-=10
        if y < 0:
            y= 20
            speed-=10
        moveSprite(viper,x,y)
        showSprite(popo)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_r]: speed_2-=.25
        if pressed[pygame.K_w]:
            speed_2+=.5
            o +=speed_2* math.cos(angle_dos*math.pi/180)
            p += speed_2* math.sin(angle_dos*math.pi/180)
        if pressed[pygame.K_s]:
            p -=speed_2* math.sin(angle_dos*math.pi/180)
            o -=speed_2* math.cos(angle_dos*math.pi/180)
        if pressed[pygame.K_a]: 
            angle_dos+= -7
            transformSprite(popo, angle_dos+90, .1)
        if pressed[pygame.K_d]: 
            angle_dos+= 7
            transformSprite(popo, angle_dos+90, .1)
        if o > 1200:
            o = 1100
            speed_2-=10
        if o < 0:
            o = 20
            speed_2-=10
        if p > 900:
            p= 880
            speed_2-=10
        if p < 0:
            p= 20
            speed_2-=10
        moveSprite(popo,o,p)
        angle_dos = angle_dos%360
        angle = angle%360
        if touching(viper,popo):
            x+=10
            y+=10
            o-=10
            p-=10
            speed -= 10
            speed_2-=10

            # makeLabel(text, fontSize, xpos, ypos, fontColour='black', font='Arial', background='clear')
        if speed < 0:
            speed = 1 
        if speed_2 < 0:
            speed_2 = 1
        if speed > 30:
            speed = 30
        if speed_2 > 20:
            speed_2 = 20
        if my_map[int(y//20)][int(x//20)].slow_down and speed > 5:
            speed-=1 
        if my_map[int(p//20)][int(o//20)].slow_down and speed_2 > 5:
            speed_2-=1


        


        # if is_blue: color = (0, 128, 255)
        # else: color = (255, 100, 0)
        # pygame.draw.rect(screen, color, pygame.Rect(x, y, 10, 10)

        clock.tick(60)

    
    
def main():
    screenSize(1200,900)
    cars()
   

        
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()