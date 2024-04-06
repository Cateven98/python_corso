#ESERCIZIO 1:


#definisco le funzioni: 
def area_triangolo(b,h):
    return (b*h)/2
    
    
def area_quadrato(l):
    return l**2

def area_rettangolo(b1,h1):
    return b1*h1
 

aree=[] #inizializzo lista aree

while True:
        tipo_area=input("quale area vuoi calcolare? se vuoi far finire il gioco scrivi fine ")
        if tipo_area=="fine":
            print("ciao")
            print(aree) #se esco dal programma mi printa tutte le aree calcolate
            break
        elif tipo_area=="triangolo":
            b=int(input("scrvi misura base del trangolo: "))
            h=int(input("scrivi misura altezza triangolo: "))
            triangolo=area_triangolo(b,h)
            print(triangolo)
            aree.append(triangolo)
            print(aree)
        elif tipo_area=="quadrato":
            l=int(input("scrivimi la misura del lato del quadrato"))
            quadrato=area_quadrato(l)
            print(quadrato)
            aree.append(quadrato)
            print(aree)
        elif tipo_area=="rettangolo":
            h1=int(input("scrivi altezza rettangolo: "))
            b1=int(input("scrivi base rettangolo: "))
            rettangolo=area_rettangolo(b1,h1)  
            print(rettangolo)
            aree.append(rettangolo)
            print(aree)

            


