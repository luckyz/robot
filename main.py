#!/usr/bin/python
# coding=utf-8
from gpiozero import Robot, LED
import serial
import curses
from time import sleep


robot = Robot(left=(6, 13), right=(19, 26))
left_light = LED(18)
right_light = LED(21)
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
				directions[int(key)][0]
				text = directions[int(key)][1]
				stdscr.addstr(" {0}{1}".format(text, ' ' * 7))
				stdscr.refresh()

				if key == 259:
					robot.backward(speed=0.6)
				elif key == 258:
					robot.forward(speed=1)
				elif key == 260:
					robot.right(speed=0.5)
					left_light.off()
					right_light.blink(on_time=0.4, off_time=0.4)
				elif key == 261:
					robot.left(speed=0.5)
					left_light.blink(on_time=0.4, off_time=0.4)
					right_light.off()
				elif key == 32:
					robot.stop()
					left_light.on()
					right_light.on()
				# returns cursor to actual position
				stdscr.move(0, 0)

	except Exception as e:
		import pudb; pudb.set_trace()
		print str(e)
	finally:
		pass

if __name__ == '__main__':
	curses.wrapper(main)
