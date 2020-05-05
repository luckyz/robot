#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
import serial
import curses
#from time import sleep


GPIO.setmode(GPIO.BOARD) # Physical numeration pins
direcciones = {
	259: ("a", "Avanzando..."),
	258: ("r", "Retrocediendo..."),
	260: ("di", "Izquierda..."),
	261: ("dd", "Derecha..."),
}

def main(stdscr):
	try:
		# define el puerto a utilizar
		# ser = ser = serial.Serial('/dev/cu.usbmodem1411', 9600) # for Mac OS X
		ser = serial.Serial('/dev/ttyACM0', 9600) # for Raspberry Pi

		# no espera por el ingreso cuando es llamado
		stdscr.nodelay(1)
		while True:
			# obtiene entrada por teclado, devuelve -1 en caso de no disponible
			c = stdscr.getch()
			if c != -1:
				comando, texto = direcciones[int(c)]
				# imprime un valor numerico
				stdscr.addstr(" {0}{1}".format(texto, ' ' * 7))
				stdscr.refresh()
				# devuelve el cursor a la posicion inicial
				stdscr.move(0, 0)
				# envia el comando a Arduino a traves del puerto COM
				ser.write(comando)

	except Exception as e:
		print str(e)
	finally:
		GPIO.cleanup()

if __name__ == '__main__':
	curses.wrapper(main)
