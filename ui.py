#!/usr/bin/python

from curses import wrapper
from ux import MainScreen


app = MainScreen()

if __name__ == '__main__':
	wrapper(app.run)
