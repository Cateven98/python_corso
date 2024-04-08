'''class Punto: 
    y=0
    x=0

nome=input()

z=Punto() #creo un oggetto, in questo caso nella mia classe non ho messo __init__
#non importa averlo messo la classe me lo crea automaticamente, ma non posso avere parametri per i miei oggetti
#se io voglio parametri per il mio oeggettto devo mettere __init__'''

#ESERCIZIO COORDINATE: 

class Punto():
    x=0
    y=0
    def muovi(self):
        x=int(input("insersci la coordinata dx: "))
        y=int(input("insersci la coordinata dy: "))
        self.x=x
        self.y=y
        return print("le coordinate scelte sono", (self.x, self.y))

    def distanza_origine(self): 
        cx=0
        cy=0
        dist=(((self.x-cx)**2)+((self.x-cy)**2))**(1/2)
        return print("la distanza tra", (self.x,self.y), "e il centro è: ", dist)


while True: 
    inizio=input("scrivi inizia se vuoi mettere le coordinate, se vuoi finire metti 0:" )
    if inizio=="0":
        break
    z=Punto()
    z.muovi()
    z.distanza_origine()
