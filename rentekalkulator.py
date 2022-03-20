# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

class Rentekalkulator:

    def __init__(self, belop, fra_dato, til_dato, rentesats):
        self._belop = belop
        self._fra = fra_dato
        self._til = til_dato
        self._rentesats = rentesats
        self._rentedag = rentesats/365
        self._forsinkelsesrenteDict = self._genererForsinkelsesrenteDict()
        self._forsinkelsesrentePerDagDict = self._genererForsinkelsesrentePerDagDict(self._forsinkelsesrenteDict)

    def normalRentesats(self):
        diff = self._til - self._fra
        dagerRente = diff.days
        return round(self._belop * (dagerRente * self._rentedag), 2)

    def forsinkelsesrente(self):
        renteUt = 0.0
        dato = self._fra + timedelta(days = 1)
        while dato <= self._til:
            renteUt += self._belop * self._forsinkelsesrentePerDagDict[dato]
            dato += timedelta(days = 1)
        return round(renteUt, 2)



    def _genererForsinkelsesrentePerDagDict(self, innDict):
        dato = datetime(1978,1,1)
        utDict = {}
        rente = 0.0
        while dato < datetime(2060,1,1):
            if dato in innDict.keys():
                rente = innDict[dato]
            utDict[dato] = (rente/100)/365
            dato += timedelta(days = 1)
            #print(dato)

        with open("renteoversiktDatoer.txt", "w") as minFil:
            for key in utDict.keys():
                minFil.write(str(key) + " " + str(utDict[key]) + "\n")

        #print(utDict)

        return utDict



    def _genererForsinkelsesrenteDict(self):
        dict = {}
        with open("forsinkelsesrenteoversikt.txt") as minFil:
            for line in minFil:
                dagOgRente = line.split()
                #print(dagOgRente)
                rente = dagOgRente[1]
                rentestrip0 = rente.replace("%","")
                renteRen = rentestrip0.replace(",",".")
                dagSplit = dagOgRente[0].split("/")
                #print(dagSplit)
                aar = dagSplit[2]
                maaned = dagSplit[1]
                dag = dagSplit[0]
                dict[datetime(int(aar),int(maaned),int(dag))] = float(renteRen)
            listeAvDatoer = []
            for key in dict.keys():
                listeAvDatoer.append(key)
                #print(listeAvDatoer)
            listeAvDatoer.sort()
            #print(listeAvDatoer)
            new_dict = {}
            for dato in listeAvDatoer:
                new_dict[dato] = dict[dato]
        return new_dict
