#coding:UTF-8
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def work_thread(connection, addr):
    while True:
        str1 = connection.recv(1024).decode('utf8')
        if (str1[0:4] != "exit"):
            str1 = str1[::-1]
            connection.send(str1.encode('utf8'))
        else:
            print 'Disconnect frome', addr
            break
    connection.close()


def main():
    host = '127.0.0.1'
    port = 3333
    s.bind((host, port))
    s.listen(15)

    while True:
        c, addr = s.accept()
        print 'Connect', addr
        thread = threading.Thread(target=work_thread, args=(c,addr))
        thread.start()
if __name__ == '__main__':
    main()