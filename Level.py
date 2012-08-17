import pygame, sys, Globals, Tile

WALL = 1
AIR = 0

def getLevel():
	print "lol"

class Level( object ):
	def __init__( self, tileset):
		self.level = [[]]
		self.tileset = tileset
		self.width= 1
		self.height= 1

	
	def loadFile( self, fileName ):
		f = open(fileName)
		lines = f.readlines()
		f.close()

#read preamble
		tilesWide=0
		tilesHigh=0
		i = 0
		for line in lines:
			lowLine = str.lower(line)
			if(lowLine.find("tileswide") == 0):
				tilesWide = int(line.split(" ")[1])
			if(lowLine.find("tileshigh") == 0):
				tilesHigh = int(line.split(" ")[1])
			if(lowLine.find("layer") == 0):
				break
			i += 1
#read actual height instead of asserting 50
		self.level = [[ 0 for j in range(tilesHigh) ] for k in range(tilesWide)]

		y = 0
		for line in lines[i+1:i+tilesHigh]:
			x = 0
			for num in line.split(",")[:tilesWide]:
				tileType = int(num)
				if(tileType == -1): tileType = 0
				self.level[x][y] = tileType
				x +=1
			y +=1
		self.width = tilesWide
		self.height = tilesHigh

	def isPixelWall( self, point ):
		x = point[0]/Globals.TILESIZE
		y = point[1]/Globals.TILESIZE
		if(x >= self.width or y >= self.height):
			return True
		if(Globals.DEBUG):
			pygame.draw.rect(Globals.CANVAS, (255, 0, 255),
				pygame.Rect((x*Globals.TILESIZE, y*Globals.TILESIZE),
					(Globals.TILESIZE,Globals.TILESIZE)))
		return self.tileset.getTile(self.level[x][y]).isWall(Tile.pointToTilePoint(point))

	def draw( self, canvasSurface ):
		tileImg = pygame.image.load("tile.png")
		for y in range(len(self.level)):
			for x in range(len(self.level[0])):
				self.tileset.getTile(self.level[y][x]).draw(canvasSurface,
						(y*Globals.TILESIZE,x*Globals.TILESIZE))

	#unused ?
	def getBoxes( self ):
		result = []
		y = 0
		for y in range(len(self.level)):
			x = 0
			for x in range(len(self.level[0])):
				if(self.level[y][x] == 1):
					result.append(pygame.Rect(Globals.TILESIZE*y, Globals.TILESIZE*x,
						Globals.TILESIZE, Globals.TILESIZE))
				x += 1
			y += 1
		return result

	#def getNeigbourTiles( self, point ):
