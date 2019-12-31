
import pygame
import random as r
import time
import sys

pygame.font.init()
myfont=pygame.font.SysFont("monospace",50)


width = 800
hight = 800                                                                 # größe muss mit funktion pause übereinstimmen!

widthPlayer = 20
hightPlayer = 20

speed_x = 1
speed_y = 0

pygame.init()

mouse = pygame.mouse.get_pos()
screen = pygame.display.set_mode((width, hight))
running = True
x = 240
y = 240

f_x = r.randint(1, 24) * widthPlayer
f_y = r.randint(1, 24) * hightPlayer

body = [(240, 240), (220, 240), (200, 240),(180,240),(160,240)]
noFruitEaten = True                         

def gameloop(screens):
    global speed_x, speed_y
    global body
    clock = pygame.time.Clock()
    global x, y
    
    
        
    
    menue = True
    while True:
        while menue:
            
            screen.fill((255,255,0))
        
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:                               # 1 = left_mousekey, 2 = middle_mousekey, 3 = right_mousekey, 4 = scrollup_mousekey, 5 = scrolldown_mousekey
                        menue = False

        
            text2=myfont.render("Click anywhere on the ",1000,((0,0,0)))
            text3=myfont.render("screen to start ",1000,((0,0,0)))
            text4 = myfont.render(" the game!",1000,((0,0,0)))
            screen.blit(text2,(80, 250))
            screen.blit(text3,(150, 300))
            screen.blit(text4,(230, 350))
            pygame.display.set_caption("menue!")
        
            pygame.display.update()





        pygame.display.update()
        screen.fill(pygame.color.Color("black"))
        events = pygame.event.get()
        check_pause(events)
        checkquit(events)
        #button(350,170,120,60,(150,0,0),(255,0,0))
        #button(150,170,120,60,(0,150,0),(0,255,0))
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


           
def check_pause(events):
    pause = False
    for rr in events:
        if rr.type == pygame.KEYDOWN:
            if rr.key == pygame.K_p:
                pause = True
                break

    if pause == True:
        red = (255, 0, 0)
        screen = pygame.display.set_mode((width, hight))
        screen.fill((0, 0, 0))
        myfont = pygame.font.SysFont("monospace", 50)
        text1 = myfont.render("Pause!", 100, red)
        text2 = myfont.render("Please resume your game!", 50, red)
        screen.blit(text2, (30, 350))
        screen.blit(text1, (300, 300))
        pygame.display.update()
        while pause == True:
            events = pygame.event.get()
            checkquit(events)
            for rr in events:
                if rr.type == pygame.KEYDOWN:
                    if rr.key == pygame.K_p:
                        pause = False
                        break



    



gameloop(screen)
