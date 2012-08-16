import pygame
SPRITESWIDE = 2
SPRITESHIGH = 10

FACING = 0
ACTION = 1

class SpriteSheet:
	def __init__(self, imgFileName):
		self.img = pygame.image.load(imgFileName)
		self.spriteWidth  = self.img.get_width()  / SPRITESWIDE
		self.spriteHeight = self.img.get_height() / SPRITESHIGH

	def draw(self, canvasSurface, pos, state):
		canvasSurface.blit(self.img, pos, self.getStateRect(state))
	
	def getStateRect(self, state):
		return pygame.Rect(self.spriteWidth*state[FACING], self.spriteHeight*
				state[ACTION], self.spriteWidth, self.spriteHeight)
