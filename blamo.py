
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
    lap_count= 0
    lap_count_2=0
    clock = pygame.time.Clock()
    viper = makeSprite('Black_viper.png')
    transformSprite(viper,90, .3)
    popo = makeSprite('cool_car.png')
    transformSprite(popo,90, .3)
    angle = 0
    angle_dos = 0
    black_laps = makeLabel(f'Black car Lap {lap_count}', 18, 100, 100, fontColour='white', font='Gugi', background='Black')
    orange_laps = makeLabel(f'Orange car Lap {lap_count_2}', 18, 300, 100, fontColour='white', font='Gugi', background='Black')
    while not done:
        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        done = True
        
        my_map = create_map()
        setBackgroundImage( 'background.png' )
        showLabel(black_laps)
        showLabel(orange_laps)
        changeLabel(black_laps, f'Black car Lap {lap_count}', fontColour='white', background='Black')
        changeLabel(orange_laps, f'Orange car Lap {lap_count_2}', fontColour='white', background='Black')
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
            transformSprite(viper, angle+90, .3)
        if pressed[pygame.K_RIGHT]: 
            angle+= 7
            transformSprite(viper, angle+90, .3)
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
            transformSprite(popo, angle_dos+90, .3)
        if pressed[pygame.K_d]: 
            angle_dos+= 7
            transformSprite(popo, angle_dos+90, .3)
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
        if speed > 40:
            speed =40
        if speed_2 > 40:
            speed_2 = 40
        if my_map[int(y//20)][int(x//20)].slow_down and speed > 5:
            speed-=1 
        if my_map[int(p//20)][int(o//20)].slow_down and speed_2 > 5:
            speed_2-=1
        if my_map[int(y//20)][int(x//20)].finish_line:
            lap_count+=1
        if my_map[int(p//20)][int(o//20)].finish_line:
            lap_count_2 +=1
        clock.tick(60)
def main():
    screenSize(1200,900)
    cars()
   

        
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()