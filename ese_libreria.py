#inizializzo lista_libri=[]

#faccio la classe Libro(self, titolo, autore, libro)
    
        #metodo: descrizione(self)
        #stringa self.titolo, self.autore, self.libro
        #append a lista_libri ????

#classe figlia Libreria(Libro): 
    #__init__(titolo, autore, isbn, catalogo)
    #catalogo= lista_libri
    #self.catalogo=catalogo

    #def aggiungi_libro():
        #append a lista_libri


#while True:
    #vuoi aggiungere libri al catalogo?
    #if no: break

#inizio: 


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
        catalogo.append(self.titolo)
        catalogo.append(self.autore)
        catalogo.append(self.isbn)
        print(catalogo)


#prova: 

tit=input("inserisci un titolo: ")
aut=input("insersci un autore: ")
cod=int(input("insersci un isbn:"))
catalogo=[]

libro1=Libro(tit, aut, cod)
libro1.descrizione()

libro1_piu=Libreria(tit, aut, cod, catalogo)
libro1_piu.aggiungi_libro()