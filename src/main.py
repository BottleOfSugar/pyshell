import string
import numpy
import random
import subprocess
import colorama as clr
from colorama import *
import os
user = os.getlogin()
ascii_arts = [
    """
======================|
   .--.               
  |o_o | 
  |:_/ | 
 //   \ \ 
(|     | )
/'\_   _/`\
\___)=(___/
======================
    """,
]
while True:
    command = input(f"local:{user} > ")
    if command == "exit":
        break
    else:
        subprocess.run(command)
        










