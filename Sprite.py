import pygame, sys
class Sprite( object ):
	def __init__(self, imgFile):
		self.pos = (0,0)
		self.isVisible = False;
		self.img = pygame.image.load(imgFile)

	"""Interface"""
	def getPos( self ):
		return self.pos

	def setPos( self, pos):
		self.pos = (int(round(pos[0])), int(round(pos[1])))

	def addPos( self, pos):
		x = self.pos[0] + pos[0]
		y = self.pos[1] + pos[1]
		self.pos = (x,y)

	def setVisibility( self, newVisibility ):
		self.isVisible = newVisibility

	def draw( self, canvasSurface ):
		print self.pos
		canvasSurface.blit(self.img, self.pos)
