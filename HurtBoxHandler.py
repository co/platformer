ALIGNMENT_PLAYER = 0
ALIGNMENT_ENEMY  = 1
ALIGNMENT_LEVEL  = 2

NUMBEROFALIGNMENTS = 3

class HurtBoxHandler:
	def __init__(self):
		self.hurtBoxes = [[] for a in range(NUMBEROFALIGNMENTS)]

	def addHurtBox(self, hurtBox, alignment):
		self.hurtBoxes[alignment].append(hurtBox)
	
	def checkAndHurt(self, sprite):
		self.hurtBoxes[sprite.alignment] = [hb for hb in self.hurtBoxes[sprite.alignment] if (not hb.framesToLive == 0)]
		for alignment in range(NUMBEROFALIGNMENTS):
			if (NUMBEROFALIGNMENTS == sprite.alignment): next
			for self.hurtBox in self.hurtBoxes[alignment]:
				self.hurtBox.checkAndHurt(sprite)
				self.hurtBox.tick()

