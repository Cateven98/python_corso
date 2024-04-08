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
   # menu={'piatti': {'prezzo': }}

    def __init__(self):
        nome=input("insersci nome ristorante: ")
        tipo_cucina=input("inserisci tipo cucina: ")
        self.nome=nome
        self.tipo_cucina=tipo_cucina
    

    def descrivi_ristorante(self):
        return print("ilristorante", self.nome, "che ha una cucina", self.tipo_cucina)
    
    


risto1=Ristorante()

risto1.descrivi_ristorante()


