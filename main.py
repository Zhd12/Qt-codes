import socket
import time

target_ip = "127.0.0.1"
target_port = 5000
bitRate = 1_000_000  # 1 mega bit per second
bit_per_second = bitRate / 8  # 125'000 bit per second
chunk_size = 1024
delay = chunk_size / bit_per_second  # time between packets

def send_stream_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((target_ip, target_port))
    data = b'0' * chunk_size
    print(f"Sending data at ~1 Mbps to {target_ip}:{target_port} ...")

    while True:
        sock.send(data)
        time.sleep(delay)  # control bitrate

send_stream_data()
