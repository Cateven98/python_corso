

inventario={"gonna":{"prezzo": 2, "quantità": 100}}
print(inventario)
spesa_cliente={}
spesa=[]                                                  #spesa: lista con solo le spese_tot di ogni acquisto per articolo (vedi aqcuisto_articoli())



#PARTE CLIENTE:  

#visulizza articoli
def visualizza_articoli():
    visualizza=input("Vuoi visualizzare gli artcoli in negozio? ")
    if visualizza=="si": 
        print(inventario)
    else: 
        print("ok ciao")

#acquisto articoli: 

def aqcuisto_articoli(): 
    articolo_acquistato=input("quale articolo vuoi acquistare? ")
    q_acquistate=int(input("quanti articoli acquistare? "))
    if articolo_acquistato in inventario: 
        inventario[articolo_acquistato]["quantità"] -= q_acquistate                #tolgo dall'inventario le quantità acquistate 
        tot_spesa=inventario[articolo_acquistato]["prezzo"]*q_acquistate           #mi calcolo la spesa totale per articolo
        #spesa_cliente.append(articolo_acquistato, q_acquistate, tot_spesa)
        spesa_cliente[articolo_acquistato] = {'prezzo': tot_spesa, 'quantità': q_acquistate}            #raccolgo tutte le spese dentro ad un nuovo dizonario spesa_cliente 
        spesa.append(tot_spesa)
        print("l'utente ha acquistato", q_acquistate, "articolo", articolo_acquistato, "per", tot_spesa, "euro")
    else: 
        print("articolo non in inventario")

'''print(inventario)
print(spesa_cliente)
aqcuisto_articoli()
print(inventario)
print(spesa_cliente)'''


#PARTE AMMINISTRATORI: 


#aggiungo articoli all'inventario: 

def aggiungo_articoli():                                            #posso non mettere alcun parametro perchè li definisco dentro la funzione
    articolo=input("che articolo vuoi aggiungere in inventario? ")
    p=int(input("segnala il prezzo dell'articolo: "))
    q=int(input("aggiungi le quantità di articolo disponibile: "))
    if articolo in inventario:                                       #se l'articolo è già presente in inventario
        inventario[articolo]["quantità"] += q                        #sommo q alle quantità già esistenti
    else: 
        inventario[articolo] = {'prezzo': p, 'quantità': q}
    print("l'articolo aggiunto in inventario è", articolo, "che costa", p, "e ne abbiamo disponibili", q)


#tolgo articoli dall'inventario: 

def togli_articoli(): 
    articolo=input("quale articolo vuoi eliminare? ")
    if articolo in inventario:                          #se l'articolo è già presente in inventario
        del inventario[articolo]                        #elimino dal dizionario l'articolo
        print("hai rimosso l'articolo", articolo, "dall'inventario")
    else: 
        print("riguarda bene forse hai sbagliato a digitare")

#visualizzo rapporto vendite + guadagno totale:

def rapporto_vendite(): 
   print(spesa_cliente) #stampo il dizionario con la spesa del cliente
   print(sum(spesa))    #stampo la somma delle spese per articolo che ho inserito nella lista spesa 


#visualizzo stato inventario: 

def stato_inventario():
    print(inventario)







