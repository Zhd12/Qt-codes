import socket
import time

target_ip = "127.0.0.1"
target_port = 5000
bitRate = 1_000_000
bytes_per_second = bitRate / 8
chunk_size = 1024
delay = chunk_size / bytes_per_second

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect((target_ip, target_port))
print("Sending NON-ZERO data at ~1 Mbps")

def generate_sawtooth_signal(max_value=2048):
    value = 0
    while True:
        yield value
        value += 1
        if value > max_value:
            value = 0

def int_to_bytes(value: int) -> bytes:
    return value.to_bytes(2, byteorder='big', signed=False)

pack = generate_sawtooth_signal()

while True:
    data = next(pack)
    # print(data)
    byte_data = int_to_bytes(data)
    # print(byte_data)
    sock.send(byte_data)
    time.sleep(delay)
