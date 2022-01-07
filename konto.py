import datetime as dt

class Konto:
    def __init__(self, nr, klient):
        self._nr = nr
        self._klient = klient
        self._stan = 0.
        self._historia = []
        print('Konto: '+self._nr+' Stan: '+str(self._stan))
    
    def wplata(self, kwota):
        self._stan += kwota
        czas = dt.datetime.now()
        self._historia.append('Czas transakcji: '+str(czas)+'  Typ: '+'WPLATA'+ '  Kwota: '+str(kwota)+ '  Stan konta: '+str(self._stan))

    def wyplata(self, kwota):
        self._stan -= kwota
        czas = dt.datetime.now()
        self._historia.append('Czas transakcji: '+str(czas)+'  Typ: '+'WYPLATA'+ '  Kwota: '+str(kwota)+ '  Stan konta: '+str(self._stan))

    def stan(self):
        print(self._stan)

    def historia(self):
        for transakcja in self._historia:
            print(transakcja)

    def drukHistorii(self):
        for transakcja in self._historia:
            print(transakcja)


# klasa KontoLimitowane dziedziczy atrybuty oraz metody klasy Konto, dodajac atrybut _limit i nadpisuje metode wyplata
class KontoLimitowane(Konto):
    def __init__(self, nr, klient):
        super().__init__(nr, klient)
        self._limit = 0
    def wyplata(self, kwota):
        if (self._stan - kwota) > self._limit:
            self._stan -= kwota
            czas = dt.datetime.now()
            self._historia.append('Czas transakcji: '+str(czas)+'  Typ: '+'WYPLATA'+ '  Kwota:'+str(kwota)+ '  Stan konta: '+str(self._stan))
        else:
            print("Brak srodkow na koncie "+ str(self._nr) + ' na wyplate ' + str(kwota))

x = Konto('111', 'Adam')

x.stan()
x.wplata(11.57)
x.stan()
x.wyplata(12)
x.stan()
x.drukHistorii()

y = KontoLimitowane('222', 'Ewa')

y.stan()
y.wyplata(100)
y.wplata(100)
y.wyplata(50)
y.drukHistorii()