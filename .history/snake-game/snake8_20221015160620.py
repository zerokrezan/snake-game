import pygame
import random as r
import time
import sys
import pickle
import os

pygame.font.init()
myfont=pygame.font.SysFont("monospace",50)
myfonts = pygame.font.SysFont("monospaces",50)
points = 0

clock = pygame.time.Clock()

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

body = [(240,240) ]
noFruitEaten = True   
filesize_points = os.path.getsize("points1.py")
filesize_body = os.path.getsize("body.py")                   

def gameloop(screens):
    global filesize_points
    global filesize_body
    global points
    global speed_x, speed_y
    global body
    clock = pygame.time.Clock()
    global x, y
    pygame.mixer.init()
    pygame.mixer.music.load("/home/rezan/Music/startgame.wav")
    pygame.mixer.music.play()
    menue = True



    if filesize_points != 0:
        points = pickle.load(open("/home/rezan/Desktop/python_git/snake-game/points1.py", "rb"))
        body = pickle.load(open("/home/rezan/Desktop/python_git/snake-game/body.py", "rb"))
        speed_x = pickle.load(open("/home/rezan/Desktop/python_git/snake-game/speed_x.py", "rb"))
        speed_y = pickle.load(open("/home/rezan/Desktop/python_git/snake-game/speed_y.py", "rb"))
        x = body[0][0]
        y = body[0][1]
       

    
   
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
                        pygame.mixer.music.load("/home/rezan/Music/start.wav")
                        pygame.mixer.music.play()

                       
                        


        
            text2=myfont.render("Click anywhere on the ",1000,((0,0,0)))
            text3=myfont.render("screen to start ",1000,((0,0,0)))
            text4 = myfont.render(" the game!",1000,((0,0,0)))
            screen.blit(text2,(50, 250))
            screen.blit(text3,(150, 350))
            screen.blit(text4,(200, 450))
        
            pygame.display.set_caption("menue!")
        
            pygame.display.update()


        point=myfont.render( str(points),1000,((0,255,255)))
        screen.blit(point,(730, 10))

        pygame.display.update()
        screen.fill(pygame.color.Color("black"))
        events = pygame.event.get()
        check_pause(events)
        checkquit(events)
        save(events)
        
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
    global points
    global f_x, f_y
    global noFruitEaten                        
    if x == f_x and y == f_y:
        points += 1
        #print(points)
        
        pygame.mixer.music.load("/home/rezan/Music/2.wav")
        pygame.mixer.music.play()
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
            pygame.mixer.init()
            pygame.mixer.music.load("/home/rezan/Music/gameover.wav")
            pygame.mixer.music.play()
            pygame.time.delay(1500)
            exit()
            
            
    
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
        #screen = pygame.display.set_mode((width, hight))
        #screen.fill((0, 0, 0))
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


def save(p):
    global speed_x
    global speed_y
    global body
    global points
    save = False
    for event in p:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save = True    
    if save == True:
        pickle.dump(points, open("points1.py", "wb"))
        pickle.dump(body, open("body.py", "wb"))
        pickle.dump(speed_x, open("speed_x.py", "wb"))
        pickle.dump(speed_y, open("speed_y.py", "wb"))
        myfont = pygame.font.SysFont("myfont", 50)
        text1 = myfont.render("Savin Game!", 100, (255,0,0))
        screen.blit(text1, (300, 300))
        pygame.display.update()
        while save == True:
            events = pygame.event.get()
            checkquit(events)

            #pickle.dump(points, open("points1.py", "wb"))
            text2 = myfont.render(str(points), 50, (255,0,0))
            screen.blit(text2, (30, 350))
            pygame.display.update()
            exit(0)

    # unsave game
    unsave = False
    for event in p:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                unsave = True
    if unsave == True:
        myfont2 = pygame.font.SysFont("myfont", 50)
        text3 = myfont2.render("Closing Game Unsaved!", 100, (255,0,0))
        screen.blit(text3, (300, 300))
        pygame.display.update()
        while unsave == True:
            events = pygame.event.get()
            checkquit(events)

            #pickle.dump(points, open("points1.py", "wb"))
            text4 = myfont2.render(str(points), 50, (255,0,0))
            screen.blit(text4, (30, 350))
            pygame.display.update()
            exit(0)
    # start a new game - reached points will be deleted and set to 0
    newGame = False
    for event in p:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                newGame = True
    if newGame == True:
        with open("points1.py", 'r+') as f:
            f.truncate(0)
        #pickle.dump(0, open("points1.py", "wb"))
        #pickle.dump(0, open("body.py", "wb"))
        #pickle.dump(0, open("speed_x.py", "wb"))
        #pickle.dump(0, open("speed_y.py", "wb"))
        myfont3 = pygame.font.SysFont("myfont", 50)
        text5 = myfont3.render("Closing Game Unsaved!", 100, (255,0,0))
        screen.blit(text5, (300, 300))
        pygame.display.update()
        while newGame == True:
            events = pygame.event.get()
            checkquit(events)

            #pickle.dump(points, open("points1.py", "wb"))
            text6 = myfont3.render(str(points), 50, (255,0,0))
            screen.blit(text6, (30, 350))
            pygame.display.update()
            exit(0)


gameloop(screen)