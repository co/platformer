import pygame, Globals, HitHexagon, HurtBoxHandler
class Entity(object):
	def __init__(self):
		self.pos = (0.0,0.0)
		self.velocity = (0.0,0.0)
		self.maxVelocity = 3
		self.isVisible = False;
		self.hitHexagon = HitHexagon.HitHexagon((pygame.Rect(self.pos,
			(Globals.TILESIZE, Globals.TILESIZE))),
			0.5)
		self.game = None
		self.maxHP = 30
		self.hp = self.maxHP
		self.alignment = HurtBoxHandler.ALIGNMENT_ENEMY

	def getMidPos( self ):
		return (self.pos[0] + float(self.spriteSheet.spriteWidth)/2-1,
				self.pos[1] + float(self.spriteSheet.spriteHeight)/2-1)

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

	def draw( self, canvasSurface, level ):
		pygame.drawRect(canvasSurface, (255,0,255), pygame.Rect(pos, (Globals.TILESIZE, Globals.TILESIZE)))

	def act( self, level):
		return None

	def getCollisions(self, level):
		return self.hitHexagon.getCollisions(self.getMidPos(), level)

	def hurt(self, damage):
		self.hp = max(self.hp - damage, 0)
	def heal(self, heal):
		self.hp = min(self.hp + heal, self.maxHP)
