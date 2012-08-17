import pygame, SimpleSprite, HurtBox, HurtBoxHandler, VectorMath
class Attack( SimpleSprite.SimpleSprite ):
	def __init__( self, imgFileName, game, pos,  frameSize=(8,8), animationDelay=2):
		super(Attack, self).__init__( imgFileName, game, pos, frameSize, animationDelay)
		self.damage = 1
		self.framesToLive = -1
		self.velocity = (0,0)
		self.alignment = HurtBoxHandler.ALIGNMENT_ENEMY
		self.lastHurtBox = None

	def update(self):
		if(not self.lastHurtBox is None):
			if(self.lastHurtBox.numberOfHurtFrames > 0):
				self.toBeRemoved = True
				return
		self.tick()
		self.pos = VectorMath.add(self.pos, self.velocity)
		box = pygame.Rect(self.pos, self.frameSize)
		hurtBox = HurtBox.HurtBox(box, 2, 1)
		self.game.hurtBoxHandler.addHurtBox(hurtBox, self.alignment)
		self.lastHurtBox = hurtBox
