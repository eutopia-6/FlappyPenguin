import random
import pygame

class Tubes():
    def __init__(self):
        self.__yTop = random.randint(10, 230)
        self.__yBot = self.__yTop + 150
        self.__width = 55
        self.__x = 557

    def getWidth(self):
        return self.__width

    def getY(self):
        return (self.__yTop, self.__yBot)

    def getX(self):
        return self.__x

    def moveTubes(self):
        self.__x -= 5

    def getLocation(self):
        return (self.__x, self.__yTop, self.__yBot)

    def draw(self, surface):
        DARKBLUE = (11, 11, 69)

        topY = self.getY()[0]
        botY = self.getY()[1]

        width = self.getWidth()

        pygame.draw.rect(surface, DARKBLUE, (self.getX(), 0, width, topY))
        pygame.draw.rect(surface, DARKBLUE, (self.getX(), botY, width, 459))

    def getOutlineTop(self):
        location = self.getLocation()
        return pygame.Rect(location[0], 0, self.getWidth(), location[1])

    def getOutlineBot(self):
        location = self.getLocation()
        return pygame.Rect(location[0], location[2], self.getWidth(), 459)



