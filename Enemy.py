import pygame, sys, SpriteSheet, HitHexagon, Level, Globals, soundplay, math
import Entity, HurtBox, HurtBoxHandler, random, VectorMath, Attack

class Enemy(Entity.Entity):
	def __init__(self, spriteSheet, game):
		super(Enemy, self).__init__()
		self.spriteSheet = spriteSheet
		self.hitHexagon = HitHexagon.HitHexagon((pygame.Rect(self.pos,
			(self.spriteSheet.spriteWidth, self.spriteSheet.spriteHeight))),
			0.5)
		self.game = game
		self.facing = 0
		self.action = 0
		self.alignment = HurtBoxHandler.ALIGNMENT_ENEMY
		self.shotCoolDown = 0

	def draw( self, canvasSurface, level ):
		self.spriteSheet.draw(canvasSurface, self.pos, (self.facing,
			self.action))

	def act( self, level):
		return None

	def getCollisions(self, level):
		return self.hitHexagon.getCollisions(self.getMidPos(), level)
