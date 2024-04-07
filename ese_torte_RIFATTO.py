'''Crea un sistema che faccia aggiungere all'utente nome e gli assegni un numero di tavolo.
l'utente dovrà poi scegliere 3 ingredienti da 3 liste specifiche (base, facritura, topping)
in base alle sue scelte dovrà creare una torta finale e il suo prezzo.
il sistema dovrà essere ripetibile e stampare alla fine dell'ordine la torta i suoi elementi e il prezzo, 
alla fine dovrà scrivere quante torte e quanto guadagno totale'''

#liste di composizione torta e prezzi: 
base=["pan di spagna", "gelato", "riso soffiato"]
farcitura=["cioccolato", "cocco", "fragola"]
topping=["praline", "panna", "canditi"]

prezzi_base=[2,5,7]
prezzi_farcitura=[5,9,1]
prezzi_topping=[4,7,9]


tavolo=1 #inizializzo ciclo
while True: #max di tavoli sono 2 
    nome=input("insersci il tuo nome: ")
    if tavolo==3: 
        print("il ristorante è al completo, torna più tardi")
        break 
    print("il tavolo del cliente", nome, "è il numero", tavolo)
    spesa_cliente=[] #azzero la spesa cliente
    numero_torte=[]


   #ciclo per la scelta dei gusti delle torte
    while True: 
            acquisto=input("vuoi acquistare? si/no ") 
            if acquisto=="no": 
                break
            scelta_base=input("quale base: ")
            if scelta_base=="pan di spagna": 
                prezzo_base=prezzi_base[0]
            elif scelta_base=="gelato":
                prezzo_base=prezzi_base[1]
            elif scelta_base=="riso soffiato": 
                prezzo_base==prezzi_base[2]
        
            scelta_farcitura=input("quale farcitura? ")
            if scelta_farcitura=="cioccolato": 
                prezzo_farcitura=prezzi_farcitura[0]
            elif scelta_farcitura=="cocco":
                prezzo_farcitura=prezzi_farcitura[1]
            elif scelta_farcitura=="fragola":
                prezzo_farcitura=prezzi_farcitura[2]
        
            scelta_topping=input("quale topping? ")
            if scelta_topping=="praline": 
                prezzo_topping=prezzi_topping[0]
            elif scelta_topping=="panna": 
                prezzo_topping=prezzi_topping[1]
            elif scelta_topping=="canditi": 
                prezzo_topping=prezzi_topping[2]
        
            q=int(input("quante torte cosi vuoi? "))
            prezzo_torta=(prezzo_topping+prezzo_base+prezzo_farcitura)*q
            spesa_cliente.append(prezzo_torta)
            numero_torte.append(q)
            #posso sommare dalla lista spesa cliente più ordini di torte diverse e poi do il prezzo finale 

            print("il cliente", nome,"al tavolo", tavolo, "ha preso", sum(numero_torte) , "torte, al prezzo totale di", sum(spesa_cliente), "euro") 
    tavolo+=1