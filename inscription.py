from tkinter import *
from tkinter import ttk
from time import strftime
from tkcalendar import DateEntry
import mysql.connector
import random 
from tkinter import messagebox
import psycopg2


s = 4
lettre = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFG"
p = "".join(random.sample(lettre,s))


#----Création de la fenetre
corps = Tk()
corps.geometry("1200x1200")
corps.title("COMPTABILITE YANN")

def Heure():
    heur = strftime("%H : %M  %S")
    var0.config(text=heur)
    var0.after(1000,Heure)

var0 = Label(corps,text="HH : MM : SS",font=("Comic Sans MS",18))
var0.place(x=3,y=2)

Heure()

#----LES VARIABLES DE RECUPERATIONS
a = IntVar()
b = IntVar()
FA  = StringVar()
FB  = StringVar()
FC  = StringVar()
FD = StringVar()
FE  = StringVar()
YANN = StringVar()
KOUAKOU = StringVar()
FRANCK = StringVar()
EPHREM = IntVar()
BIBI = StringVar()
DATE = StringVar()
x = StringVar()
varX = IntVar()
var25 = IntVar()
V = StringVar()

#----LES FONCTIONS DU LOGICIEL
#---FFONCTION QUITTER
def QUITTER():
    corps.quit()


#-----FONCTION EFFACER
def EFFACER():
    FA.set("")
    FB.set("")
    FC.set("")
    FD.set("")
    FE.set("")
    KOUAKOU.set("")
    YANN.set("")
    FRANCK.set("")
    EPHREM.set("")
    BIBI.set("")
    DATE.set("")
    x.set("")
    b.set("")
    a.set("")
    V.set("")
    var02 = Label(var32,text="",font=("Arial",14),foreground="blue")
    var02.place(x=178,y=70)
    var02.after(1000,var02.destroy())




##---FONCTION ENREGISTRER
def ENREGISTRER():

    #----Récupération table apprenant
    A = DANO.get()
    B = DANIEL.get()
    C = var8.get()
    D = varE.get()
    E = varF.get()
    

    #------Récupération table formation
    F = varZ.get()
    G = varY.get()
    H = varX.get()
    I = varW.get()
    J = varV.get()
    K = varU.get()


    if ( A =="" or  B== "" or C=="" or D=="" or E=="" or F=="" or G=="" or H=="" or I=="" or J=="" or K=="" ):
        messagebox.showerror("Info","Veuillez renseigner tous les champs")
    #---Requête 1
    else:
        connexion = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="29122003",
        database = "python",
        port=5432
        );

        curseur = connexion.cursor()

        sql = "INSERT INTO APPRENANT(Nom,Prenom,Email,Contact,Adresse,CdeFact) VALUES(%s,%s,%s,%s,%s,%s)"
        valeur = (A,B,C,D,E,p)
        curseur.execute(sql,valeur)
        #---Requête 2
        yann = "INSERT INTO  FORMATION(Nom_Formateur,Duree,Montant,Date_Inscription,Jour_de_Formation,Type) VALUES(%s,%s,%s,%s,%s,%s)"
        franck = (F,G,H,I,J,K)
        # curseur.execute(sql,valeur)
        curseur.execute(yann,franck)

        connexion.commit()
        x = FA.get()
        y = DANIEL.get()        
        z = varU.get()
        xx = varZ.get()
        yy = varW.get()
        zz = var25.get()
        oo = varX.get()
        AA = int(oo)
        BB = int(zz)
        somme = AA - BB
        
        varCode = Label(var32,text=p,font=("Arial",16),foreground="red")
        varCode.place(x=257,y=40)

        var02 = Label(var32,text=x,font=("Arial",14),foreground="blue")
        var02.place(x=178,y=70)

        var05 = Label(var32,text=y,font=("Arial",14),foreground="blue")
        var05.place(x=178,y=110)

        var06 = Label(var32,text=z,font=("Arial",14),foreground="blue")
        var06.place(x=178,y=150)

        var08 = Label(var32,text=xx,font=("Arial",14),foreground="blue")
        var08.place(x=178,y=190)

        var010 = Label(var32,text=yy,font=("Arial",14),foreground="blue")
        var010.place(x=178,y=230)

        var012 = Label(var32,text=zz,font=("Arial",14),foreground="blue")
        var012.place(x=178,y=270)

        var012 = Label(var32,text=somme,font=("Arial",14),foreground="blue")
        var012.place(x=178,y=310)

        FC.set("")
        FD.set("")

        
        FE.set("")

        FRANCK.set("")
        BIBI.set("")
        zz = var25.get()
        oo = varX.get()
        AA = int(oo)
        BB = int(zz)
        E = AA - BB
        b.set(E)

        import pyttsx3
        vocal = pyttsx3.init()
        vocal.say("Enregistrement Reussi")
        vocal.runAndWait()








