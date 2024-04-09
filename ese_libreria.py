#classe padre: 

class Libro:
    def __init__(self, titolo, autore, isbn): 
        self.titolo=titolo
        self.autore=autore
        self.isbn=isbn
    
    def descrizione(self):                                                                           #descrizione libro 
        print(f"titotlo: {self.titolo}, autore; {self.autore}, codice identificativo: {self.isbn}")


#classe figlia: 

class Libreria(Libro):
    def __init__(self, titolo, autore, isbn, catalogo):     
        super().__init__(titolo, autore, isbn)
        self.catalogo=catalogo

    def aggiungi_libro(self):                                 #aggiungo libro alla libreria catalogo
        if self.titolo in catalogo: 
            print("libro già presente in catalogo")
        else: 
            catalogo[self.titolo]={'autore': self.autore, 'isbn': self.isbn}
            print(f"il libro aggiunto è {self.titolo} dell'autore {self.autore} con codice identificativo {self.isbn}")
        print(catalogo)
    
    def rimuovi_libro(self):                                #elimino libro alla libreria catalogo, per titolo
        if self.titolo in catalogo:
            del catalogo[self.titolo] 
            print(f"il libro rimosso ha titolo {self.titolo} dell'autore {self.autore} con codice identificativo {self.isbn}")
        else: 
            print("attezione libro non in catalogo")


    def cerca_libro(self): 
        if self.titolo in catalogo: 
            print(f"il libro cercato ha titolo: {self.titolo}")
            for i in catalogo: 
                if i==self.titolo: 
                    print(f"il libro trovato è {catalogo[self.titolo]}")
                else: 
                    print("libro non in catalogo")


    def mostra_catalogo(self): 
        print(catalogo)



#definisco il libro:
tit=input("inserisci un titolo: ")
aut=input("insersci un autore: ")
cod=int(input("insersci un isbn:"))

        
#definisci dizionario catalogo:
catalogo={"volare":{"autore": "cate", "isbn": 223 }, 
          "tartaruga": {"autore": "gio",  "isbn": 224}}
#print(catalogo)

'''
for i in catalogo: 
    if i=="volare": 
        print("bravo")'''

libro1=Libro(tit, aut, cod)  
libro1_piu=Libreria(tit, aut, cod, catalogo) 

libro1_piu.aggiungi_libro()

libro1_piu.cerca_libro()



#automatizzo DA RIVEDERE: 
'''

while True: 
    accedi=input("vuoi accedere alla libreria? si/no" )
    if accedi=="no": 
        break

    while True: 
        visualizza_cerca=input("visualizza o cerca libro? ")
        if visualizza_cerca=="0": 
            pass
        while True: 
            prestito=input("vuoi ritirare=0, riportare libri=1 o cercare=2 o visualizzare intero catalogo=3? ")
        
            #definisco il libro:
            tit=input("inserisci un titolo: ")
            aut=input("insersci un autore: ")
            cod=int(input("insersci un isbn:"))

        
            #definisci dizionario catalogo:
            catalogo={}
        
            libro1=Libro(tit, aut, cod)  
            libro1_piu=Libreria(tit, aut, cod, catalogo) 


            if prestito=="1": 
                libro1.descrizione()
                libro1_piu.aggiungi_libro()
        
            elif prestito=="0":
                libro1.descrizione()
                libro1_piu.rimuovi_libro()
        
            elif prestito=="2":
                pass
        
            elif prestito=="3": 
                pass
'''

            
       
