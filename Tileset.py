import pygame, Globals, Tile

BLACK = (0, 0, 0, 255)

class Tileset( object ):
	def __init__(self, tilesetFileName):
		self.img = pygame.image.load(tilesetFileName + ".png")
		width = self.img.get_width() /Globals.TILESIZE
		height= self.img.get_height()/Globals.TILESIZE
		self.tiles = []
		for y in range(height):
			for x in range(width):
				tileChoiceRect = pygame.Rect((x * Globals.TILESIZE, y * Globals.TILESIZE),
					(Globals.TILESIZE, Globals.TILESIZE))
				collisionMask = self.loadCollisionMask(tilesetFileName + ".cm.png", tileChoiceRect)
				self.tiles.append(Tile.Tile(self.img, collisionMask, tileChoiceRect))

	def loadCollisionMask(self, collisionMaskFileName, tileChoiceRect ):
		img = pygame.image.load(collisionMaskFileName)
		#pixelMatrix = pygame.PixelArray(img)
		collisionMask = [[0 for i in range(16)] for j in range(16)]
		print "testo: ", tileChoiceRect.left
		offsetX = tileChoiceRect.left
		offsetY = tileChoiceRect.top
		for y in range(Globals.TILESIZE):
			for x in range(Globals.TILESIZE):
				#print "lolz: ",  img.get_at((y + offsetY,x + offsetX))
				if (img.get_at((x + offsetX,y + offsetY)) == BLACK):
					collisionMask[y][x] = 1
				else:
					collisionMask[y][x] = 0
		print collisionMask
		return collisionMask

	def getTile( self, index ):
		return self.tiles[index]
