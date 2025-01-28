import socket

ready = False

def Main():
   
    host = '0.0.0.0' #Server ip
    port = 4000

    second_port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    servertolaptop = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servertolaptop.bind((host, second_port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')

        if data == "slidechange":
            print("Slide changed")
        else:
            print("Message from: " + str(addr))
            print("From connected user: " + data)
            data = data.upper()
            print("Sending: " + data)
            s.sendto(data.encode('utf-8'), addr)
            
            print(data)

            if data == "ADDRESS":
                displayaddr = addr
                ready = True
                print("reached")

            if ready == True:
                servertolaptop.sendto(data.encode('utf-8'), displayaddr)
                print("reached2")

    s.close()

if __name__=='__main__':
    Main()
