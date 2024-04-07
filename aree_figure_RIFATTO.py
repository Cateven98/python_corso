'''Scrivi una funzione chimata area_triangolo che preda in input la base e l'altezz del triangolo e restituisca la sua area.
fare la stessa cosa con quadrato e erttangolo e rendere ripetibile salvando in una lista 
tutti i risultati'''


#funzioni per calcolare le aree: 

def area_rettangolo(b,h): #rettangolo
    return b*h

def area_quadrato(l,y): #area quadrato
    return l*y

def area_triangolo(r,t):  #area triangolo
    return (r*t)/2

aree=[] #inizializzo la lista dei risultati
print(aree)

while True: 
    figura=input("insersci il nome di una figura, o scrivi esci se vuoi uscire dal programma: ") #scegli figura o esci 
    if figura=="esci": 
        print("ciao")
        break
    base=int(input("insersci la misura di una base: "))
    altezza=int(input("insersci la misura di un'altezza: "))
    if figura=="rettangolo": 
        area=area_rettangolo(base, altezza)
        print("l'area del rettangolo è:", area)
    elif figura=="quadrato":
        area=area_quadrato(base, altezza) 
        print("l'area del quadrato è:", area)
    elif figura=="triangolo": 
        area=area_triangolo(base, altezza)
        print("l'area del triangolo è:", area)
    else: 
        print("figura o inserimento sbagliati")
    
    aree.append(area)  #attenzione a dove metti questo passaggio, se lo metto dentato sta dentro al while, sennò no 
    print(aree)
