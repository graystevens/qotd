"""Script to impliment QotD (RFC865) in Python3."""
import sys
import socket

def main():
    """Main entry point for the script."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
    host = socket.gethostname()	# Get local machine name
    port = 17					# Reserve a port for your service.
    s.bind((host, port))		# Bind to the port

    s.listen(5)					# Now wait for client connection.
    while True:
        c, addr = s.accept()	# Establish connection with client.
        print('Got connection from', addr)
        c.send(b'Thank you for connecting')
        c.close()				# Close the connection
        pass

if __name__ == '__main__':
    sys.exit(main())
