class BankovniUcet:
    
    def __init__(self, vlastnik : str):
        self._vlastnik = vlastnik
        self._zustatek = 0
    
    def zjisti_zustatek(self):
        print("Zjištění zůstatku.")
        return self._zustatek
    
    def vloz(self, hodnota):
        self._zustatek += hodnota
        print(f"Vloženo {hodnota}, na účtě máte {self._zustatek}.")
    
    def vyber(self, hodnota):
        if self._zustatek < hodnota:
            print("Výběr peněz nemožný, nedostatek peněz na účtu.")
            return
        self._zustatek -= hodnota
        print(f"Vybírám {hodnota}, na účtě máte {self._zustatek}.")
        
muj_ucet = BankovniUcet("Barack")
muj_ucet.vloz(800)
muj_ucet.zjisti_zustatek()
muj_ucet.vyber(700)
muj_ucet.vyber(700)
print(muj_ucet._vlastnik)