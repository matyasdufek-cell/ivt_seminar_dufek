class Zamestnanec:

    def __init__(self, jmeno, prijmeni, datum_nastupu):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.datum = datum_nastupu

class Ucitel(Zamestnanec):
    def __init__(self, jmeno, prijmeni, datum_nastupu, predmet):
        super().__init__(jmeno, prijmeni, datum_nastupu)
        self.predmet = predmet

class Uklizecka(Zamestnanec):
    def __init__(self, jmeno, prijmeni, datum_nastupu, typ_mopu):
        super().__init__(jmeno, prijmeni, datum_nastupu)
        self.typ_mopu = typ_mopu