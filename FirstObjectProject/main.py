import random
import sys

import sys


class Tier:

    def __init__(self, tiername, augen, ohren, beine, gesunde_bein, schwanz):
        self.tiername = tiername
        self.augen = augen
        self.ohren = ohren
        self.beine = beine
        self.gesunde_bein = gesunde_bein
        self.schwanz = schwanz

    def change_name(self, tiername):
        self.tiername = tiername

    def change_augen (self, augen):
        self.augen = augen

    def change_ohren(self, ohren):
        self.ohren = ohren

    def change_beine(self, beine):
        self.beine = beine

    def change_gesunde_beine(self, gesunde_bein):
        self.gesunde_bein = gesunde_bein

    def change_schwanz(self, schwanz):
        self.schwanz = schwanz


if __name__ == '__main__':

    liste_aller_tiere = []

    i: int
    for i in range(0, random.randint(500, 1000)):
        # Instanz des Tiers
        tierobject = Tier("", 0, 0, 0, [], 0)
        #Value setting
        tierobject.tiername = "tierobject " + str(i)
        tierobject.augen = random.randrange(0, 8, 2)
        tierobject.ohren = random.randrange(0, 4, 2)
        tierobject.beine = random.randrange(2, 16, 2)
        #erstelle Liste in dem Object
        j: int
        for j in range(tierobject.beine):
            tierobject.gesunde_bein.append(random.randint(0, 1))
        tierobject.schwanz = random.randrange(0, 2, 1)
        #erweitere ObjectListe um das aktuelle Object
        liste_aller_tiere.append(tierobject)
        tierobject = None

    i: int
    for i in range(len(liste_aller_tiere)):
        krankebeine = 0
        gesundebeine = 0

        j: int
        for j in range(liste_aller_tiere[i].beine):
            if liste_aller_tiere[i].gesunde_bein[j] == 0:
                gesundebeine = gesundebeine + 1
            else:
                krankebeine = krankebeine + 1

        print (liste_aller_tiere[i].tiername + " mit " + str(liste_aller_tiere[i].augen) + " Augen und " + str(liste_aller_tiere[i].ohren) + " Ohren und " + str(liste_aller_tiere[i].beine) + " Beine, davon " + str(gesundebeine) + " gesund und " + str(krankebeine) + " krank, aber " + str(liste_aller_tiere[i].schwanz) + " Schwänz(e)")

app = QApplication(sys.argv)

w = QWidget()
w.setGeometry(50, 70, 500, 500)
w.setWindowTitle("Ausgabe der Liste YOOAH!")

w.show()

sys.exit(app.exec())
