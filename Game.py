#!/usr/bin/python2.7
import pygame, sys, Player, HitHexagon, Level, Globals, Tileset, SpriteSheet
import Camera, Bar, PowerUp, HurtBoxHandler, Attack
from pygame.locals import *

class Game( object ):

	def __init__( self, level, player, camera, canvas):
		self.level = level
		self.entities = []
		self.simpleSprites = []
		self.entities.append(player)
		self.camera = camera
		self.canvas = canvas
		self.player = player
		self.guiFeatures = []
		self.hurtBoxHandler = HurtBoxHandler.HurtBoxHandler()

# draw on the surface object

	def act(self):
		for entity in self.entities:
			entity.act(self.level)

	def collisionHandler(self):
		for entity in self.entities:
			for i in range(200):#try a fixed amount of time to push the entity
				#out of walls
				collisions = entity.getCollisions(self.level)
				if(any(collisions)):
					entity.reactToCollision(collisions)
				else:
					break

	def addGravity(self):
		for entity in self.entities:
			if(entity.isInAir(self.level)):
				entity.addVelocity((0,Globals.GRAVITY))

	def drawDebugText(self, canvas):
		font = pygame.font.Font(None, 24)
		text1 = font.render("velocity " + "(%1s,%1s)," % self.player.velocity, 1, (10, 10, 10))
		text2 = font.render("position " + "(%1s,%1s)," % self.player.pos, 1, (10, 10, 10))
		canvas.blit(text1, (20,20))
		canvas.blit(text2, (20,40))

	def drawFrame(self, canvas):
		levelCanvas = pygame.Surface((1000, 1000))
		levelCanvas.fill(Globals.SKY)

		self.level.draw(levelCanvas, self.player.pos)


		for entity in self.entities:
			entity.draw(levelCanvas, self.level)

		for sprite in self.simpleSprites:
			sprite.draw(levelCanvas)

		if(Globals.DEBUG):
			self.drawDebugText(self.entities[0])
		frameCanvas = pygame.Surface(Globals.PIXELSIZE)
		frameCanvas.blit(levelCanvas, (0,0), self.camera.cameraRect)

		for guiElement in self.guiFeatures:
			guiElement.draw(frameCanvas)
		
		scaledCanvas = pygame.transform.scale(frameCanvas, Globals.SCREENSIZE)
		canvas.blit(scaledCanvas, (0,0))

	def updateSimpleSprites(self):
		self.simpleSprites = [s for s in self.simpleSprites if not s.toBeRemoved]
		for sprite in self.simpleSprites:
			sprite.update()

	def updateHurtBoxes(self):
		for entity in self.entities:
			self.hurtBoxHandler.checkAndHurt(entity)

	def start(self):
		self.player.game = self
		while True: # main game loop
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			if(self.player.hp == 0):
				self.winning = False
				break

			self.camera.updateCameraPos(self.player.getMidPos())
			self.addGravity()
			self.collisionHandler()
			self.act()
			self.updateSimpleSprites()
			self.drawFrame(self.canvas)
			self.updateHurtBoxes()

			pygame.display.update()
			Globals.FPSCLOCK.tick(Globals.FPS)
			Globals.FRAMECOUNT +=1

