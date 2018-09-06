import socket
from os import system
from platform import system as cek
port = "1030"
def listen(port=None):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Menunggu koneksi ke Port: " + str(port)
        server.bind(("127.0.0.1", int(port)))
        server.listen(1)
        k, ip = server.accept()
        print "Terkoneksi ke: {}".format(ip)
        data = k.recv(1080)
        print "Data Terima: \n", data
        k.send("HTTP/1.0 200 OK\n")
        k.send("Content-Type: text/html\n")
        k.send("\n")
        k.send("SOLVED")
    except socket.error:
        print "Port sebelumnya masih berjalan"
        print "Menutup proxy yang sama"
        if cek() == "Windows":
            print system("""netstat -aon | find /i "{}" """.format(port))
            server.close()
while 1:
    proxy = listen(port=port)
