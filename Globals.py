import pygame, SoundPlayer
WIDTH = 16
HEIGHT = 12
GRAVITY = 0.2
DEBUG = False
TILESIZE = 16
SCREENMULTIPLIER = 3
SCREENSIZE = (WIDTH*TILESIZE*SCREENMULTIPLIER,
	HEIGHT*TILESIZE*SCREENMULTIPLIER)
PIXELSIZE = (WIDTH*TILESIZE, HEIGHT*TILESIZE)
CANVAS = pygame.display.set_mode(SCREENSIZE)
FRAMECOUNT = 0

SOUNDPLAYER = SoundPlayer.SoundPlayer()
FPSCLOCK = pygame.time.Clock()

FPS = 60
# set up the colors
SKY = (0x6d, 0xc2, 0xca)
