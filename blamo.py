import pygame
from pygame import draw

# define a main function
def main():
    
    pygame.display.set_caption("Blamo")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1900,1000))
     
    # define a variable to control the main loop
    running = True
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(0,0,128),(450,450,30,40,30))
    pygame.display.update()
    # main loop
    while running:
        
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()