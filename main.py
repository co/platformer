#!/usr/bin/python2.7
import pygame, sys, Player, HitHexagon, Level, Globals, Tileset, SpriteSheet
import Camera, Bar, PowerUp, Game

pygame.init()
pygame.display.set_caption('LOL ITS A GAEM')


def loadLevelOne():
#Level
	tileset = Tileset.Tileset("tileset")
	level = Level.Level(tileset)
	level.loadFile("world1.map")

#Player
	spriteSheet = SpriteSheet.SpriteSheet("spriteSheet1.png")
	player = Player.Player(spriteSheet)
	player.setPos((64,16))
	sprites = []
	sprites.append(player)

	camera = Camera.Camera(player.pos, Globals.PIXELSIZE)

	game = Game.Game(level, player, camera, Globals.CANVAS)

#PowerUps
	heart = PowerUp.PowerUp("heart.png", game, (128,128), (9,8))
	game.powerUps.append(heart)

	game.start()

loadLevelOne()
