import pygame, sys, SpriteSheet, HitHexagon, Level, Globals, soundplay, math
import Enemy, Bar, HurtBoxHandler, VectorMath

WALKANIMATION = 7

FACE_RIGHT = 0
FACE_LEFT =  1

STAND= 0
RUN_0 = 1
RUN_1 = 2
JUMP = 3
HURT = 4
DEAD = 5

HURTTIMER = 20

class Mamal(Enemy.Enemy):
	def __init__(self, spriteSheet, game):
		super(Mamal, self).__init__(spriteSheet, game)
		self.facing = FACE_LEFT
		self.hurtTimer = 0

	def draw( self, canvasSurface, level ):
		if( (self.hurtTimer % 8) > 4 ):
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

	def flipFacing(self):
		if(self.facing is FACE_LEFT):
			self.facing = FACE_RIGHT
		else:
			self.facing = FACE_LEFT

	def act(self, level):
		SPEED = 1

		oldPos = self.pos
		if(self.facing == FACE_LEFT):
			self.pos = VectorMath.add(self.pos, (-SPEED, 0))
		else:
			self.pos = VectorMath.add(self.pos, (SPEED, 0))

		if(self.isInAir(level)):
			self.pos = oldPos
			self.flipFacing()

		self.pos = VectorMath.add(self.pos, self.velocity)

		if(self.hurtTimer > 0): self.hurtTimer -= 1
	
	def getCollisions(self, level):
		return self.hitHexagon.getCollisions(self.getMidPos(), level)

	def hurt(self, damage):
		if( self.hurtTimer == 0):
			self.hp = max(self.hp - damage, 0)
			if(not self.isInAir(self.game.level)):
				self.velocity = (0,-1)
			else:
				self.velocity = (0,self.velocity[1])
			self.hurtTimer = HURTTIMER

	def reactToCollision(self, collisions):
		self.checkAndCrush(collisions)
		self.pushOutOfWalls(collisions)

		if(collisions[HitHexagon.LEFT]):
			self.facing = FACE_RIGHT
		if(collisions[HitHexagon.RIGHT]):
			self.facing = FACE_LEFT
