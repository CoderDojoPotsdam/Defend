#!/usr/bin/env python3.4
# Defend
#
# a simple pvp game
import kivy
import sys, controller, minion


kivy.require("1.9.2")

def main(argv):
	game = controller.Controller()
	mini = minion.Minion()
	game.update("addFloppy", mini)
	game.run()

if __name__ == "__main__":
	main(sys.argv)