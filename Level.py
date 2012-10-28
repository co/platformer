import pygame, sys, Globals, Tile

WALL = 1
AIR = 0

BGLAYER = 0
PLAYLAYER = 2
NUMBEROFLAYERS = 3

def getLevel():
	print "lol"

class Level( object ):
	def __init__( self, tileset):
		self.level = [[[]]]
		self.tileset = tileset
		self.width= 1
		self.height= 1


	def readLayerFromFile(self, lines, layerNumber, lineNumber ):
		y = 0
		for line in lines[lineNumber+1:lineNumber+self.height]:
			x = 0
			for num in line.split(",")[:self.height]:
				tileType = int(num)
				if(tileType == -1):
					tileType = 0
				self.level[layerNumber][x][y] = tileType
				x +=1
			y +=1


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
		self.width = tilesWide
		self.height = tilesHigh

		self.level = [[[ 0 for j in range(tilesHigh) ] for k in
			range(self.width)] for l in range(NUMBEROFLAYERS)]
		for k in range(NUMBEROFLAYERS):
			self.readLayerFromFile(lines, k, i)
			i += 2 + self.height

	def isPixelWall( self, point ):
		x = point[0]/Globals.TILESIZE
		y = point[1]/Globals.TILESIZE
		if(x >= self.width or y >= self.height):
			return True
		if(Globals.DEBUG):
			pygame.draw.rect(Globals.CANVAS, (255, 0, 255),
				pygame.Rect((x*Globals.TILESIZE, y*Globals.TILESIZE),
					(Globals.TILESIZE,Globals.TILESIZE)))
		return self.tileset.getTile(self.level[PLAYLAYER][x][y]).isWall(Tile.pointToTilePoint(point))

	def draw( self, canvasSurface, cameraPos):
		startX = max(int(cameraPos[0]/Globals.TILESIZE -Globals.WIDTH), 0)
		startY = max(int(cameraPos[1]/Globals.TILESIZE -Globals.HEIGHT), 0)
		endX   = min(int(cameraPos[0]/Globals.TILESIZE +Globals.WIDTH), self.width)
		endY   = min(int(cameraPos[1]/Globals.TILESIZE +Globals.HEIGHT), self.height)
		for layer in range(NUMBEROFLAYERS):
			for y in range(startX, endX):
				for x in range(startY, endY):
					xMod = x #% self.height
					if(layer == BGLAYER):
						scrollSpeed = -1.1
						paralaxOffsetx = -1*(cameraPos[1]*scrollSpeed+cameraPos[1])
						paralaxOffsety = -1*(cameraPos[0]*scrollSpeed+cameraPos[0])
					else:
						paralaxOffsetx = 0
						paralaxOffsety = 0
					tile = self.tileset.getTile(self.level[layer][y][xMod])
					positionToDraw = (y*Globals.TILESIZE + paralaxOffsety,
							xMod*Globals.TILESIZE + paralaxOffsetx)
					tile.draw(canvasSurface, positionToDraw)

	#unused ?
	def getBoxes( self ):
		result = []
		y = 0
		for layer in range(NUMBEROFLAYERS):
			for y in range(len(self.level[0])):
				x = 0
				for x in range(len(self.level[0][0])):
					if(self.level[layer][y][x] == 1):
						result.append(pygame.Rect(Globals.TILESIZE*y, Globals.TILESIZE*x,
							Globals.TILESIZE, Globals.TILESIZE))
		return result

	#def getNeigbourTiles( self, point ):
