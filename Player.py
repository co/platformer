import pygame, sys, HitHexagon, Level, Globals
class Player( object ):
	def __init__(self, imgFile):
		self.controlAcc = 0.3
		self.pos = (0,0)
		self.velocity = (0,0)
		self.maxVelocity = 7
		self.isVisible = False;
		self.img = pygame.image.load(imgFile)
		self.hitHexagon = HitHexagon.HitHexagon((pygame.Rect(self.pos,
			(self.img.get_width(), self.img.get_height()))), 1)
		self.state = 1

	"""Interface"""
	def getPos( self ):
		return self.pos
	def getMidPos( self ):
		return (self.pos[0] + self.img.get_width()/2, self.pos[1] +
				self.img.get_height()/2)

	def setPos( self, pos):
		self.pos = (int(round(pos[0])), int(round(pos[1])))

	def getIntPoint(self):
		return (int(round(self.pos[0])), int(round(self.pos[1])))

	def addPos( self, pos):
		x = self.pos[0] + pos[0]
		y = self.pos[1] + pos[1]
		self.pos = (x,y)

	def isInAir( self, level):
		underFoot = self.hitHexagon.getPointUnderFoot(self.getMidPos())
		isInAir = (not level.isPixelWall( underFoot ))
		
		if(Globals.DEBUG):
			font = pygame.font.Font(None, 24)
			text1 = font.render("inAir? %s" %
					(isInAir), 1, (10, 10, 10))
			Globals.CANVAS.blit(text1, (20,60))
		

		return isInAir

	def addVelocity( self, velocity):
		xV = self.velocity[0] + velocity[0]
		yV = self.velocity[1] + velocity[1]


		xV = max(-1*self.maxVelocity, xV)
		yV = max(-1*self.maxVelocity, yV)

		xV = min(self.maxVelocity, xV)
		yV = min(self.maxVelocity, yV)

		self.velocity = (xV,yV)

	def setVelocity( self, velocity ):

		self.velocity = velocity

	def setVisibility( self, newVisibility ):
		self.isVisible = newVisibility

	def draw( self, canvasSurface ):
		canvasSurface.blit(self.img, self.pos)
		self.hitHexagon.draw(self.getMidPos(), canvasSurface)

	def friction( self ):
		cutOffV = self.controlAcc*3.0
		if(self.velocity[0] <=  -cutOffV): self.addVelocity((cutOffV,0))
		elif(self.velocity[0] >= cutOffV): self.addVelocity((-cutOffV,0))
		else: self.setVelocity((0,self.velocity[1]))

	def act( self, level):
		self.addPos(self.velocity)

		key=pygame.key.get_pressed()  #checking pressed keys
		if key[pygame.K_LEFT]: self.addVelocity((-self.controlAcc,0))
		if key[pygame.K_RIGHT]:self.addVelocity((self.controlAcc,0))
		if (key[pygame.K_SPACE] and (not self.isInAir(level))): self.addVelocity((0,
			-self.controlAcc*40))
		#if key[pygame.K_DOWN]: self.addVelocity((0,  self.controlAcc))
		if (not (key[pygame.K_LEFT] or key[pygame.K_RIGHT])): self.friction()

		if(pygame.mouse.get_pressed()[0]):
			self.setPos(pygame.mouse.get_pos())
	
	def getCollisions(self, level):
		return self.hitHexagon.getCollisions(self.getMidPos(), level)
