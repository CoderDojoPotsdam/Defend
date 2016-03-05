from kivy.uix.image import Image

class Minion:
	def __init__(self):
		self.__health = 100
		self.image = Image(source = "icons/minion.png")

	def update(self,*args):
		if args[0]=="hit":
			pass
