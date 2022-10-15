import pygame

width = 500
hight = 500

widthPlayer = 20
hightPlayer = 20

speed_x = 0
speed_y = 0


x,y = 250,250


pygame.init()

screen = pygame.display.set_mode((width,hight)) # screen wird erst dann ausgeführt, wenn die Funktionen gameloop(screen) und checkquit(e) vorliegen!

# code wird vom compiler von oben nach unten gelesen!

def gameloop(screen):
    x,y = 250,250
   
    while True:      
        pygame.display.update()
        events = pygame.event.get()
        screen.fill((0,0,0))         # Schwarz, weil Spuren zu sehen sind!
        checkquit(events)            # checkquit(events) bedeutet, dass Python die Funktion checkquit(quit) ausführt. 
        pygame.draw.rect(screen,
                        (255, 0, 0),
                        (x,y,20,20))

        speed_x, speed_y = handle_movement(events) # same meaning like above!
        x += speed_x * widthPlayer
        y += speed_y * hightPlayer
    

def handle_movement(liste):
    s_x = 0
    s_y = 0
    for ev in liste:
        if ev.type == pygame.KEYDOWN:       # ev steht für event als Variable und steht beliebig zur Auswahl!Also event.type = ev.type.Außerdem wurde ev als Variable schon für die Funktion handle_movement(liste) benutzt.
            if ev.key == pygame.K_RIGHT:
                s_x = 1
            if ev.key == pygame.K_LEFT:
                s_x = -1
            if ev.key == pygame.K_UP:
                s_y = -1

            if ev.key == pygame.K_DOWN:
                s_y = 1
    return s_x,s_y

def checkquit(quit):
    for ev in quit:
        if ev.type == pygame.QUIT:
            exit(0) # Schließen des Fensters in 0 Sekunden!
    
      

gameloop(screen) #screen wird nun ausgeführt!


