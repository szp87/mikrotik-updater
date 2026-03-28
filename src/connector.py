import paramiko

def sprawdz_wersje(host, user, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=user, password=password)
    stdin, stdout, stderr = client.exec_command('/system resource print')
    output = stdout.read().decode()
    client.close()

    for linia in output.splitlines():
        if 'version' in linia:
            wersja = linia.split(':')[1].strip()
            return wersja.split(' ')[0]

    return None

