import pyfiglet
from termcolor import cprint
import sys
import datetime

now = datetime.datetime.now()
current_time = now.strftime("%H:%M")
date = now.strftime("%d/%m/%Y")
result = pyfiglet.figlet_format(date+ '\n' + current_time ) 

dateTime = result.split('\n')
for i,item in enumerate(dateTime):
    if((i % 4) == 0):
        cprint(item, 'light_green', attrs=['bold'])
    elif((i % 4) == 1):
        cprint(item, 'blue', attrs=['bold'])
    elif((i % 4) == 2):
        cprint(item, 'yellow', attrs=['bold'])
    else:
        cprint(item, 'light_cyan', attrs=['bold'])
