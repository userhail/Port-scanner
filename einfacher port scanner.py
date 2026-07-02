import socket

target = "127.0.0.1"

ports = [21, 22, 80, 443, 8080]

print(f"Scannning {target}...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} ist offen")
    else:
        print(f"Port {port} ist geschlossen")

        s.close()
    