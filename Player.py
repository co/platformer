import pygame, sys, SpriteSheet, HitHexagon, Level, Globals, soundplay, math
import Entity, Bar, HurtBoxHandler

WALKANIMATION = 7

FACE_RIGHT = 0
FACE_LEFT =  1

STAND= 0
RUN_0 = 1
RUN_1 = 2
JUMP = 3
HURT = 4
DEAD = 5

HURTTIMER = 100

class Player(Entity.Entity):
	def __init__(self, spriteSheet):
		super(Player, self).__init__()
		self.controlAcc = 0.3
		self.spriteSheet = spriteSheet
		self.hitHexagon = HitHexagon.HitHexagon((pygame.Rect(self.pos,
			(self.spriteSheet.spriteWidth, self.spriteSheet.spriteHeight))),
			0.5)
		self.facing = FACE_RIGHT
		self.HPbar = Bar.Bar("hpbar.png", (8,8))
		self.alignment = HurtBoxHandler.ALIGNMENT_PLAYER
		self.hurtTimer = 0

	def draw( self, canvasSurface, level ):
		if( self.hurtTimer % 8 > 4 ):
			return
		action = STAND
		if(math.fabs(self.velocity[0]) > 1):
			if((Globals.FRAMECOUNT % (2*WALKANIMATION)) < WALKANIMATION):
				action = RUN_1
			else: action = RUN_0
		if(self.isInAir(level)):
			action = JUMP
		if(self.hurtTimer > HURTTIMER -30 and math.fabs(self.velocity[0]) < 2):
			action = HURT

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
		

	def updateHPBar(self):
		self.HPbar.length = self.maxHP
		self.HPbar.value = self.hp

	def act(self, level):
		self.addPos(self.velocity)
		self.updateHPBar()

		controlMultiplier = 0.4
		key=pygame.key.get_pressed()  #checking pressed keys
		if key[pygame.K_LSHIFT or pygame.K_RSHIFT]:
			controlMultiplier = 1.0
		if key[pygame.K_LEFT]:
			self.facing = FACE_LEFT
			self.addVelocity((-self.controlAcc*controlMultiplier,0))
		if key[pygame.K_RIGHT]:
			self.facing = FACE_RIGHT
			self.addVelocity((self.controlAcc*controlMultiplier,0))
		if (key[pygame.K_SPACE] and (not self.isInAir(level))):
			self.jump()
			#if key[pygame.K_DOWN]: self.addVelocity((0,  self.controlAcc))
		if (not (key[pygame.K_LEFT] or key[pygame.K_RIGHT])): self.friction()

		if(pygame.mouse.get_pressed()[0]):
			mousePos = pygame.mouse.get_pos()
			self.pos = (mousePos[0]/Globals.SCREENMULTIPLIER,
					mousePos[1]/Globals.SCREENMULTIPLIER)

		print self.hurtTimer
		if(self.hurtTimer > 0): self.hurtTimer -= 1
	
	def getCollisions(self, level):
		return self.hitHexagon.getCollisions(self.getMidPos(), level)

	def hurt(self, damage):
		if( self.hurtTimer == 0):
			self.hp = max(self.hp - damage, 0)
			if(not self.isInAir(self.game.level)):
				self.velocity = (0,-2)
			else:
				self.velocity = (0,self.velocity[1])
			self.hurtTimer = HURTTIMER
