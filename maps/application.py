import socket


def connect_to_application(host, port, keywords):
    send_keywords = ','.join(keywords)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(send_keywords)
    print 'Sent: ' + send_keywords
    received = s.recv(1024)
    s.close()
    print 'Received', repr(received)
