import pygame, sys, SpriteSheet, HitHexagon, Level, Globals, soundplay, math
import Entity, HurtBox, HurtBoxHandler

SPEED = 1

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

	def draw( self, canvasSurface, level ):
		self.spriteSheet.draw(canvasSurface, self.pos, (self.facing,
			self.action))

	def attack(self):
		hurtBox = HurtBox.HurtBox(self.hitHexagon.getRect(self.getMidPos()), 1, 1)
		self.game.hurtBoxHandler.addHurtBox(hurtBox, self.alignment)


	def act( self, level):
		sx = self.pos[0]
		sy = self.pos[1]
		self.attack()

		px = self.game.player.pos[0]
		py = self.game.player.pos[1]

		if(sx > px): sx -= SPEED
		if(sx < px): sx += SPEED
		if(sy > py): sy -= SPEED
		if(sy < py): sy += SPEED

		self.pos = (sx,sy)

	def getCollisions(self, level):
		return self.hitHexagon.getCollisions(self.getMidPos(), level)
