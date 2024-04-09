
class Libro:
    def __init__(self, titolo, autore, isbn): 
        self.titolo=titolo
        self.autore=autore
        self.isbn=isbn
    
    def descrizione(self): 
        print(f"titotlo: {self.titolo}, autore; {self.autore}, codice identificativo: {self.isbn}")

class Libreria(Libro):
    def __init__(self, titolo, autore, isbn, catalogo):
        super().__init__(titolo, autore, isbn)
        self.catalogo=catalogo

    def aggiungi_libro(self): 
        if self.titolo in catalogo: 
            print("libro già presente in catalogo")
        else: 
            catalogo[self.titolo]={'autore': self.autore, 'isbn': self.isbn}
            print(f"il libro aggiunto è {self.titolo} dell'autore {self.autore} con codice identificativo {self.isbn}")
        print(catalogo)
    
    def rimuovi_libro(self):
        if self.titolo in catalogo:
            del catalogo[self.titolo] 
            print(f"il libro rimosso ha titolo {self.titolo} dell'autore {self.autore} con codice identificativo {self.isbn}")
        else: 
            print("attezione libro non in catalogo")

    

    



#prova: 

tit=input("inserisci un titolo: ")
aut=input("insersci un autore: ")
cod=int(input("insersci un isbn:"))
catalogo={}

libro1=Libro(tit, aut, cod)
libro1.descrizione()

libro1_piu=Libreria(tit, aut, cod, catalogo)
libro1_piu.aggiungi_libro()
