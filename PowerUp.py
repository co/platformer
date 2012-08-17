import pygame, math, SimpleSprite

class PowerUp( SimpleSprite.SimpleSprite ):

	def __init__( self, imgFileName, game, pos,  frameSize=(8,8), animationDelay=2):
		super(PowerUp, self).__init__( imgFileName, game, pos, frameSize, animationDelay)
		
	def update(self):
		self.tickAnimation()
		playerPos = self.game.player.getMidPos()
		hitBox = pygame.Rect(self.pos, self.frameSize)
		if self.game.player.hitHexagon.isCollidingWithRect(playerPos, hitBox):
			self.game.player.heal(100)
			self.toBeRemoved = True