var1 = Label(corps,text="COMPTABILITE YANN",borderwidth=5,background="blue",font=("Comic Sans MS",26),anchor=CENTER,border=5)
var1.place(x=460,y=0,width=500,height=70)


var2 = LabelFrame(corps,text="APPRENANT",font=("Arial",18))
var2.place(x=5,y=120,width=380,height=280)

var3 = Label(var2,text="Nom",font=("Arial",14))
var3.place(x=8,y=10)

DANO = Entry(var2,font=("Arial",14),textvariable=FA)
DANO.place(x=100,y=10)

var5 = Label(var2,text="Prenom",font=("Arial",14))
var5.place(x=8,y=50)

DANIEL = Entry(var2,font=("Arial",14),textvariable=FB)
DANIEL.place(x=100,y=50)

var7 = Label(var2,text="Email",font=("Arial",14))
var7.place(x=8,y=90)

var8 = Entry(var2,font=("Arial",14),textvariable=FC)
var8.place(x=100,y=90)

var9 = Label(var2,text="Contact",font=("Arial",14))
var9.place(x=8,y=130)

varE = Entry(var2,font=("Arial",14),textvariable=FD)
varE.place(x=100,y=130)

var11 = Label(var2,text="Adresse",font=("Arial",14))
var11.place(x=8,y=170)

varF = Entry(var2,font=("Arial",14),textvariable=FE)
varF.place(x=100,y=170)




### ---Autres lables frames 

var9 = LabelFrame(corps,text="FORMATION",font=("Arial",18))
var9.place(x=400,y=120,width=500,height=280)

Jour = ["Lundi","Mercredi","Samedi","Dimanche"]

Formation = ["A","B","C","D","E","F","G"]

varU = ttk.Combobox(corps,values=Formation,textvariable=YANN,font=("Arial",14))
# var20.current(3)
varU.place(x=570,y=360,width=230,height=26)



var10 = Label(var9,text="Nom_Formateur",font=("Arial",14))
var10.place(x=8,y=10)

varZ = Entry(var9,font=("Arial",14),textvariable=KOUAKOU)
varZ.place(x=170,y=10)

var12 = Label(var9,text="Durée",font=("Arial",14))
var12.place(x=8,y=50)

Durée = ["2mois","3mois","4mois","5mois"]

varY = ttk.Combobox(corps,font=("Arial",14),textvariable=FRANCK,values=Durée)
varY.place(x=570,y=200,height=26,width=230)

var14 = Label(var9,text="Montant",font=("Arial",14))
var14.place(x=8,y=90)

varX = Entry(var9,font=("Arial",14),textvariable=EPHREM)
varX.place(x=170,y=90)

var16 = Label(var9,text="Jour",font=("Arial",14))
var16.place(x=8,y=130)


var18 = Label(var9,text="Date_Inscription",font=("Arial",14))
var18.place(x=8,y=130)



