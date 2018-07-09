import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('Meme Shooter')

black = (0,0,0)
white = (255,255,255)

player_width = 73

pygame.mixer.init()
pygame.mixer.music.load("Things/Sounds/soviet-anthem.mp3")
pygame.mixer.music.play(-1,0.0)

clock = pygame.time.Clock()
playerImg = pygame.image.load('Things/Pictures/josephstalin.png')

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def player(x,y):
    gameDisplay.blit(playerImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('Things/Fonts/FreeSansBold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
def crash():
    message_display('You Died')

x =  (display_width * 0.60)
y = (display_height * 1.2)

x_change = 0

thing_startx = random.randrange(0, display_width)
thing_starty = -600
thing_speed = 7
thing_width = 100
thing_height = 100

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            python.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -25
            elif event.key == pygame.K_RIGHT:
                x_change = 25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 00

    x += x_change 

    gameDisplay.fill(white)


    things(thing_startx, thing_starty, thing_width, thing_height, black)
    thing_starty += thing_speed
    player(x,y)

    if x > display_width - player_width or x < 0:
        crash()

    if y < thing_starty+thing_height:
            print('y crossover')

    if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
            print('x crossover')
            crash()
      
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
           