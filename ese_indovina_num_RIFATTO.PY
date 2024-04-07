'''Scrivi un programma che genera un numero casuale tra 1 e 100 (inclusi).
L'utente deve indovinare quale numero è stato generato. Dopo ogni tentativo, il programma dovrebbe dire all'utente se il
numero da indovinare è più alto o più basso rispetto al numero inserito. Il gioco termina quando l'utente indovina il numero
o decide di uscire.'''

#funzione di randomizzazione: 
import random
def randomizzatore():
    return random.randint(1,100)

x=randomizzatore()                     #se metto qui la funzione il numero da indovinare cambia solo se finisco o esco dal gioco
print("il numero da indovinare è", x)

#scelta del numero
while True:
        gioco=input("vuoi giocare o ti arrendi? ") #no: esci dal programma
        if gioco=="no": 
            print("ciao")
            break 
        num=int(input("inserire un numero: "))
        if num>x: 
            print("numero troppo alto")
        elif num<x: 
            print("numero troppo basso")
        else:
            print("hai indovinato!!") #se indovino esco dal ciclo
            break
        
 




#altro modo possibile:
'''

from random import *

def numero_casuale(): #funzione numero casuale
    return randint(1, 100)


def check(numero, numero_casuale): #funzione che checka se il numero è giusto o no
    if numero == numero_casuale:
        print("Hai indovinato, complimenti!")
    elif numero > numero_casuale:
        print("Il numero è troppo alto")
    elif numero < numero_casuale:
        print("Il numero è troppo basso")
    else:
        print("Numero non valido")

numero_casuale = numero_casuale()

while True:
    resa = int(input("Vuoi giocare o vuoi arrenderti? Premi 1 per giocare, 2 per arrenderti\n"))
    print("il numero da indovinare è", numero_casuale)
    if resa == 2:
        break

    numero = int(input("Scegli un numero da 1 a 100 per il nostro gioco!\n"))
    

    check(numero, numero_casuale)

    if numero == numero_casuale:
        break
    '''