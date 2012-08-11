#!/usr/bin/python2.7
import pygame, sys, Player, HitHexagon, Level, Globals, Tileset, SpriteSheet
import Camera, Bar, PowerUp
from pygame.locals import *

class Game( object ):

	def __init__( self, level, player, camera, canvas):
		self.level = level
		self.sprites = []
		self.powerUps = []
		self.sprites.append(player)
		self.camera = camera
		self.canvas = canvas
		self.player = player
		self.guiFeatures = []
		self.guiFeatures.append(Bar.Bar("hpbar.png", (8,8), 20))


	def reactToCollision(self, sprite, collisions):
		if(collisions[HitHexagon.LEFT] and collisions[HitHexagon.RIGHT]):
			print "You got crushed by walls"
		if(collisions[HitHexagon.TOP] and collisions[HitHexagon.BOTTOM]):
			print "You got crushed by walls"
		
		if(collisions[HitHexagon.LEFT]):
			sprite.velocity = (0,sprite.velocity[1])
			sprite.addPos((0.5,0))

		if(collisions[HitHexagon.RIGHT]):
			sprite.velocity = (0,sprite.velocity[1])
			sprite.addPos((-0.5,0))

		if(collisions[HitHexagon.TOP]):
			sprite.velocity = (sprite.velocity[0],0)
			sprite.addPos((0,0.1))

		if(collisions[HitHexagon.BOTTOM]):
			sprite.velocity = (sprite.velocity[0],0)
			sprite.addPos((0,-0.1))

# draw on the surface object

	def act(self):
		for sprite in self.sprites:
			sprite.act(self.level)

	def collisionHandler(self):
		for sprite in self.sprites:
			for i in range(200):#try a fixed amount of time to push the sprite
				#out of walls
				collisions = sprite.getCollisions(self.level)
				if(any(collisions)):
					self.reactToCollision(sprite, collisions)
				else:
					break

	def addGravity(self):
		for sprite in self.sprites:
			if(sprite.isInAir(self.level)):
				sprite.addVelocity((0,Globals.GRAVITY))

	def drawDebugText(self, canvas):
		font = pygame.font.Font(None, 24)
		text1 = font.render("velocity " + "(%1s,%1s)," % self.player.velocity, 1, (10, 10, 10))
		text2 = font.render("position " + "(%1s,%1s)," % self.player.pos, 1, (10, 10, 10))
		canvas.blit(text1, (20,20))
		canvas.blit(text2, (20,40))

	def drawFrame(self, canvas):
		levelCanvas = pygame.Surface((1000, 1000))
		levelCanvas.fill(Globals.SKY)

		self.level.draw(levelCanvas)

		for power in self.powerUps:
			power.draw(levelCanvas)

		for sprite in self.sprites:
			sprite.draw(levelCanvas, self.level)
		if(Globals.DEBUG):
			drawDebugText(self.sprites[0])
		frameCanvas = pygame.Surface(Globals.PIXELSIZE)
		frameCanvas.blit(levelCanvas, (0,0), self.camera.cameraRect)

		for guiElement in self.guiFeatures:
			guiElement.draw
		
		scaledCanvas = pygame.transform.scale(frameCanvas, Globals.SCREENSIZE)
		canvas.blit(scaledCanvas, (0,0))

	def updatePowerups(self):
		for power in self.powerUps:
			power.update()

	def start(self):
		self.player.game = self
		while True: # main game loop
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			self.camera.updateCameraPos(self.player.getMidPos())
			self.addGravity()
			self.collisionHandler()
			self.act()
			self.updatePowerups()
			self.drawFrame(self.canvas)

			pygame.display.update()
			Globals.FPSCLOCK.tick(Globals.FPS)
			Globals.FRAMECOUNT +=1

