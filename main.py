import pygame
from tubes import Tubes

pygame.init()
gameScreen = pygame.display.set_mode((612, 459))
backgroundImage = pygame.image.load("flappyBack.jpg")

piplup = pygame.image.load("piplup.png")
piplupX = 50
piplupY = 229
piplupYchange = 0

speed = 60

counter = 0
counterFont = pygame.font.Font("freesansbold.ttf", 32)

def showCounter(counter):
    show = counterFont.render(f"Score: {counter}", True, (0, 0, 0))
    gameScreen.blit(show, (20, 20))

def showPiplup(x,y):
    gameScreen.blit(piplup, (x,y))

def pipOutline():
    return pygame.Rect(piplupX, piplupY, 50, 59)

def intersect(obj1, obj2, obj3):
    if (obj1.x + obj1.width >= obj2.x and obj1.x + obj1.width < obj2.width + obj2.x) and ((obj1.y <= obj2.height)):
        return False
    if (obj1.x + obj1.width >= obj3.x and obj1.x + obj1.width < obj3.width + obj3.x) and ((obj1.y + obj1.height >= obj3.y)):
        return False
    if (obj1.x + obj1.width < obj2.x) and (obj1.x + obj1.width >= obj2.x):
        return False
    if (obj1.x + obj1.width < obj3.x) and (obj1.x + obj1.width >= obj3.x):
        return False


if __name__ == "__main__":
    running = True
    showBegin = True
    tubesSpawn = Tubes()


    while running:

        fps = pygame.time.Clock()
        gameScreen.fill((0, 0, 0))
        gameScreen.blit(backgroundImage, (0,0))
        pygame.display.set_caption("Flappy Piplup")

        if showBegin:
            beginFont = pygame.font.Font("freesansbold.ttf", 40)
            begin = beginFont.render(f"Press SpaceBar to Start", False, (0, 0, 0))
            gameScreen.blit(begin, (80, 100))

        showPiplup(piplupX, piplupY)
        spawn = False

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    piplupYchange = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    piplupYchange = 3

        showCounter(counter)

        if piplupYchange != 0:
            spawn = True

        piplupY += piplupYchange

        if piplupY <= 0:
            piplupY = 0

        if piplupY >= 400:
            piplupY = 400

        showPiplup(piplupX, piplupY)

        if spawn:
            tubesSpawn.draw(gameScreen)
            showBegin = False
            tubesSpawn.moveTubes()
            if tubesSpawn.getX() < 0:
                counter += 1
                tubesSpawn = Tubes()

        if intersect(pipOutline(), tubesSpawn.getOutlineTop(), tubesSpawn.getOutlineBot()) == False :
            running = False


        speed += 0.05

        fps.tick(speed)
        pygame.display.update()


