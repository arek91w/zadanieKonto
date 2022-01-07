import konto as k


x = k.Konto('111', 'Adam')

x.stan()
x.wplata(11.57)
x.stan()
x.wyplata(12)
x.stan()
x.drukHistorii()

y = k.KontoLimitowane('222', 'Ewa')

y.stan()
y.wyplata(100.)
y.wplata(100)
y.wyplata(50)
y.drukHistorii()