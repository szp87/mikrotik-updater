import yaml
from src.scraper import pobierz_wersje
from src.connector import sprawdz_wersje
from src.comparator import czy_potrzebny_upgrade

with open('config/devices.yaml', 'r') as f:
    config = yaml.safe_load(f)

wersja_najnowsza = pobierz_wersje()
print(f"Najnowsza wersja stable: {wersja_najnowsza}")

for device in config['devices']:
    name = device['name']
    host = device['host']
    user = device['user']
    password = device['password']

    wersja_na_routerze = sprawdz_wersje(host, user, password)
    potrzebny = czy_potrzebny_upgrade(wersja_na_routerze, wersja_najnowsza)

    print(f"{name} ({host}): {wersja_na_routerze} -> upgrade potrzebny: {potrzebny}")