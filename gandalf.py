import os
import time
import sys
import random


run = True
banner = """
            _
           / \
          /   \
         /_   _\
        /_     _\
        /_______\
           | |
           | |
           | |

G   A   N   D   A   L   F



"""
print(banner)

while run == True:
  terminal = input("$> ")
  if terminal == "list spells":
    print(isfile(join("/spells", f))
