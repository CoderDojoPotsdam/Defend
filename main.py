#!/usr/bin/env python3.4
# Defend
#
# a simple pvp game
import kivy
from kivy.uix.button import Button
import sys, controller


kivy.require("1.9.2")

def main(argv):
	game = controller.Controller()
	game.update("add", Button(text="Test"))
	game.run()

if __name__ == "__main__":
	main(sys.argv)