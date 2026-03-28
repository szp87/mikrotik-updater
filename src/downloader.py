import requests
import os

PACZKI = ['routeros', 'wifi-qcom', 'dude']

def pobierz_image(wersja, architektura, folder='images'):
    os.makedirs(folder, exist_ok=True)
    pobrane = []

    for paczka in PACZKI:
        if paczka == 'routeros':
            nazwa_pliku = f"routeros-{wersja}-{architektura}.npk"
        else:
            nazwa_pliku = f"{paczka}-{wersja}-{architektura}.npk"

        url = f"https://download.mikrotik.com/routeros/{wersja}/{nazwa_pliku}"
        sciezka = os.path.join(folder, nazwa_pliku)

        if os.path.exists(sciezka):
            print(f"Plik juz istnieje: {sciezka}")
            pobrane.append(sciezka)
            continue

        print(f"Pobieranie {nazwa_pliku}...")
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(sciezka, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print(f"Pobrano: {sciezka}")
        pobrane.append(sciezka)

    return pobrane
