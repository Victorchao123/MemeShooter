
import pygame
from pygame.locals import *


#Setting up The Game
   
pygame.init()
screen=pygame.display.set_mode((1000,1000),HWSURFACE|DOUBLEBUF|RESIZABLE)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
keys = [False, False, False, False]
playerpos=[100,50]
pygame.display.set_caption('Game Test')

#Background Music

pygame.mixer.init()
pygame.mixer.music.load("Things/Sounds/soviet-anthem.mp3")
pygame.mixer.music.play(-1,0.0)

#Variable Stating

player = pygame.image.load("Things/Pictures/square.png")

door = pygame.image.load("Things/Pictures/cave.jpg")

start = pygame.image.load("Things/Pictures/start.jpg")

#The plan is to have the player "enter the doorway" and start the game.


while 1:
	#Screen Images
    screen.fill(0)
    screen.blit(player, playerpos)
    screen.blit(door,(685,800))
    screen.blit(start,(750,600))
    pygame.display.flip()
    #Exit Button
    for event in pygame.event.get():
      if event.type==pygame.QUIT: 
            pygame.quit() 
            exit(0)  

    #Player Movements
      if event.type == pygame.KEYDOWN:
           if event.key==pygame.K_UP:
               keys[0]=True
           elif event.key==pygame.K_LEFT:
               keys[1]=True
           elif event.key==pygame.K_DOWN:
               keys[2]=True
           elif event.key==pygame.K_RIGHT:
               keys[3]=True

      if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
  

      if keys[0]:
           playerpos[1]-=50
      elif keys[2]:
           playerpos[1]+=50
      elif keys[1]:
           playerpos[0]-=50
      elif keys[3]:
           playerpos[0]+=50  	    	
             
           