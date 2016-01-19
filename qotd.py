"""Script to impliment QotD (RFC865) in Python3."""
import sys
import socket
import csv
import random

def getQuote():
	with open('quotes_all.csv', 'r') as allQuotes:
		quotes = list(csv.reader(allQuotes, delimiter=';'))
		randomQuote = random.choice(quotes)
		quote = randomQuote[0] + "\n – " + randomQuote[1]
		quote = quote.encode()
		print (quote)
		return quote

def main():
    """Main entry point for the script."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket object
    host = socket.gethostname()	# Get local machine name
    port = 17				# Reserve a port for your service.
    s.bind((host, port))		# Bind to the port

    s.listen(5)					# Now wait for client connection.
    while True:
        (clientsocket, address) = s.accept()		# Establish connection with client.
        print('Got connection from', address)
        clientsocket.send(getQuote())				# Get a random quote!
        clientsocket.close()						# Close the connection
        pass

if __name__ == '__main__':
    sys.exit(main())
