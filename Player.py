import pygame, sys, SpriteSheet, HitHexagon, Level, Globals, soundplay, math, Entity
WALKANIMATION = 7
class Player(Entity.Entity):
	def __init__(self, spriteSheet):
		super(Player, self).__init__()
		self.controlAcc = 0.3
		self.spriteSheet = spriteSheet
		self.hitHexagon = HitHexagon.HitHexagon((pygame.Rect(self.pos,
			(self.spriteSheet.spriteWidth, self.spriteSheet.spriteHeight))),
			0.5)
		self.facing = SpriteSheet.FACE_RIGHT

	def setHPBar( self, bar ):
		self.HPbar = bar

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
		else: self.velocity = (0,self.velocity[1])

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
