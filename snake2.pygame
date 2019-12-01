import pygame
import time
width = 500
hight = 500


widthPlayer = 20
hightPlayer = 20

speed_x = 0
speed_y = 0

pygame.init()

screen = pygame.display.set_mode((width, hight))

x, y = 250, 250

v = 5

def gameloop(screen):
    global speed_x, speed_y
    clock = pygame.time.Clock()
    global x,y
    while True:
        pygame.display.update()
        screen.fill(pygame.color.Color("black"))
        events = pygame.event.get()
        checkquit(events)
        pygame.draw.rect(screen,
                         (255, 0, 0),
                         (x, y, 20, 20))
        handle_movement(events)
        x += speed_x * widthPlayer
        y += speed_y * hightPlayer
       
    
        

        clock.tick(10)


def handle_movement(liste):
    global speed_x, speed_y
    for rr in liste:
        if rr.type == pygame.KEYDOWN:
            if rr.key == pygame.K_RIGHT:
                speed_x = 1
                speed_y = 0
            if rr.key == pygame.K_LEFT:
                speed_x = -1
                speed_y = 0
            if rr.key == pygame.K_UP:
                speed_y = -1
                speed_x = 0
            if rr.key == pygame.K_DOWN:
                speed_y = 1
                speed_x = 0
    print(x,y)


def checkquit(e):
    for ev in e:
        if ev.type == pygame.QUIT:
            exit(0)
        if x  > width or x < 0 or y < 0 or y > hight:
            exit(0)



           
            

              
   

gameloop(screen)





