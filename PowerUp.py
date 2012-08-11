import pygame

class PowerUp( object ):

	def __init__( self, imgFileName, game, pos,  frameSize=(8,8), animationDelay=2):
		self.frameSize = frameSize
		self.img = pygame.image.load(imgFileName)
		self.numberOfFrames = self.img.get_width() / frameSize[0]
		self.animationTick = 0
		self.currentFrame = 0
		self.pos = pos
		self.animationDelay = animationDelay
		self.game = game

	def update(self):
		self.tickAnimation()

	def tickAnimation(self):
		self.animationTick += 1
		if(self.animationTick >= self.animationDelay):
			self.currentFrame = (self.currentFrame + 1) % self.numberOfFrames
			self.animationTick = 0

	def draw(self, canvasSurface):
		currentFrameRect = pygame.Rect((self.currentFrame*self.frameSize[0],0), self.frameSize)
		canvasSurface.blit(self.img, self.pos, currentFrameRect)
