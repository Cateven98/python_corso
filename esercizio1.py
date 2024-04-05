#ESERCIZIO 1: 

#credenziali utente e risposte a domande sicurezza per l'utente già loggato: 
utente_log="admin"
psw_log="123"
domanda1="gatto"
domanda2="it"

#utente è registrato?
registrato=input("ho già un account si/no?")
if registrato== "si":  
    print("iniziamo il log-in")
    utente=input("inserisci un nome utente:\n")
    psw=input("inserisci una password:\n")
            

else: 
    utente=input("Iniziamo la registrazione, inserisci il nome utente:\n") #utente non registrato
    psw=input("inserisci la password:\n") 
    utente_log=utente  #sovrascrivo in modo da renderla sempre vera 
    psw_log=psw #sovrascrivo in modo da renderla sempre vera
    print(utente)
    print(utente_log)
    domanda1=input("domanda di sicurezza n1: il tuo animale preferito è?\n")
    domanda2=input("domanda di sicurezza n2: il tuo film preferito è?\n")
    print("sei registrato") 


#controllo se credenziali sono corrette: 
#(le risccrivo finchè non lo sono)
i=False
while i==False: 
    if  utente_log==utente and psw_log==psw: 
        print("Benvenuto nel tuo account!")
        i=True
    else: 
        print("credenziali non corrette, riprova ad inserire nome utente e password")
        utente=input("inserisci un nome utente:\n")
        psw=input("inserisci una password:\n")

#Se credenziali corrette procedo con eventuale cambio password e nome utente: 
scelta_cambio= input("Se vuoi cambiare il nome utente allora scrivi 'utente', se vuoi cambiare la psw allora scrivi 'psw', oppure "+
                         "scrivi 'no modifiche' se voglio solo entrare nell'account: ") #rispondo alle domande di acesso

#Cambio l'utente o la password?
#cambio utente
if scelta_cambio== "utente":                
    utente=input("Il tuo nuovo utente è:\n")
    print("il tuo nuovo nome utente è: ", utente)
elif scelta_cambio== "no modifiche": 
    print("puoi entrare nel tuo account!")
#cambio password: 
elif scelta_cambio== "psw": 
    psw_vecchia=input("la tua vecchia password è:\n") 
    if psw_vecchia== psw:
        scelta_domanda= input("vuoi rispondere alla domanda 1 o 2?") #scelta della domanda di accesso
        if scelta_domanda== "1": 
            domanda1_cambio=input("Il tuo animale preferito?\n")
            if domanda1_cambio==domanda1:
                print("puoi cambiare la tua password")
                psw_nuova=input("scrivi la tua nuova password:\n")
                print("la tua nuova password è", psw_nuova)
            else: 
                print("risposta domanda sbagliata, non puoi modificare la password")
        elif scelta_domanda== "2":
            domanda2_cambio=input("Il tuo film preferito?\n")
            if domanda2_cambio == domanda2:
                print("puoi cambiare la tua password")
                psw_nuova=input("scrivi la tua nuova password:\n")
                print("la tua nuova password è", psw_nuova)
            else: 
                print("risposta domanda sbagliata, non puoi modificare la password") 
        else: 
             pass
    else: 
         print("la password non è corretta")
else: 
     print("entra direttamente in account")

