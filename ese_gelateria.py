

#RIVEDI E FALLO DIVERSO!!

scelte=[] #inizializzo scelte

class Gusti():
    def __init__(self, gusto1, gusto2, gusto3):
        self.gusto1=gusto1
        self.gusto2=gusto2
        self.gusto3=gusto3

    def aggiungi_gusti(self):
        scelte.append(self.gusto1) #aggiungo i gusti alla lista scelte
        scelte.append(self.gusto2)
        scelte.append(self.gusto3)
        print(scelte)



class Gelato(Gusti):
    def __init__(self,gusto1, gusto2, gusto3, cono): 
        super().__init__(gusto1, gusto2, gusto3)
        self.cono=cono
    
    def scelgi_cono(self):                                                                           #scelta di cono o coppetta
        print(f"vuoi un {self.cono} con i seguenti gusti:{self.gusto1, self.gusto2, self.gusto3}")   #riepilogo



while True:                                #1° ciclo se voglio gelato o no
    entr=input("vuoi un gelato' si/no ")
    if entr=="no":
        print("ok, ciao")
        break
    while True:                            #2° ciclo: scelgo i gusti
        g1=input("dimmmi il primo gusto di gelato: ")
        g2=input("dimmmi il secondo gusto di gelato: ")
        g3=input("dimmmi il terzo gusto di gelato: ")
        z=Gusti(g1,g2,g3)

        tipo_c=input("vuoi cono o coppetta? ")
        c=Gelato( g1, g2, g3, tipo_c)
        c.aggiungi_gusti()
        c.scelgi_cono()
        if len(scelte)==3: #il ciclo si ferma e ritorna al 1° ciclo quando len della lista scelte è completa
            break
