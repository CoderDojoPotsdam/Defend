# -*- coding: utf-8 -*-
import kivy.app
from kivy.core.window import Window
from kivy.uix.floatlayout import  FloatLayout

size = (640, 480)

class AppWindow(kivy.app.App):
	#Icon und Title
	icon = "icon.png"
	title = "Defend"

	def init(self):
		self.root = FloatLayout()

	# Fenster erstellen
	def build(self):
		Window.size = size

	# Objekte hinzuf�gen
	def add(self, new):
		self.root.add_widget(new)

	# Objekte entfernen
	def remove(self, toRemove):
		self.root.remove_widget(toRemove)