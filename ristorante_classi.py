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
    
    menu={
    }

    def __init__(self):
        nome=input("insersci nome ristorante: ")
        tipo_cucina=input("inserisci tipo cucina: ")
        self.nome=nome
        self.tipo_cucina=tipo_cucina
    

    def descrivi_ristorante(self):
        return print("ilristorante", self.nome, "che ha una cucina", self.tipo_cucina)
    
    def stato_apertura():
        if Ristorante.aperto=="False": 
            return print("il ristorante è chiuso torna più tardi")
        else: 
            return print("il ristorante è aperto!")
    
    def apri_ristorante(apri): 
        #apri=input("Vuoi sapere se il ristorante è aperto? si/no ")
        Ristorante.aperto==True
        return print("il ristorante sta aprendo")
    
    def chiudi_ristorante(apri): 
       #apri=input("Vuoi sapere se il ristorante è aperto? si/no ")
        Ristorante.aperto==False
        return print("il ristorante sta chiudendo")
    

    def aggiungi_menu(piatto, prezzo_piatto): 
        aggiungi=("vuoi aggiungere un piatto e il suo prezzo? si/no")
        if aggiungi=="no":
            return print("ok, ciao")
        else:
            piatto=input("che piatto vuoi aggiungere? ")
            prezzo_piatto=input("che prezzo h ail piatto: ")
            Ristorante.menu[piatto]= {"prezzo": prezzo_piatto}
            print("il ristorante aggiunto è", piatto, "che costa", prezzo_piatto)


risto1=Ristorante()

risto1.descrivi_ristorante()

risto1.apri_ristorante()

risto1.togli_menu()



