import pygame
import numpy as np
import time 

width, height = 800, 800

nxC, nyC = 80, 80
dimCW = (width) / nxC
dimCH = (height) / nyC

pygame.init()

screen = pygame.display.set_mode((width, height))

bg = (10, 10, 10)
LIVE_COLOR = (255,255,255)
DEAD_COLOR = (128,128,128)

gameState = np.zeros((nxC, nyC))

#gameState[5, 3] = 1 gameState[5, 4] = 1 gameState[5, 5] = 1

#gameState[21, 21] = 1 gameState[22, 22] = 1 gameState[22, 23] = 1 gameState[21, 23] = 1 gameState[20, 23] = 1

pauseExect = False
running = True
while running:

    newGameState = np.copy(gameState)
        
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            x, y = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[x, y] = not mouseClick [2]
    screen.fill(bg)

    for x in range(0, nxC):
        for y in range(0, nyC):

            if not pauseExect:
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + gameState[(x) % nxC, (y - 1) % nyC] + \
                gameState[(x + 1) % nxC, (y - 1) % nyC] +  gameState[(x - 1) % nxC, (y) % nyC] + \
                gameState[(x + 1) % nxC, (y) % nyC] + gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                gameState[(x) % nxC, (y + 1) % nyC] +  gameState[(x + 1) % nxC, (y + 1) % nyC]
                if gameState [x, y] == 0 and n_neigh == 3:
                    newGameState [x, y] = 1
                elif gameState [x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                        newGameState [x, y] = 0
            poly = [((x) * dimCW, y * dimCH), ((x+1) * dimCW, y * dimCH), ((x+1) * dimCW, (y+1) * dimCH), ((x) * dimCW, (y+1) * dimCH)]
            
            if newGameState[x, y] == 1:
                pygame.draw.polygon(screen, LIVE_COLOR, poly, 0)
                
            else:
                pygame.draw.polygon(screen, DEAD_COLOR, poly, 1)
    
    gameState = np.copy(newGameState)
    time.sleep(0.1)
    pygame.display.flip()



pygame.quit()