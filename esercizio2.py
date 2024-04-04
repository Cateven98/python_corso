#######ESERCIZIO 2: 

numero=int(input("inserisci un numero: ")) #inserisco il numero da cui iniziare il range 
for i in range(numero,-1,-1):
            print(i)

#voglio continuare ad inserire numeri o no?
while True: #rendo infinito il loop 
    domanda=int(input("vuoi continuare si=1/no=0? "))
    if domanda == 1:
        numero=int(input("inserisci un numero: "))
        for i in range(numero,-1,-1):
            print(i)
    else:  
        print("finito!!")            
        break  #se non voglio continuare il break conclude il mio ciclo infinito 
