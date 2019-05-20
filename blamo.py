
import math
from pygame_functions import *
from tutorial import *
import time


# define a main function
def cars():
    car_passed_check_1 = False
    car_passed_check_2 = False
    car_passed_check_3 = False
    car2_passed_check_1 = False
    car2_passed_check_2 = False
    car2_passed_check_3 = False
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
    crash = makeSound('car crash.ogg')
    accelerate = makeSound('racecar_sound.ogg')
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
            playSound(accelerate)
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
        if pressed[pygame.K_q]:
            hideLabel(black_laps)
            hideLabel(orange_laps)
            killSprite(viper)
            killSprite(popo)
            break

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
            playSound(accelerate)
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
            playSound(crash)
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
        if my_map[int(y//20)][int(x//20)].checkpoint[0] == True and my_map[int(y//20)][int(x//20)].checkpoint[1] == 1:
            car_passed_check_1 = True
        if my_map[int(y//20)][int(x//20)].checkpoint[0] == True and my_map[int(y//20)][int(x//20)].checkpoint[1] == 2:
            car_passed_check_2 = True
        if my_map[int(y//20)][int(x//20)].checkpoint[0] == True and my_map[int(y//20)][int(x//20)].checkpoint[1] == 3:
            car_passed_check_3 = True


        if my_map[int(y//20)][int(x//20)].finish_line and car_passed_check_1 == True and car_passed_check_2 == True and car_passed_check_3 == True:
            lap_count+=1
            car_passed_check_1 = False
            car_passed_check_2 = False
            car_passed_check_3 = False
        if my_map[int(p//20)][int(o//20)].checkpoint[0] == True and my_map[int(p//20)][int(o//20)].checkpoint[1] == 1:
            car2_passed_check_1 = True
        if my_map[int(p//20)][int(o//20)].checkpoint[0] == True and my_map[int(p//20)][int(o//20)].checkpoint[1] == 2:
            car2_passed_check_2 = True
        if my_map[int(p//20)][int(o//20)].checkpoint[0] == True and my_map[int(p//20)][int(o//20)].checkpoint[1] == 3:
            car2_passed_check_3 = True
        if my_map[int(p//20)][int(o//20)].finish_line and car2_passed_check_1 == True and car2_passed_check_2 == True and car2_passed_check_3 == True:
            lap_count_2+=1
            car2_passed_check_1 = False
            car2_passed_check_2 = False
            car2_passed_check_3 = False
        if lap_count_2 > 6:
            showLabel(contine_label)
            if keyPressed('p'):
                lap_count = 0
                lap_count_2 = 0
                x = 20
                y= 20
                o = 30
                p = 30
                hideLabel(contine_label)
                


        if lap_count > 6:
            showLabel(contine_label_2)
            if keyPressed('p'):
                lap_count = 0
                lap_count_2 = 0
                x = 20
                y= 20
                o = 30
                p = 30
                hideLabel(contine_label_2)
    


        clock.tick(60)
def bumper_cars():
    tag_count = 0
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
    tagged = makeLabel(f'Black car Tagged!', 40, 100, 100, fontColour='white', font='Gugi', background='clear')
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        my_map = create_map_tag()
        setBackgroundImage( 'tag_map.png' )
        showLabel(tagged)
        
        
        showSprite(viper)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_m]: speed-=.25
        if pressed[pygame.K_UP]:
            playSound(accelerate)
            speed+=.5
            x +=speed* math.cos(angle*math.pi/180)
            y += speed* math.sin(angle*math.pi/180)
        if pressed[pygame.K_DOWN]:
            y -=speed* math.sin(angle*math.pi/180)
            x -=speed* math.cos(angle*math.pi/180)
        if pressed[pygame.K_q]:
            killSprite(viper)
            killSprite(popo)
            hideLabel(tagged)
            break
        if pressed[pygame.K_LEFT]: 
            angle += -7
            transformSprite(viper, angle+90, .3)
        if pressed[pygame.K_RIGHT]: 
            angle+= 7
            transformSprite(viper, angle+90, .3)
        if x > 1100:
            x = 1050
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
            playSound(accelerate)
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
            playSound(crash)
            x+=10
            y+=10
            o-=10
            p-=10
            speed -= 10
            speed_2-=10
            if tag_count % 2 == 0:
                changeLabel(tagged,'Orange Car tagged', fontColour='white', background='Black')
            else:
                changeLabel(tagged,'Black Car tagged', fontColour='white', background='Black')
            tag_count+=1
            # makeLabel(text, fontSize, xpos, ypos, fontColour='black', font='Arial', background='clear')
        if speed < 0:
            speed = 1 
        if speed_2 < 0:
            speed_2 = 1
        if speed > 40:
            speed =40
        if speed_2 > 40:
            speed_2 = 40
        if my_map[int(y//20)][int(x//20)].extra_slow_down and speed > 5:
            speed-=4
        if my_map[int(p//20)][int(o//20)].extra_slow_down and speed_2 > 5:
            speed_2-=4
        if my_map[int(y//20)][int(x//20)].pseudo_wall and speed > 5:
            speed=1
        if my_map[int(p//20)][int(o//20)].pseudo_wall and speed_2 > 5:
            speed_2=1

def main():
    welcome_label = makeLabel(f'Hello Welcome to BLAMO!', 30, 5, 5, fontColour='red', font='Gugi', background='clear')
    decide_label = makeLabel(f'Press "a" for Racing, "b" for Bumper cars, or "q" to Quit', 30, 50, 50, fontColour='red', font='Gugi', background='clear')
    goodbye_label =makeLabel(f'Shutting down', 60, 5, 5, fontColour='red', font='Gugi', background='clear')
    setBackgroundImage( 'start_screen.png' )
    while True:
        showLabel(welcome_label)
        showLabel(decide_label)
        
        if keyPressed("a"):
            hideLabel(welcome_label)
            hideLabel(decide_label)
            cars()
        if keyPressed("b"):
            hideLabel(welcome_label)
            hideLabel(decide_label)
            bumper_cars()
        if keyPressed("q"):
            showLabel(goodbye_label)
            hideLabel(welcome_label)
            hideLabel(decide_label)
            time.sleep(1)
            break
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__" :
    # call the main function
    screenSize(1200,900)
    main()