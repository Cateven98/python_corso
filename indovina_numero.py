#ESERCIZIO BASE:

#non volgio che mi dia voi giocare ancora? subito, lo voglio solo dopo che ha indovinato il numero

#funzione per randomizzare:
import random
def randomizzatore():
    return random.randint(1,100)

#numero segreto: 
numero_segreto=randomizzatore() 
print("il nunero da indovinare è",numero_segreto)

tentativi=1 #inzializzo i tentativi
while tentativi==True:
    gioco=input("vuoi giocare ancora? ")
    while gioco=="si":
        numero=int(input("dammi un numero: "))
        if numero_segreto>numero:
            print("il numero è troppo piccolo")
            pass
        elif numero_segreto<numero:
            print("il numero è troppo grande")
            pass
        else: 
            print("hai indovinato!")
            break
    if gioco=="no":
        tentativi==False
        print("esci dal gioco")
        break

