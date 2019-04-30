import pygame
from pygame_functions import *
#import Pygame_Functions-master
pygame.init()
map_width = 80
map_height = 60
cell_width = 20
cell_height = 20
dis_width = 1600
dis_height = 1200
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grass = pygame.image.load('grass.png')
road = pygame.image.load('road.png')
class Tile:

    def __init__(self,slow_down):
        self.slow_down = slow_down


mymap = [[ Tile(False) for x in range(0,map_width)] for y in range(0,map_height)]
#mymap = [[r*30],[r*30]]

#mymap[10][10].slow_down = True

mymap[29][39].slow_down = True


gameDisplay = pygame.display.set_mode((dis_width,dis_height))
#surface main^
def draw_map(m):
    for x in range(map_width):
        for y in range(map_height):
            if m[y][x].slow_down:
                #draw grass
                gameDisplay.blit(grass, (x*cell_width, y* cell_height))

                
            else:
                #draw road
                gameDisplay.blit(road, (x*cell_width, y* cell_height))
                

pygame.display.set_caption('McQuestionable')

clock = pygame.time.Clock()
bassimg = pygame.image.load('basspro.png')
#bassimg = makeSprite('basspro.png')

def bass(x,y):
    gameDisplay.blit(bassimg,(x,y))
    #showSprite(bassimg)
    #moveSprite(bassimg,x,y)








crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    pygame.display.update()
    clock.tick(60)
    #gameDisplay.fill(blue)
    draw_map(mymap)
    bass(400,200)

pygame.quit()
quit()