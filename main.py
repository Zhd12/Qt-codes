import socket
import time
import random

target_ip = "127.0.0.1"
target_port = 5000
bitRate = 1_000_000
bytes_per_second = bitRate / 8
chunk_size = 1024
delay = chunk_size / bytes_per_second

def send_stream_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((target_ip, target_port))
    print("Sending NON-ZERO data at ~1 Mbps")
    while True:
        data = bytes(random.randint(1, 255) for _ in range(chunk_size))
        sock.send(data)
        time.sleep(delay)

send_stream_data()
