#!/usr/bin/python2.7
import pygame, sys, Player, HitHexagon, Level, Globals, Tileset
from pygame.locals import *

pygame.init()

tileset = Tileset.Tileset("tileset")

def reactToCollision(sprite, collisions):
	if(collisions[HitHexagon.LEFT] and collisions[HitHexagon.RIGHT]): sys.exit(0)
	if(collisions[HitHexagon.TOP] and collisions[HitHexagon.BOTTOM]): sys.exit(0)
	
	if(collisions[HitHexagon.LEFT]):
		sprite.velocity = (0,sprite.velocity[1])
		sprite.addPos((0.1,0))

	if(collisions[HitHexagon.RIGHT]):
		sprite.velocity = (0,sprite.velocity[1])
		sprite.addPos((-0.1,0))

	if(collisions[HitHexagon.TOP]):
		sprite.velocity = (sprite.velocity[0],0)
		sprite.addPos((0,0.1))

	if(collisions[HitHexagon.BOTTOM]):
		sprite.velocity = (sprite.velocity[0],0)
		sprite.addPos((0,-0.1))


FLOORHEIGHT = Globals.HEIGHT/6

FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('LOL ITS A GAEM')

FPS = 60
# set up the colors
SKY = (0x6d, 0xc2, 0xca)

# draw on the surface object

player = Player.Player("dude.png")
player.setPos((64,16))

sprites = []
sprites.append(player)

level = Level.Level(tileset)
level.loadFile("world1.map")

def act( sprites, level ):
	for sprite in sprites:
		sprite.act(level)

def collisionHandler(sprites, level):
	for sprite in sprites:
		for i in range(100):#try a fixed amount of time to push the sprite
			#out of walls
			collisions = sprite.getCollisions(level)
			if(any(collisions)):
				reactToCollision(sprite, collisions)
			else:
				break

def addGravity(sprites, level):
	for sprite in sprites:
		if(sprite.isInAir(level)):
			sprite.addVelocity((0,Globals.GRAVITY))

def drawDebugText(player):
	font = pygame.font.Font(None, 24)
	text1 = font.render("velocity " + "(%1s,%1s)," % player.velocity, 1, (10, 10, 10))
	text2 = font.render("position " + "(%1s,%1s)," % player.pos, 1, (10, 10, 10))
	Globals.CANVAS.blit(text1, (20,20))
	Globals.CANVAS.blit(text2, (20,40))

def drawFrame(canvas, sprites, level):
	Globals.CANVAS.fill(SKY)

	level.draw(Globals.CANVAS)

	for sprite in sprites:
		sprite.draw(Globals.CANVAS)
	if(Globals.DEBUG):
		drawDebugText(sprites[0])
	
frame = 0
while True: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	drawFrame(Globals.CANVAS, sprites, level)
	addGravity(sprites, level)
	collisionHandler(sprites, level)
	act( sprites, level )

	pygame.display.update()
	FPSCLOCK.tick(FPS)
	frame +=1
	#print "END OF FRAME: ", frame
pygame.display.update()

