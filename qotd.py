"""Script to impliment QotD (RFC865) in Python3."""
import sys
import socket
import csv
import random
import textwrap
import select

def getQuote():
    with open('quotes_all.csv', 'r') as allQuotes:
        quotes = list(csv.reader(allQuotes, delimiter=';'))
        randomQuote = random.choice(quotes)
        quote = textwrap.fill(randomQuote[0], width=60)
        quote = quote + "\n\t\t\t – " + randomQuote[1]
        quote = quote.encode()
        return quote

def tcpCon(connection):
    (clientsocket, address) = connection.accept()# Establish connection with client.
    print('Got TCP connection from', address)
    clientsocket.send(getQuote())				# Get a random quote!
    clientsocket.close()						# Close the connection

def udpCon(connection):
    (data, address) = connection.recvfrom(1)# Establish connection with client.
    print('Got UDP connection from', address)
    connection.sendto(getQuote(),address)               # Get a random quote!

def main():
    #Main entry point for the script.
    #Set some initial variables, applying to both sockets
    port = 17
    backlog = 5
    host = socket.gethostname()	# Get local machine name

    #Setup TCP socket
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind((host, port))		# Bind to the port
    tcp.listen(backlog)

    #Setup UDP socket
    udp =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((host, port))

    choice = [tcp,udp]

    while True:
        inselect,outselect,exceptselect = select.select(choice,[],[])

        for connection in inselect:
            if connection == tcp:
                tcpCon(connection)
            elif connection == udp:
                udpCon(connection)
            else:
                print("Error!")
        

if __name__ == '__main__':
    sys.exit(main())
