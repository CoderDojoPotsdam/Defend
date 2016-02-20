# Fensterverwaltung

import kivy
import kivy.app
import kivy.uix.button
from kivy.core.window import Window as win

class Window(kivy.app.App):
	# Fenster icon und Title
	icon = "icon.png"
	title = "Defend"


	def build(self):
		# Fenster erstellen
		win.size = (640, 480)
		return kivy.uix.button.Button(text = "test", size_hint = (0.5, 0.25))

	def close(self):
		win.close()
