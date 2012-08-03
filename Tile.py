import pygame, sys, Globals

def pointToTilePoint(point):
	"""docstring for pointToTilePoint"""
	x,y = point
	return (x % Globals.TILESIZE, y % Globals.TILESIZE)

class Tile( object ):
	def __init__(self, img, collisionMask, tileChoiceRect):
		self.img = img
		self.collisionMask = collisionMask
		self.tileChoiceRect = tileChoiceRect

	def draw(self, canvasSurface, pos):
		canvasSurface.blit(self.img, pos, self.tileChoiceRect)

	def isWall(self, point):
		return(self.collisionMask[point[0]][point[1]] == 1)