varW = DateEntry(corps,selectmode='day',font=("Arial",14),textvariable=DATE)
varW.place(x=570,y=280,width=230,height=26)

var100 = Label(var9,text="Jour de Formation",font=("Arial",14))
var100.place(x=8,y=170)



varV = ttk.Combobox(corps,values=Jour,textvariable=BIBI,font=("Arial",14))
varV.place(x=570,y=320,width=230,height=26)
varV.current(0)




varXX = Label(var9,text="Type",font=("Arial",14))
varXX.place(x=8,y=210)




var21 = LabelFrame(corps,text="FONCTION",font=("Arial",18))
var21.place(x=8,y=410,width=895,height=250)

var22 = Label(var21,text="A payer",font=("Arial",14))
var22.place(x=8,y=10)

var23 = Entry(var21,font=("Arial",14),textvariable=EPHREM)
var23.place(x=80,y=10,width=150)

var24 = Label(var21,text="Verser",font=("Arial",14))
var24.place(x=8,y=50)

var25 = Entry(var21,font=("Arial",14),textvariable=a)
var25.place(x=80,y=50,width=150)

var26 = Label(var21,text="Reste",font=("Arial",14))
var26.place(x=8,y=90)

var27 = Entry(var21,font=("Arial",14),textvariable=b)
var27.place(x=80,y=90,width=150)


var29 = Button(var21,text="EFFACER",font=("Arial",14),background="yellow",command=EFFACER)
var29.place(x=750,y=10)

var30 = Button(var21,text="QUITTER",font=("Arial",14),background="green",command=QUITTER)
var30.place(x=250,y=160)

var31 = Button(var21,text="ENREGISTRER",font=("Arial",14),background="blue",command=ENREGISTRER)
var31.place(x=720,y=160)



var32 = LabelFrame(corps,text="FACTURE",font=("Arial",18))
var32.place(x=915,y=120,width=360,height=420)

var00 = Label(var32,text="-------COMPTABLILITE YANN-------",font=("Arial",14),foreground="blue")
var00.place(x=8,y=10)

var01 = Label(var32,text="Nom  Apprenant ",font=("Arial",14),foreground="blue")
var01.place(x=4,y=70)

var03 = Label(var32,text="Prenom  Apprenant ",font=("Arial",14),foreground="blue")
var03.place(x=4,y=110)

var05 = Label(var32,text="Formation ",font=("Arial",14),foreground="blue")
var05.place(x=4,y=150)

var07 = Label(var32,text="Nom Formateur ",font=("Arial",14),foreground="blue")
var07.place(x=4,y=190)

var09 = Label(var32,text="Date d'Inscription ",font=("Arial",14),foreground="blue")
var09.place(x=4,y=230)

var11 = Label(var32,text="Somme verset ",font=("Arial",14),foreground="blue")
var11.place(x=4,y=270)

var13 = Label(var32,text="Reste ",font=("Arial",14),foreground="blue")
var13.place(x=4,y=310)

varEE = Label(var32,text="============================ ",font=("Arial",14),foreground="blue")
varEE.place(x=4,y=350)



