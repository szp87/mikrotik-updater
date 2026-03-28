import yaml
import schedule
import time
from src.scraper import pobierz_wersje
from src.connector import sprawdz_wersje
from src.comparator import czy_potrzebny_upgrade
from src.downloader import pobierz_image
from src.upgrader import wykonaj_upgrade
from src.logger import loguj

def run():
    with open('config/devices.yaml', 'r') as f:
        config = yaml.safe_load(f)

    wersja_najnowsza = pobierz_wersje()
    loguj('system', f"Najnowsza wersja stable: {wersja_najnowsza}")

    for device in config['devices']:
        name = device['name']
        host = device['host']
        user = device['user']
        password = device['password']
        import yaml
        import schedule
        import time
        from src.scraper import pobierz_wersje
        from src.connector import sprawdz_wersje
        from src.comparator import czy_potrzebny_upgrade
        from src.downloader import pobierz_image
        from src.upgrader import wykonaj_upgrade
        from src.logger import loguj

        def run():
            with open('config/devices.yaml', 'r') as f:
                config = yaml.safe_load(f)

            wersja_najnowsza = pobierz_wersje()
            loguj('system', f"Najnowsza wersja stable: {wersja_najnowsza}")

            for device in config['devices']:
                name = device['name']
                host = device['host']
                user = device['user']
                password = device['password']
                architektura = device['architecture']

                wersja_na_routerze = sprawdz_wersje(host, user, password)
                loguj(name, f"Wersja na routerze: {wersja_na_routerze}")

                if czy_potrzebny_upgrade(wersja_na_routerze, wersja_najnowsza):
                    loguj(name, f"Upgrade potrzebny: {wersja_na_routerze} -> {wersja_najnowsza}")
                    pliki = pobierz_image(wersja_najnowsza, architektura)
                    wynik = wykonaj_upgrade(host, user, password, pliki)
                    if wynik:
                        loguj(name, "Upgrade zakończony sukcesem")
                    else:
                        loguj(name, "Upgrade nie powiódł się")
                else:
                    loguj(name, f"Brak upgrade - wersja aktualna: {wersja_na_routerze}")

        schedule.every().monday.at("03:00").do(run)
        loguj('system', "Scheduler uruchomiony - sprawdzanie co poniedzialek o 03:00")

        run()  # uruchom od razu przy starcie

        while True:
            schedule.run_pending()
            time.sleep(60)