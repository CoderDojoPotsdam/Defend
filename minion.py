from kivy.uix.image import Image

class Minion:
	def __init__(self):
		self.__health = 100
		self.position = []
		self.image = Image(source = "icons/minion.png")

	def update(self,*args):
		if args[0]=="hit":
			pass
		elif args[0] == "move":
			self.image.x += args[1][0]
			self.image.y += args[1][1]
