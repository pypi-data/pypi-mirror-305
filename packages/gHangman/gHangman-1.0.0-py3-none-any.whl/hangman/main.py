from . import efx
from .sides import LoginSetup
from .game import Menu

def start():
	input(efx.Printer(efx.intro,delay=0.0005))

	LoginSetup()

	Menu()
