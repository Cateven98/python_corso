#funzione per randomizzare:
import random
def randomizzatore():
    return random.randint(1,100)

#numero segreto: 
numero_segreto=randomizzatore() 
print("il numero da indovinare è", numero_segreto)

tentativi=1 #inzializzo i tentativi
while tentativi==True:
    gioco=input("vuoi giocare? ")
    while gioco=="si":
        numero=int(input("dammi un numero: "))
        if numero_segreto>numero:
            print("il numero è troppo piccolo")
        elif numero_segreto<numero:
            print("il numero è troppo grande")
        else:
            print("hai indovinato!")
            gioco=input("vuoi giocare ancora? ")
            #break
    if gioco=="no":
        tentativi==False
        print("esci dal gioco")
        break

