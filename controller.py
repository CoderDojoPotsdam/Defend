# controller
import window

class Observer:

	def update(self, *args, **kwargs):
		# Verfügbare Befehle sind:
		# - "add" + object
		pass

class Controller(Observer):
	def __init__(self):
		self.window = window.Window()

	def __del__(self):
		pass

	def run(self):
		self.window.run()


	def update(self, command, **kwargs):
		# update something
		# Beispiel: controller.update("minion", "goto", [0,4, 0,2])
		pass
