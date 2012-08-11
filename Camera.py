import pygame, Globals
class Camera( object ):
	"""Keeps track of camera position and the canvas surface"""

	def __init__( self, playerPos, size ):
		
		x = max(playerPos[0] -size[0]/2, 0)
		y = max(playerPos[1] -size[1]/2, 0)
		self.cameraRect = pygame.Rect((x,y), (size[0], size[1]))
	
		self.FOCUSOFFSETX= 128
		self.FOCUSOFFSETY= 128

	def updateCameraPos(self, playerMidPos):
		#print "LOL big", self.cameraRect
		cameraFocus = self.cameraRect.inflate((-self.FOCUSOFFSETX, -self.FOCUSOFFSETY))
		#print "LOL small", cameraFocus

		if(cameraFocus.inflate((1,1)).collidepoint(playerMidPos)): return

		#print "at EDGE LOL"
		x = int(round(playerMidPos[0]))#* Globals.SCREENMULTIPLIER
		y = int(round(playerMidPos[1]))#* Globals.SCREENMULTIPLIER

		cameraFocus.top    = max(min(cameraFocus.top,    y),self.FOCUSOFFSETX/2)
		cameraFocus.bottom = max(cameraFocus.bottom, y)
		cameraFocus.left   = max(min(cameraFocus.left,  x),self.FOCUSOFFSETY/2)
		cameraFocus.right  = max(cameraFocus.right, x)

		self.cameraRect = cameraFocus.inflate((self.FOCUSOFFSETX, self.FOCUSOFFSETY))
