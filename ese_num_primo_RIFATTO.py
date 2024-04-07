'''Crea uno script cher chiede nome e numero poi una chima a
la funzione primo_o_no che determini se un numero dato è primo o no. 
la funzione dovrebbe restituire True se il numero è primo e False altrimenti. A quel punto, 
se è primo lo salva e continua il ciclo altrimenti ti dice quante volte sta nel divisore più piccolo
'''

#funzione per definire se è primo o meno: 
def is_prime(numero):
    div = 0

    if numero == 1:
        return 1
    for i in range(2, numero//2+1): #se il numero è primo div rimane zero
        if numero%i == 0:
            div = i
            break
    return div


#inizializzo le due liste di utenti e numeri primi 
utente=[]
primi=[]

while True: 
    num=int(input("insersci un numero, oppure scrivi 0 se vuoi uscire: "))
    if num==0: 
        print("ciao")
        break
    nome=input("insersci un nome: ")

    div=is_prime(num) #utilizzo la funzione per vedere se sono numeri primi 
    if div==0: 
        print(num,"è un numero primo")
        primi.append(num)                 #se primo inserisco nella lista il numero
        utente.append(nome)               #se primo inserisco nella lista il nome utente 
        
        #se primo, faccio un recap del nome utente e del numero primo scelto
        for i in range(len(utente)):
            print("l'utente", utente[i], "ha scelto il numero primo", primi[i])
    else: 
        print(num, "non è un numero primo, il suo divisore più piccolo è:", div)



