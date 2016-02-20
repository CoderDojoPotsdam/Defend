# controller

class Observer:
	@abstactmethod
	def update(self, *args, **kwargs):
		pass

class Controller(Observer):
	def __init__(self):
		pass

	def __del__(self):
		pass


	def update(self, command, **kwargs):
		# update something
		# Beispiel: controller.update("minion", "goto", [0,4, 0,2])
		pass
