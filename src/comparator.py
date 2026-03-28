def czy_potrzebny_upgrade(wersja_na_routerze, wersja_najnowsza):
    return tuple(int(x) for x in wersja_na_routerze.split('.')) < tuple(int(x) for x in wersja_najnowsza.split('.'))

