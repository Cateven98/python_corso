'''Chiedi all'utente di inserire un numero N. Il
programma dovrebbe stampare la sequenza di Fibonacci fino a N.
Ad esempio, se l'utente inserisce 100, il programma dovrebbe
stampare tutti i numeri della sequenza di Fibonacci minori o uguali a 100
'''

#funzione di fibonacci: 
def fibonacci(n):
    for i in range(0,19,1): 
        num_fibo=ordine[i]+ordine[i+1]
        ordine.append(num_fibo)
        if num_fibo>=n: 
            ordine.remove(num_fibo) #se arriva ad un  numero di fibonacci più grande di num, lo inserisce nella lista quindi cos' lo togliamo
            break 

#ciclo per avere sequenza di numeri di fibonacci 
while True:
    ordine=[0,1]    #la metto qui cosi ad ogni nuovo ciclo torna ad "azzerarsi"
    gioco=input("vuoi giocare? si/no ")
    if gioco=="no":
        print("ok, ciao")
        break 
    num=int(input("inserisci un numero: ")) #inserisco il numero
    fibonacci(num)
    print("il numero scelto è", num, "la sua sequenza di fibonacci è", ordine)