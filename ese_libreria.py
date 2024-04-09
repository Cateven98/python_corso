

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
            print(f"il libro cercato ha titolo: {self.titolo}, con isbn {catalogo[self.titolo]["isbn"]}") #libro che voglio cercare 
            
            for i in catalogo.keys():    #ciclo for per cercare tra le chiavi il titolo del libro                                              
                if i==self.titolo: 
                    print(f"il libro {i}, con isbn {catalogo[self.titolo]["isbn"]} è stato trovato")
                    break  #se trova il libro break il ciclo for
                else: 
                    print("libro non in catalogo")
                    break #se non trova il libro break il ciclo for

    def mostra_catalogo(self): 
        for j in catalogo.keys():                                                                               #ciclo for mi stampa le chiavi cioè i titoli di ogni j libro e rispettivi autore e isbn 
            print(f"Titolo:{j}, Autore:{catalogo[j]["autore"]}, codice identificativo: {catalogo[j]["isbn"]}")


#PROVE DEI VARI METODI: 

#definisco il libro:
tit=input("inserisci un titolo: ")
aut=input("insersci un autore: ")
cod=int(input("insersci un isbn:"))

        
#definisci dizionario catalogo:
catalogo={"volare":{"autore": "cate", "isbn": 223 }, 
          "tartaruga": {"autore": "gio",  "isbn": 224}}
#print(catalogo["volare"]["isbn"])


libro1=Libro(tit, aut, cod)  
libro1_piu=Libreria(tit, aut, cod, catalogo) 

libro1_piu.aggiungi_libro()

libro1_piu.cerca_libro()
libro1_piu.mostra_catalogo()
libro1_piu.rimuovi_libro()

       
