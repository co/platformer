import pygame, sys, SpriteSheet, HitHexagon, Level, Globals, soundplay, math
import Entity, HurtBox, HurtBoxHandler, random, VectorMath, Attack, Enemy

SHOTCOOLDOWN = 30
class BlackGhost( Enemy.Enemy):
	def __init__(self, spriteSheet, game):
		super(BlackGhost, self).__init__(spriteSheet, game)

	def generateProjectile(self, pos):
		shotLifeLength = 200
		shotSpeed = 1
		attack = Attack.Attack("shot.png", self.game, pos, (4,4))
		attack.damage = 5
		attack.velocity = VectorMath.normalize(VectorMath.sub
				(self.game.player.getMidPos(),self.getMidPos()),shotSpeed)
		attack.framesToLive = shotLifeLength
		return attack

	def attack(self):
		if(self.shotCoolDown == 0):
			distance = self.distanceToPoint(self.game.player.getMidPos())
			shotInitPos = VectorMath.add(self.pos, (6,3))
			self.game.simpleSprites.append(self.generateProjectile(shotInitPos))
			self.shotCoolDown = SHOTCOOLDOWN
			Globals.SOUNDPLAYER.playSound("shoot.wav")
		if(self.shotCoolDown >= 1):
			self.shotCoolDown -=1

	def distanceToPoint(self, point):
		return VectorMath.magnitude((VectorMath.sub(self.pos,point)))

	def act( self, level):
		distance = self.distanceToPoint(self.game.player.getMidPos())
		if(distance > 256):
			speed = 0
		elif(distance > 80):
			self.attack()
			speed = 1
		elif(distance > 64):
			self.attack()
			speed = 0
			if(random.randrange(10) == 0):
				self.moveRandom()
		elif(distance > 32):
			speed = -2
		else:
			speed = -3

		self.move(speed)

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

