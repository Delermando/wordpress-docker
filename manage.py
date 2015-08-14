from manage.commands import *
import sys


commands = Commands()
arg = sys.argv
commands.creatProject( arg[1] )