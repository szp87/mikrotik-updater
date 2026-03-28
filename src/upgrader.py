import paramiko
import os
import time

def wykonaj_upgrade(host, user, password, pliki):
    # wysylanie plikow
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password)

    sftp = client.open_sftp()
    for plik in pliki:
        nazwa = os.path.basename(plik)
        print(f"Wysylanie {nazwa} na {host}...")
        sftp.put(plik, f"/{nazwa}")
    sftp.close()

    # reboot
    print(f"Wykonywanie reboot na {host}...")
    client.exec_command('/system reboot')
    client.close()

    # czekanie az router wróci
    print(f"Czekam az {host} sie podniesie...")
    time.sleep(30)

    for i in range(10):
        try:
            client2 = paramiko.SSHClient()
            client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client2.connect(host, username=user, password=password, timeout=5)
            client2.close()
            print(f"{host} jest z powrotem online")
            return True
        except Exception:
            print(f"Czekam... ({i+1}/10)")
            time.sleep(15)

    print(f"Router {host} nie wrócił w czasie")
    return False