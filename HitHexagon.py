import pygame, Globals, Level

LEFT   = 0
RIGHT  = 1
TOP    = 2
BOTTOM = 3

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

	def getCollisions(self, midPos, level):
		top    = (int(round(midPos[0])), int(round(midPos[1] + self.relativeTop)))
		bottom = (int(round(midPos[0])), int(round(midPos[1] + self.relativeBottom)))
		left   = (int(round(midPos[0]) + self.relativeLeft), int(round(midPos[1])))
		right  = (int(round(midPos[0]) + self.relativeRight),int(round(midPos[1])))

		print "top: " + repr(top)
		print "bottom: " + repr(bottom)
		print "left: " + repr(left)
		print "right: " + repr(right)
		result = [False, False,  False,  False]
		
		#not hexagon yet more left and right
		if(level.isPixelWall(top)): result[TOP] = True
		if(level.isPixelWall(bottom)): result[BOTTOM] = True
		if(level.isPixelWall(left)): result[LEFT] = True
		if(level.isPixelWall(right)): result[RIGHT] = True
		if((not any(result)) or not Globals.DEBUG): return result
#DEBUG WRITING
		#pygame.draw.rect(Globals.CANVAS, (255, 255, 255),
		#pygame.draw.rect(Globals.CANVAS, (255, 0, 0), rect)

		font = pygame.font.Font(None, 24)
		text1 = font.render("colision (t:%s,b:%s,l:%s,r:%s)," %
				(result[TOP], result[BOTTOM], result[LEFT], result[RIGHT]), 1, (10, 10, 10))
		Globals.CANVAS.blit(text1, (20,60))
		return result

	def draw( self, midPos, canvasSurface ):
		top    = (int(round(midPos[0])), int(round(midPos[1] + self.relativeTop)))
		bottom = (int(round(midPos[0])), int(round(midPos[1] + self.relativeBottom)))
		left   = (int(round(midPos[0]) + self.relativeLeft), int(round(midPos[1])))
		right  = (int(round(midPos[0]) + self.relativeRight),int(round(midPos[1])))
		if(not Globals.DEBUG): return
		pygame.draw.line(canvasSurface, (255, 255, 0), top, bottom)
		pygame.draw.line(canvasSurface, (0, 255, 255), left, right)

