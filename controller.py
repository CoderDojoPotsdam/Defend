# controller
import window

class Observer:

	def update(self, *args, object):
		# Verfügbare Befehle sind:
		# - "add" + object
		pass


class Controller(Observer):
	def __init__(self):
		self.window = window.AppWindow()
		self.window.init()

	def run(self):
		self.window.run()

	def update(self, command, object):
		# update something
		# Beispiel: controller.update("minion", "goto", [0,4, 0,2])
		if command == "close":
			self.window.close()
		elif command == "add":
			self.window.add(object)
