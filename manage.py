from manage.commands import *
import sys


commands = Commands()
arg = sys.argv
commands.startProject( arg[1] )