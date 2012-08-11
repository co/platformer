import pygame, sys, SpriteSheet, HitHexagon, Level, Globals, soundplay, math
WALKANIMATION = 7
class Player( object ):
	def __init__(self, spriteSheet):
		self.controlAcc = 0.3
		self.pos = (0.0,0.0)
		self.velocity = (0.0,0.0)
		self.maxVelocity = 3
		self.isVisible = False;
		self.spriteSheet = spriteSheet
		self.hitHexagon = HitHexagon.HitHexagon((pygame.Rect(self.pos,
			(self.spriteSheet.spriteWidth, self.spriteSheet.spriteHeight))),
			0.5)
		self.facing = SpriteSheet.FACE_RIGHT
		self.game = None

	"""Interface"""
	def getPos( self ):
		return (int(self.pos[0]), int(self.pos[1]))

	def setHPBar( self, bar ):
		self.HPbar = bar

	def getMidPos( self ):
		return (self.getPos()[0] + float(self.spriteSheet.spriteWidth)/2-1,
				self.getPos()[1] + float(self.spriteSheet.spriteHeight)/2-1)

	def setPos( self, pos):
		self.pos = (int(round(pos[0])), int(round(pos[1])))

	def getIntPoint(self):
		return (int(round(self.pos[0])), int(round(self.pos[1])))

	def addPos( self, pos):
		x = max(self.pos[0] + pos[0],0)
		y = max(self.pos[1] + pos[1],0)
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

	def draw( self, canvasSurface, level ):
		print self.pos
		action = SpriteSheet.STAND
		if(math.fabs(self.velocity[0]) > 1):
			if((Globals.FRAMECOUNT % (2*WALKANIMATION)) < WALKANIMATION):
				action = SpriteSheet.RUN_1
			else: action = SpriteSheet.RUN_0
		if(self.isInAir(level)): action = SpriteSheet.JUMP
		self.spriteSheet.draw(canvasSurface, self.pos, (self.facing,
			action))
		if(Globals.DEBUG):
			self.hitHexagon.draw(self.getMidPos(), canvasSurface)

	def friction( self ):
		cutOffV = self.controlAcc*0.6
		if(self.velocity[0] <=  -cutOffV): self.addVelocity((cutOffV,0))
		elif(self.velocity[0] >= cutOffV): self.addVelocity((-cutOffV,0))
		else: self.setVelocity((0,self.velocity[1]))

	def jump(self):
		self.velocity= (self.velocity[0],-14)
		Globals.SOUNDPLAYER.playSound("jump.wav")
		

	def act( self, level):
		self.addPos(self.velocity)

		controlMultiplier = 0.4
		key=pygame.key.get_pressed()  #checking pressed keys
		if key[pygame.K_LSHIFT or pygame.K_RSHIFT]:
			controlMultiplier = 1.0
		if key[pygame.K_LEFT]:
			self.facing = SpriteSheet.FACE_LEFT
			self.addVelocity((-self.controlAcc*controlMultiplier,0))
		if key[pygame.K_RIGHT]:
			self.facing = SpriteSheet.FACE_RIGHT
			self.addVelocity((self.controlAcc*controlMultiplier,0))
		if (key[pygame.K_SPACE] and (not self.isInAir(level))): 	
			self.jump()
			#if key[pygame.K_DOWN]: self.addVelocity((0,  self.controlAcc))
		if (not (key[pygame.K_LEFT] or key[pygame.K_RIGHT])): self.friction()

		if(pygame.mouse.get_pressed()[0]):
			mousePos = pygame.mouse.get_pos()
			self.setPos((mousePos[0]/Globals.SCREENMULTIPLIER,
					mousePos[1]/Globals.SCREENMULTIPLIER))
	
	def getCollisions(self, level):
		return self.hitHexagon.getCollisions(self.getMidPos(), level)
