import pygame
class HurtBox( object ):
	def __init__(self, box, damage, framesToLive=-1):
		self.box = box
		self.damage = damage
		self.framesToLive = framesToLive
		self.numberOfHurtFrames= 0

	def checkAndHurt(self, entity):
		if entity.hitHexagon.isCollidingWithRect(entity.getMidPos(), self.box):
			entity.hurt(self.damage)
			self.numberOfHurtFrames += 1

	def tick(self):
		if(self.framesToLive > 0):
			self.framesToLive -= 1

	def destroy(self):
		self.framesToLive = 0
