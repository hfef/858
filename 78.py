import socket
import os
import time
def ping(host):
    try:
        ip = socket.gethostbyname(host)
        start_time = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, 80))
        end_time = time.time()
        print(f'Ping to {host} took {(end_time - start_time)*1000} ms')
    except (socket.gaierror, socket.timeout, ConnectionRefusedError) as e:
        print(f'Ping to {host} failed: {str(e)}')
ping('www.tiktok.com') 