def IMPRIMER():
    import os
    from reportlab.pdfgen.canvas import Canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    # Le nom et prénom de l'apprenant
    nom_apprenant = FA.get()
    prenom_apprenant = FB.get()
    
    
    # Nom du fichier
    nom_fichier = f"{nom_apprenant}_{prenom_apprenant}.pdf".replace(' ', '_').replace('/', '_').replace('\\', '_')
    
    # Chemins du dossier
    dossier_principal = "E:\PERSONNEL\APPLICATION PYTHON\GESTION DES INSCRIPTIONS\LISTE PRINCIPALE FACTURES"  # Changez ce chemin en celui que vous voulez pour le stockage principal
    chemin_fichier_principal = os.path.join(dossier_principal, nom_fichier)



    # Créez le PDF
    can = Canvas(chemin_fichier_principal, pagesize=A4)
    A = DANO.get()
    B = DANIEL.get()
    C = varU.get()
    D = varZ.get()
    E = varW.get()
    F = var25.get()
    G = var27.get()
    Cde = p
    texte = "-------COMPTABLILITE YANN-------"
    Code = "Code "
    abc1 = "Nom  Apprenant "
    abc2 = "Prenom  Apprenant "
    abc3 = "Formation "
    abc4 = "Nom Formateur  "
    abc5 = "Date d'Inscription"
    abc6 = "Somme verset "
    abc6a = "Reste "
    abc7 = "============================"

    can.setFont("Helvetica-Bold",14)
    posOO,posFF = 0.5*cm,28*cm
    posCC,posFC=   4*cm,26*cm
    posA,posB = 0.5*cm,25*cm
    posC,posD = 0.5*cm,24*cm
    posE,posF=  0.5*cm,23*cm
    posG,posH = 0.5*cm,22*cm
    posI,posJ = 0.5*cm,21*cm
    posK,posL = 0.5*cm,20*cm
    posZZ,posEE = 0.5*cm,19*cm
    posM,posN = 0.5*cm,18*cm

    posCDE,posDEF = 5.5*cm,26*cm
    posO,posP = 5.5*cm,25*cm
    posQ,posR = 5.5*cm,24*cm
    posAA,posBB = 5.5*cm,23*cm
    posS,posT = 5.5*cm,22*cm
    posU,posV = 5.5*cm,21*cm
    posW,posX = 5.5*cm,20*cm
    posY,posZ = 5.5*cm,19*cm

    can.drawString(posOO,posFF,texte)
    can.drawString(posCDE,posDEF,Cde)
    can.drawString(posCC,posFC,Code)
    can.drawString(posA,posB,abc1)
    can.drawString(posC,posD,abc2)
    can.drawString(posE,posF,abc3)
    can.drawString(posG,posH,abc4)
    can.drawString(posI,posJ,abc5)
    can.drawString(posK,posL,abc6)
    can.drawString(posM,posN,abc7)
    can.drawString(posZZ,posEE,abc6a)

    can.drawString(posO,posP,A)
    can.drawString(posO,posP,A)
    can.drawString(posQ,posR,B)
    can.drawString(posAA,posBB,C)
    can.drawString(posS,posT,D)
    can.drawString(posU,posV,E)
    can.drawString(posW,posX,F)
    can.drawString(posY,posZ,G)

    can.save()
    FA.set("")
    FB.set("")
    FC.set("")
    FD.set("")
    FE.set("")
    KOUAKOU.set("")
    YANN.set("")
    FRANCK.set("")
    EPHREM.set("")
    BIBI.set("")
    DATE.set("")
    x.set("")
    b.set("")
    a.set("")

def RECHERCHER():
    connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "PYTHON");
    curseur = connexion.cursor()
    p = V.get()
    a = "SELECT Nom,Prenom,Email,Contact,Adresse FROM Apprenant WHERE CdeFact = %s";
 
    curseur.execute(a,(p,))
    resultat = curseur.fetchone()
    if resultat:
        FA.set(resultat[0])
        FB.set(resultat[1])
        FC.set(resultat[2])
        FD.set(resultat[3])
        FE.set(resultat[4])







varYANN = Button(var21,text="IMPRIMER",font=("Arial",14),background="red",command=IMPRIMER)
varYANN.place(x=250,y=10)

var001 = LabelFrame(corps,text="VERIFIER",font=("Arial",18))
var001.place(x=915,y=550,width=360,height=110)

var002 = Entry(var001,font=("Arial",14),textvariable=V)
var002.place(x=10,y=10,width=170)

var003 = Button(var001,text="Rechercher",font=("Arial",14),command=RECHERCHER)
var003.place(x=190,y=4,width=160)





corps.mainloop()