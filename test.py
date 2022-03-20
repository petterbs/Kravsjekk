# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from rentekalkulator import Rentekalkulator


def test():
    minFraDato = datetime(2022,1,1)
    minTilDato = datetime(2023,1,1)
    minRentesats = 0.085
    mittBelop = 10000

    minRentekalkulator = Rentekalkulator(mittBelop, minFraDato, minTilDato, minRentesats)
    minRente = minRentekalkulator.normalRentesats()
    minForsinkelsesrente = minRentekalkulator.forsinkelsesrente()
    print(minRente)
    print(minForsinkelsesrente)
    #print(minRentekalkulator._forsinkelsesrenteDict)

test()
