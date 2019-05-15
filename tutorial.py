import pygame
from pygame_functions import *
#import Pygame_Functions-master
#Tutorials Used:
# Pygame top down racing game - start of tutorial to get started - https://www.youtube.com/playlist?list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
#Rogue like tutorial (mostly Part 4) - https://www.youtube.com/watch?v=6XfQqFvJtts&list=PLKUel_nHsTQ1yX7tQxR_SQRdcOFyXfNAb
#
#sources
#
#
pygame.init()
map_width = 60
map_height = 45
cell_width = 20
cell_height = 20
dis_width = map_width * cell_width
dis_height = map_height * cell_height
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grass = pygame.image.load('red.png')
road = pygame.image.load('road.png')
finish = pygame.image.load('finish_line.png')
check = pygame.image.load('blue.png')
pseudo = pygame.image.load('pseudo.png')
gameDisplay = pygame.display.set_mode((dis_width,dis_height))
class Tile:

    def __init__(self,slow_down,finish_line,block_path,checkpoint,extra_slow_down,pseudo_wall):
        self.slow_down = slow_down
        self.finish_line = finish_line
        self.block_path = block_path
        self.checkpoint = checkpoint
        self.extra_slow_down = extra_slow_down
        self.pseudo_wall = pseudo_wall


def create_map_tag():
    tag_map = [[ Tile(False,False,False,(False,0),False,False) for x in range(0,map_width)] for y in range(0,map_height)]


    for y in range(10,15):
        for x in range(20,25):
            tag_map[y][x].extra_slow_down = True
            tag_map[y+23][x].extra_slow_down = True
            tag_map[y][x+26].extra_slow_down = True
            tag_map[y+22][x+25].extra_slow_down = True
            tag_map[y+12][x-14].extra_slow_down = True
            if x < 23 and y < 13: 
                tag_map[22+y-10][35+x-20].pseudo_wall = True

    return tag_map


def create_map():
    mymap = [[ Tile(False,False,False,(False,0),False,False) for x in range(0,map_width)] for y in range(0,map_height)]
    #map2 = [[ Tile(False) for x in range(0,map_width)] for y in range(0,map_height)]



#mymap = [[r*30],[r*30]]

#mymap[10][10].slow_down = True
    for y in range(12,33):
        for x in range(15,46):
            mymap[y][x].slow_down = True
    mymap[12][15].slow_down = False
    mymap[32][45].slow_down = False
    mymap[12][45].slow_down = False
    for i in range(3):
        mymap[32 - i][15].slow_down = False
        mymap[12+i][15].slow_down = False
        mymap[32-i][45].slow_down = False
        mymap[12+i][45].slow_down = False
    for i in range(3):
        mymap[32][15+i].slow_down = False
        mymap[12][15+i].slow_down = False
        mymap[32][45-i].slow_down = False
        mymap[12][45-i].slow_down = False
    for i in range(60):
        
        mymap[0][i].slow_down = True
        mymap[1][i].slow_down = True
        mymap[44][i].slow_down = True
        mymap[43][i].slow_down = True
        if i < 45:
            mymap[i][0].slow_down = True
            mymap[i][1].slow_down = True
            mymap[i][59].slow_down = True
            mymap[i][58].slow_down = True
            

    #top left
    for i in range(8):
        mymap[(map_height-1)-i][map_width - 2].slow_down = True
        mymap[1][i].slow_down = True
        mymap[(map_height-1)-i][1].slow_down = True
        mymap[1][(map_width-1)-i].slow_down = True
        if i < 7:
            mymap[(map_height-1)-i][map_width - 3].slow_down = True
            mymap[2][i].slow_down = True
            mymap[(map_height-1)-i][2].slow_down = True
            mymap[2][(map_width-1)-i].slow_down = True
        if i < 6:
            mymap[(map_height-1)-i][map_width - 4].slow_down = True
            mymap[3][i].slow_down = True
            mymap[(map_height-1)-i][3].slow_down = True
            mymap[3][(map_width-1)-i].slow_down = True
        if i < 5:
            mymap[(map_height-1)-i][map_width - 4].slow_down = True
            mymap[4][i].slow_down = True
            mymap[(map_height-1)-i][4].slow_down = True
            mymap[4][(map_width-1)-i].slow_down = True
        if i < 4:
            mymap[(map_height-1)-i][map_width - 5].slow_down = True
            mymap[5][i].slow_down = True
            mymap[(map_height-1)-i][5].slow_down = True
            mymap[5][(map_width-1)-i].slow_down = True
        if i < 3:
            mymap[(map_height-1)-i][map_width - 6].slow_down = True
            mymap[6][i].slow_down = True
            mymap[(map_height-1)-i][6].slow_down = True
            mymap[6][(map_width-1)-i].slow_down = True
        if i < 2:
            mymap[(map_height-1)-i][map_width - 7].slow_down = True
            mymap[7][i].slow_down = True
            mymap[(map_height-1)-i][7].slow_down = True
            mymap[7][(map_width-1)-i].slow_down = True

    
    
    
    
    #bottom right
    mymap[44][0].slow_down = True
    #bottom left
    mymap[0][59].slow_down = True
    for y in range(3):
        for i in range(2,16):
            mymap[i-2][29+y].finish_line = True
            if i < 14:
                mymap[i-2][29+y].finish_line = True
                mymap[i+31][29+y].checkpoint = (True,2)
            mymap[22+y][i+44].checkpoint = (True,1)
            mymap[22+y][i-2].checkpoint = (True,3)
            
        mymap[22+y][45].checkpoint = (False,1)

    #top right
    return mymap
#surface main^
def draw_map(m):
    for x in range(map_width):
        for y in range(map_height):
            if m[y][x].slow_down == False:
                #draw road
                gameDisplay.blit(road, (x*cell_width, y* cell_height))
            if m[y][x].slow_down:
                #draw grass
                gameDisplay.blit(grass, (x*cell_width, y* cell_height))

            if m[y][x].finish_line:
                #draw finish line
                gameDisplay.blit(finish, (x*cell_width, y* cell_height))
            if m[y][x].checkpoint[0]:
                gameDisplay.blit(check, (x*cell_width, y* cell_height))

            if m[y][x].extra_slow_down:
                gameDisplay.blit(grass, (x*cell_width, y* cell_height))
            if m[y][x].pseudo_wall:
                gameDisplay.blit(pseudo, (x*cell_width, y* cell_height))


                
    
                


#bassimg = pygame.image.load('basspro.png')
#bassimg = makeSprite('basspro.png')

#def bass(x,y):
    #gameDisplay.blit(bassimg,(x,y))
    #showSprite(bassimg)
    #moveSprite(bassimg,x,y)







def main():
    pygame.display.set_caption('McQuestionable')

    clock = pygame.time.Clock()

    crashed = False

    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        pygame.display.update()
        clock.tick(60)
        #gameDisplay.fill(blue)
        #mymap = create_map()
        tag = create_map_tag()
        draw_map(tag)
        #bass(400,200)

    pygame.quit()
    quit()

if __name__ == '__main__':
    main()