import soundplay, threading, time

class SoundThread( threading.Thread ):
	def __init__(self):
		self.nextSound = None
		super(SoundThread, self).__init__()

	def run(self):
		while True:
			while(self.nextSound == None):
				time.sleep(0) #yield
			soundplay.playsound(self.nextSound)
			self.nextSound = None

class SoundPlayer( object ):
	def __init__(self):
		self.soundThread = SoundThread()
		self.soundThread.daemon=True
		self.soundThread.start()

	def playSound(self, soundFile):
		self.soundThread.nextSound = soundFile
