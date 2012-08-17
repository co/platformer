import pygame, Globals, Level

LEFT   = 0
RIGHT  = 1
TOP    = 2
BOTTOM = 3
NUMBEROFPOINTS = 4

class HitHexagon( object ):
		
	def __init__(self, rect, multiplier):
		self.relativeTop = -rect.height/2 + 0.5
		self.relativeBottom = rect.height/2
		self.relativeRight = (rect.width/2) * multiplier
		self.relativeLeft = -(rect.width/2) * multiplier

	def getPointUnderFoot(self, midPos):
		bottom = (int(round(midPos[0])), int(round(midPos[1] + self.relativeBottom)))
		underFoot = (bottom[0], bottom[1]+1)
		return underFoot

	def getPoints(self, midPos):
		points = [0 for i in range(NUMBEROFPOINTS)]
		points[TOP]    = (int(round(midPos[0])), int(round(midPos[1] + self.relativeTop)))
		points[BOTTOM] = (int(round(midPos[0])), int(round(midPos[1] + self.relativeBottom)))
		points[LEFT]   = (int(round(midPos[0]) + self.relativeLeft), int(round(midPos[1])))
		points[RIGHT]  = (int(round(midPos[0]) + self.relativeRight),int(round(midPos[1])))
		return points

	def getRect(self, midPos):
		points = self.getPoints(midPos)
		return pygame.Rect((points[LEFT][0],points[TOP][1]),
			(points[RIGHT][0]-points[LEFT][0],points[BOTTOM][1]-points[TOP][1]))



	def getCollisions(self, midPos, level):

		points = self.getPoints(midPos)

		#print "top: " + repr(top)
		#print "bottom: " + repr(bottom)
		#print "left: " + repr(left)
		#print "right: " + repr(right)
		results = [False for i in range(NUMBEROFPOINTS)]
		
		#not hexagon yet more left and right
		for i in range(NUMBEROFPOINTS):
			if(level.isPixelWall(points[i])): results[i] = True
		if((not any(results)) or not Globals.DEBUG): return results
#DEBUG WRITING
		#pygame.draw.rect(Globals.CANVAS, (255, 255, 255),
		#pygame.draw.rect(Globals.CANVAS, (255, 0, 0), rect)

		font = pygame.font.Font(None, 24)
		text1 = font.render("colision (t:%s,b:%s,l:%s,r:%s)," %
				(results[TOP], results[BOTTOM], results[LEFT], results[RIGHT]), 1, (10, 10, 10))
		Globals.CANVAS.blit(text1, (20,60))
		return results

	def draw( self, midPos, canvasSurface ):
		if(not Globals.DEBUG): return

		points = self.getPoints(midPos)

		pygame.draw.line(canvasSurface, (255, 255, 0), points[TOP], points[BOTTOM])
		pygame.draw.line(canvasSurface, (0, 255, 255), points[LEFT], points[RIGHT])

	def isCollidingWithRect( self, midPos, rect ):
		thisRect = self.getRect(midPos)
		return thisRect.colliderect(rect)

