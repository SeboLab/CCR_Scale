import socket

import csv

def Main():

    # ip address for other computer (not in a virtual machine)
    server_ip = '' # Put IP Address for personal laptop Mac here
    server_port = 4000
    
    server = (server_ip, server_port)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Type the word "address" in this prompt to let the server know how to send messages to this computer
    message = input("-> ")
    s.sendto(message.encode('utf-8'), server)

    # Makes sure the server got the above message. Should print out "Recieved from server: ADDRESS" twice
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    print("Received from server: " + data)

    read_value = 0

    while True:

        # Reads the current value of displaynumber.csv
        with open('displaynumber.csv',newline='') as file:
            reader = csv.reader(file, delimiter=',',quotechar='"')
            for row in reader:
                read_value = row[0]

        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)

        # Writes what it recieved to a csv file that is read by display.py
        with open("displaynumber.csv", "w",newline='') as filewrite:
            csvwriter = csv.writer(filewrite)
            csvwriter.writerow([data])

        # Sends a message to the server if the slide changes
        if read_value != data:
            s.sendto("slidechange".encode('utf-8'), server)
    
    s.close()

if __name__=='__main__':
    Main()

