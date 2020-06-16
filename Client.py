import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 2048
# send 4096 bytes each time step
# the ip address or hostname of the server, the receiver
host = socket.gethostbyname(socket.gethostname())
# the port, let's use 5001
port = 5001
# the name of file we want to send, make sure it exists
# filename = r'C:\Users\GAUTAM\Documents\edited.mp4'
# get the file size

s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")


def send(filename):
    filesize = os.path.getsize(filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())

    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "rb") as f:
        for _ in progress:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transmission in
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))


def text():
    with open("change.txt", 'r') as f:
        return f.read()


first = text()
while True:
    now = text()
    if now != first:
        print('change')
        print(now)
        first = now
