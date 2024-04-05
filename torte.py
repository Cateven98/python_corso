#ESERCIZIO 1: 
#if tavolo == 3: #così blocco il codice infinito
#        tavolo = False
#       break

#numero=int(input("dammi un numero: "))
tavolo=1
ciao=True
while ciao==True: 
    nome=input("nome:")
    print("il cliente", nome, "ha il tavolo" , tavolo)
    tavolo +=1
    
#lista con base e ingredienti: 
    scelte=["base", "farcitura", "topping"]
    base=["crostata", "pan di spagna", "gelato"]
    farcitura=["cioccolata", "fragola", "crema"]
    topping=["praline","m&m", "panna"]


    #composizione menu
    for r in base: 
            scelta_base=input("che base voglio? ")
            print("la base scelta è ",scelta_base)
            if r=="gelato" or r=="pan di spagna" or r=="crostata" :
                  break
    for x in farcitura: 
                scelta_farcitura=input("che farcitura voglio? ")
                print("la base scelta è ",scelta_farcitura)
                if x=="crema" or x=="fragola" or x=="cioccolata":
                      break
    for z in topping: 
                    scelta_topping=input("che topping voglio? ")
                    print("il topping è ",scelta_topping)
                    print("il cliente", nome, "al tavolo", tavolo, "ha preso", scelta_base, "con", scelta_farcitura, "e", scelta_topping)
                    if z=="praline" or z=="panna" or z=="m&m":
                          break


#assegno prezzi a ingredienti: 
#prezzo base:
    if scelta_base==base[0]: 
        prezzo_base=2
    elif scelta_base==base[1]:
        prezzo_base=4
    else: 
        prezzo_base=6

#prezzo farcitura:
    if scelta_farcitura==farcitura[0]: 
        prezzo_farcitura=2
    elif scelta_farcitura==farcitura[1]:
        prezzo_farcitura=4
    else: 
        prezzo_farcitura=6

#prezzo topping:
    if scelta_topping==topping[0]: 
        prezzo_topping=2
    elif scelta_topping==topping[1]:
        prezzo_topping=4
    else: 
        prezzo_topping=6


#prezzo totale: 
    prezzo_totale=(prezzo_topping+prezzo_farcitura+prezzo_base)
    print("il clinete", nome, "dovrà pagare", prezzo_totale)
    







#menu=input("scelta  torta: ")
#if torta=='''