import pygame
import random as r
import time


width = 500
hight = 500

widthPlayer = 20
hightPlayer = 20

speed_x = 1
speed_y = 0

pygame.init()

screen = pygame.display.set_mode((width, hight))

x = 240
y = 240

f_x = r.randint(1, 24) * widthPlayer
f_y = r.randint(1, 24) * hightPlayer

body = [(240, 240), (220, 240), (200, 240),(180,240),(160,240)]
noFruitEaten = True                         

def gameloop(screen):
 

    global speed_x, speed_y
    global body
    clock = pygame.time.Clock()
    global x, y
    while True:
        pygame.display.update()

        screen.fill(pygame.color.Color("black"))
        events = pygame.event.get()
        checkquit(events)
        for rect in body:
            pygame.draw.rect(screen,
                            (255, 0, 0),
                            (rect[0],rect[1],  20-3, 20-3))                         
        pygame.draw.rect(screen,
                         (0, 128, 0),
                         (f_x, f_y, 20, 20))
        
        handle_movement(events)
        x += speed_x * widthPlayer
        y += speed_y * hightPlayer

        check_eaten()                         
        handle_body()                        
        body[0] = (x, y)
        check_wall()
        check_body_touched()
        clock.tick(10)


def handle_movement(liste):
    global speed_x, speed_y
    for rr in liste:
        if rr.type == pygame.KEYDOWN:
            if rr.key == pygame.K_RIGHT and not(speed_x == -1 and speed_y == 0):
                speed_x = 1
                speed_y = 0
            if rr.key == pygame.K_LEFT and not(speed_x == 1 and speed_y == 0):
                speed_x = -1
                speed_y = 0
            if rr.key == pygame.K_UP and not(speed_x == 0 and speed_y == 1):
                speed_y = -1
                speed_x = 0
            if rr.key == pygame.K_DOWN and not(speed_x == 0 and speed_y == -1):
                speed_y = 1
                speed_x = 0

def check_eaten():
    global f_x, f_y
    global noFruitEaten                        
    if x == f_x and y == f_y:


        while True:
            coordinatesFound = True
            maybe_x = r.randint(1, 24) * widthPlayer
            maybe_y = r.randint(1, 24) * hightPlayer
            for k in body:
                if maybe_x == k[0] and maybe_y == k[1]:
                    coordinatesFound = False

            if coordinatesFound == True:
                break

        f_x = maybe_x
        f_y = maybe_y
        noFruitEaten = False                        



def handle_body():
    global noFruitEaten
    global body                        
    length_of_body = len(body)
    if noFruitEaten:                        
        for i in range(length_of_body - 1):
            body[-(i + 1)] = body[-(i + 2)]
    else:                        
        body.append(body[-1])                        
        for i in range(length_of_body - 1):
            body[-(i + 2)] = body[-(i + 3)]                        
            noFruitEaten = True                        


def check_wall():
    global x, y
    if x > width:
        x = 0
    if x < 0:
        x = width
    if y > hight:
        y = 0
    if y < 0:
        y = hight

def check_body_touched():
    global x, y
    global width,hight
    for k in body[4:]:
        if k[0] == x and k[1] == y:
            exit(0)
            pygame.display.set_mode((width, hight))
            pygame.display.flip()




def checkquit(e):
    
    for ev in e:
        if ev.type == pygame.QUIT:
            exit(0)
            
            
            
            
 gameloop(screen)
