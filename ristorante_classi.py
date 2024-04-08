'''
classe Ristorante: 
aperto=False
menu={
    'piatti': {'prezzo': }
}

    def __init__(self, nome, tipo_cucina):
    nome=input("insersci nome ristorante)
    tipo=input("inserisci tipo cucina)
    
    #aggiungo gli attributi a self


#aggiungo i metodi: 
#1) descrivi_ristorante(self)
    faccio un print, con self.nome e self.tipo

#2) stato apertura()
    aperto=input("vuoi sapere se il ristorante è aperto?)
    if Ristorante.aperto==False: 
    print("il risto è chiuso, torna più tardi)

#3) apri_ristorante()
    Ristorante.aperto=True
    if Ristorante.aperto==True: 
    print("il ristorante sta aprendo, puoi entrare)


#4) chiudi_ristorante()


#5) aggiungi_al_menu(piatti, prezzi):
    if 



#6) togli_dal_menu()

#7)stampa_menu()
    print(Ristorante.menu)
'''
class Ristorante: 
    aperto=False
    menu={}

    def __init__(self):
        nome=input("insersci nome ristorante: ")
        tipo_cucina=input("inserisci tipo cucina: ")
        self.nome=nome
        self.tipo_cucina=tipo_cucina

    def descrivi_ristorante(self):
        return print("il nome del ristorante è", self.nome, "che fa cucina", self.tipo_cucina)
    
    def stato_apertura(self):
        if Ristorante.aperto=="False": 
            return print("il ristorante è chiuso torna più tardi")
        else: 
            return print("il ristorante è aperto!")
    
    def apri_ristorante(self): 
        #apri=input("Vuoi sapere se il ristorante è aperto? si/no ")
        Ristorante.aperto==True
        return print("il ristorante sta aprendo")
    
    def chiudi_ristorante(self): 
       #apri=input("Vuoi sapere se il ristorante è aperto? si/no ")
        Ristorante.aperto==False
        print("il ristorante sta chiudendo")
    

    def aggiungi_menu(self): 
        aggiungi=("vuoi aggiungere un piatto e il suo prezzo? si/no")
        piatto1=input("che piatto vuoi aggiungere? ")
        prezzo_piatto1=int(input("che prezzo h ail piatto: "))
        if aggiungi=="no":
            print("ok, ciao")
        else:
            Ristorante.menu[piatto1]= prezzo_piatto1
            print("il ristorante aggiunto è", piatto1 , "che costa", prezzo_piatto1)



    def togli_menu(self): 
        piatto_tolto=input("inserisci il nome del piatto da togliere: ")
        if piatto_tolto not in Ristorante.menu: 
            print("il piatto selezionato non è presente nel menu")
        else: 
            del Ristorante.menu[piatto_tolto]
            print("il piatto tolto dal menu è:", piatto_tolto)


#prove dei metodi: 

'''
risto1=Ristorante()

risto1.descrivi_ristorante()

risto1.apri_ristorante()

risto1.chiudi_ristorante()

risto1.aggiungi_menu()

risto1.togli_menu()'''



while True:
    utente=input("Ciao ristoratore, benvenuto nel sito, inserisci il tuo nome utente o se vuoi uscire scrivi esci: ")
    if utente.lower=="esci" or "0":
        break

    risto1=Ristorante()
    risto1.descrivi_ristorante()

    while True: 
        vedi=input("vuoi sapere se il ristorante è chiuso?")








