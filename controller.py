# -*- coding: utf-8 -*-
from kivy.clock import Clock
import window

class Observer:
	def __init__(self):
		pass

	def update(self, *args):
		# Verf�gbare Befehle sind:
		# - "add" + object
		pass

class Controller(Observer):

	def __init__(self):
		self.window = window.AppWindow()
		self.window.init()

		self.minions = []

		Clock.schedule_interval(self.loop, 1/30)

	def run(self):
		self.window.run()

	def update(self, *command):
		# update something
		# Beispiel: controller.update("minion", "goto", [0,4, 0,2])
		if command[0] == "close":
			self.window.close()
		elif command[0] == "add":
			self.window.add(command[1])

	def loop(self, dt):
		for i in self.minions:
			i.update()

