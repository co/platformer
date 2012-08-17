import pygame, sys, SpriteSheet, HitHexagon, Level, Globals, soundplay, math
import Entity, HurtBox, HurtBoxHandler, random, VectorMath, Attack

SHOTCOOLDOWN = 30

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

	def generateProjectile(self, pos):
		shotSpeed = 1
		attack = Attack.Attack("shot.png", self.game, pos, (4,4))
		attack.damage = 5
		attack.velocity = VectorMath.normalize(VectorMath.sub
				(self.game.player.getMidPos(),self.getMidPos()),shotSpeed)
		return attack

	def attack(self):
		distance = self.distanceToPoint(self.game.player.getMidPos())
		shotInitPos = VectorMath.add(self.pos, (6,3))
		if(self.shotCoolDown == 0 and distance < 80):
			self.game.simpleSprites.append(self.generateProjectile(shotInitPos))
			self.shotCoolDown = SHOTCOOLDOWN
		if(self.shotCoolDown >= 1):
			self.shotCoolDown -=1

	def distanceToPoint(self, point):
		return VectorMath.magnitude((VectorMath.sub(self.pos,point)))

	def act( self, level):
		distance = self.distanceToPoint(self.game.player.getMidPos())
		if(distance > 256):
			speed = 0
		elif(distance > 64):
			speed = 1
		elif(distance > 48):
			speed = 0
			if(random.randrange(10) == 0):
				self.moveRandom()
		elif(distance > 32):
			speed = -2
		else:
			speed = -3

		self.move(speed)

		self.attack()

	def moveRandom(self):
		UP = 0
		DOWN = 1
		LEFT = 2
		RIGHT = 3
	
		speed = 1

		choices = [UP, DOWN, LEFT, RIGHT]
		decision = random.choice(choices)

		if(decision == UP):
			self.pos = (self.pos[0], self.pos[1] -speed)
		if(decision == DOWN):
			self.pos = (self.pos[0], self.pos[1] +speed)
		if(decision == LEFT):
			self.pos = (self.pos[0] -speed, self.pos[1])
		if(decision == RIGHT):
			self.pos = (self.pos[0] +speed, self.pos[1])


	def move(self, speed):
			if(speed == 0):
				return

			sx = self.pos[0]
			sy = self.pos[1]

			px = self.game.player.pos[0]
			py = self.game.player.pos[1]

			if(sx > px): sx -= speed
			if(sx < px): sx += speed
			if(sy > py): sy -= speed
			if(sy < py): sy += speed

			if(sy >= py): sy -= 1

			self.pos = (sx,sy)


	def getCollisions(self, level):
		return self.hitHexagon.getCollisions(self.getMidPos(), level)
