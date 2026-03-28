import datetime
import os

def loguj(urzadzenie, wiadomosc):
    os.makedirs('logs', exist_ok=True)
    teraz = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    linia = f"{teraz} | {urzadzenie} | {wiadomosc}"
    print(linia)
    with open('logs/log.txt', 'a') as f:
        f.write(linia + '\n')