#!/usr/bin/python
# coding=utf-8
from gpiozero import Robot
import serial
import curses
from time import sleep


robot = Robot(left=(6, 13), right=(19, 26))
directions = {
	259: 	[robot.forward(), "Forward..."],
	258: 	[robot.backward(), "Backbard..."],
	260: 	[robot.left(), "Turning left..."],
	261: 	[robot.right(), "Turning right..."],
	32: 	[robot.stop(), "Stopped"],
}

def main(stdscr):
	try:
		# no wait for input
		stdscr.nodelay(1)
		while True:
			# gets keyboard input. returns -1 if unavailable
			# curses.halfdelay(1)
			key = stdscr.getch()
			if key != -1:
				text = directions[int(key)][1]
				stdscr.addstr(" {0}{1}".format(text, ' ' * 7))
				stdscr.refresh()

				if key == 259:
					robot.forward()
				elif key == 258:
					robot.backward()
				elif key == 260:
					robot.right()
				elif key == 261:
					robot.left()
				elif key == 32:
					robot.stop()
				# returns cursor to actual position
				stdscr.move(0, 0)

	except Exception as e:
		import pudb; pudb.set_trace()
		print str(e)
	finally:
		pass

if __name__ == '__main__':
	curses.wrapper(main)
