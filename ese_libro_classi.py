#ESERCIZIO LIBRO: 

#ESERCIZIO LIBRO: 

#creo classe libro: 
class Libro():

    def descrizione(self):                             #creo funzione descrizione
        titolo=input("dammi il titolo del libro: ")
        autore=input("insersci il nome dell'autore: ")
        pagine=int(input("insersci il numero di pagine: ")) 

        self.titolo=titolo   #assegno attributo ai miei oggetti 'self'
        self.autore=autore   #assegno attributo ai miei oggetti 'self'
        self.pagine=pagine   #assegno attributo ai miei oggetti 'self'
        
        return print("Il libro", self.titolo, "dell'autore", self.autore, "ha", self.pagine)

#Inizio il mio archivio libri: 
while True: 
    archivio=input("vuoi inserire un altro libro scrvi si, vuoi uscire dall'archivio scrivi esci: ")
    if archivio=="esci": 
        break
    z=Libro()
    z.descrizione()