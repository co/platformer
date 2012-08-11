import pygame
SPRITESWIDE = 2
SPRITESHIGH = 10

FACING = 0
ACTION = 1

FACE_RIGHT = 0
FACE_LEFT =  1

STAND= 0
RUN_0 = 1
RUN_1 = 2
JUMP = 3
DEAD = 4

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
