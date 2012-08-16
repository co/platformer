import pygame
BARPARTS = 4
LEFTEDGE = 0
FILLED = 1
EMPTY = 2
RIGHTEDGE = 3
class Bar( object ):
	def __init__(self, barImgFileName, pos):
		self.length = 1
		self.value = self.length
		self.pos = pos
		self.img = pygame.image.load(barImgFileName)
		self.barPartWidth  = self.img.get_width()  / BARPARTS
		self.barHeight = self.img.get_height()

	def draw(self, canvasSurface):
		leftEdge = pygame.Rect((LEFTEDGE,0), (self.barPartWidth,self.barHeight))
		canvasSurface.blit(self.img, self.pos, leftEdge)
		for dx in range(self.value):
			canvasSurface.blit(self.img, (self.pos[0] + dx +1, self.pos[1]),
				pygame.Rect((FILLED,0),(self.barPartWidth,self.barHeight)))
			
		for dx in range(self.length - self.value):
			canvasSurface.blit(self.img, (self.pos[0] +1 + dx + self.value, self.pos[1]),
				pygame.Rect((EMPTY,0),(self.barPartWidth,self.barHeight)))

		canvasSurface.blit(self.img, (self.pos[0] + self.length + 1, self.pos[1]) ,
				pygame.Rect((RIGHTEDGE,0),(self.barPartWidth,self.barHeight)))
