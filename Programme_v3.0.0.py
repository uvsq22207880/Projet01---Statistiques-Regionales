


# Partie 1: Les outils. 


# Les librairies .
from tkinter import *
from math import*    
from tkinter import filedialog
import random 
import pandas as pd
import matplotlib.pyplot as plt

    
################################################################################################################################################################
    #####################################################################################################################################################   
   ####                                                                                                                                               ####
  ####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                #### 
 ####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                  ####
####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                    #### 
####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                     ####
####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                     #### 
####              ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                    ####
 ####              ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                  #### 
  ####              ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                ####
   ####                                                                                                                                               ####            
    #####################################################################################################################################################



#1A)
# (a) Une fonction nommée cree_fichier_alea(nb, nomfichier) prenant un argument entier et un autre chaine de caracteres
def cree_fichier_alea(nb, nomfichier):

    with open(nomfichier, 'w') as fichier_alea:                    # on utilise 'a' append, aulieux de 'w' write qui ecrase le fichier
                                                                   # nb est notre entier dans ce cas et 'w' ou 'a' notre methode d'ecriture.
        i = 0
        while i < nb :
            x = random.uniform(0, 500)                             # Random.uniform pour que nb soit un float /.randint pour un integer 
            y = random.uniform(0, 500)
            fichier_alea.write(f'{x} {y}\n'.format(x, y))          # Le code .format() est une méthode utilisée pour formater des chaînes de caractères en Python. Il permet d'insérer des variables, des valeurs numériques et des chaînes de caractères dans une chaîne de caractères. Cela permet aux développeurs de créer des chaînes de caractères plus lisibles et plus faciles à maintenir.
            i = i + 1

#1B)
# (b) coder une fonction qui represente le nom d'un fichier sur le disque.
def lit_fichier(nom_fichier): 
    listeX_abs = []                                                # doit contenir la colonne 1 de exemple.txt
    listeY_ord = []                                                # doit contenir la colonne 2 de exemple.txt
    with open(nom_fichier, 'r') as fichier_alea: 
        for line in fichier_alea: 
            x, y = line.split() 
            listeX_abs.append(float(x)) 
            listeY_ord.append(float(y)) 

    return listeX_abs, listeY_ord

#1C)
# c) fonction qui appele la fonction lit_fichier()pour obtenir les coordonées des points de nuages.
def trace_Nuage(nomfichier):          # définit une fonction nommée trace_Nuage qui prend en paramètre le nom du fichier à lire.
    points = lit_fichier(nomfichier)  # La fonction lit le fichier et stocke les données dans une liste appelée points.
    x = points[0]                     # Les données sont ensuite extraites de cette liste et stockées dans deux autres listes appelées x et y, qui contiennent  les valeurs des x=abscisses / y=ordonnées. 
    y = points[1]
    plt.close()
    plt.plot(x, y, 'o')               # la fonction plt.plot est utilisée pour tracer un graphique à partir des données stockées dans x et y
    plt.show()                        # plt.show est utilisée pour afficher le graphique sur l'écran
    return len(points)                # .len retourne également la longueur de la liste points (c'est-à-dire le nombre de points)


# 1D)
# (d) fonction qui determine les coordonées de 2 points de cette droite afin qu'une ligne reliant ces 2 points soit représentée graphiquement.
def trace_droite(a, b):
    x1 = 0                            # x1 est choisis au hasard
    y1 = a * x1 + b                   # equation d'une droite "ax+b"
    x2 = 1000                         # x2 est choisis au hasard
    y2 = a * x2 + b 
    plt.close()
    plt.plot([x1, x2,], [y1, y2,], color='g') 
    plt.show()

################################################################################################################################################################
    #####################################################################################################################################################   
   ####                                                                                                                                               ####
  ####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                #### 
 ####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                  ####
####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                    #### 
####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                     ####
####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                     #### 
####              ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                    ####
 ####              ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                  #### 
  ####              ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                ####
   ####                                                                                                                                               ####            
    #####################################################################################################################################################

# Partie-2 : Calcules Statistiques.

#ref: http://www.france-ioi.org/algo/course.php?idChapter=653&idCourse=2020

#2A)
def moyenne(serie_stat):             #definition de la fonction (avec serie_stat comme argument)
    somme = 0                        #initialisation de la somme 
    for nombre in serie_stat:        # pour chaque element (nombre,nom...) dans la liste (serie statistique)
        somme += nombre              # la somme= somme+ element(nombre)
    return somme / len(serie_stat)   # retourne la somme de la liste et sa longueur (len=5(pour l'exemple))

#2B)
def variance(serie_stat):
    moyenne_b = moyenne(serie_stat)     
    somme_ecarts_carres = 0
    for element in serie_stat:
        loi_variance = (element - moyenne_b)**2 #var (Y )=Σ/i=1n ( yi−̄y)²/n
        somme_ecarts_carres += loi_variance

    variance = somme_ecarts_carres / (len(serie_stat))

    return variance

#2C)
def covariance(serieX, serieY):
    moyenneX = moyenne(serieX)
    moyenneY = moyenne(serieY)
    somme = 0
    for e in range(len(serieX)):
        somme += (serieX[e] - moyenneX)*(serieY[e] - moyenneY)
    return somme / (len(serieX))

#2D)
def correlation(serieX, serieY): 
    varX = variance(serieX) 
    varY = variance(serieY) 
    covXY = covariance(serieX, serieY) 
    return covXY/sqrt(varX*varY)

#2E)
def forteCorrelation(serieX, serieY):
    corSxSy = correlation(serieX, serieY)
    print(corSxSy)
    if (corSxSy > abs(0.8) or corSxSy < -0.8):
        return True 
    
    else: 
        return False

#2F)
def droite_reg(serieX, serieY): 
  # Calculer la moyenne des séries X et Y
  moyX = moyenne(serieX) 
  moyY = moyenne(serieY) 

  # Calculer le coefficient directeur de la droite de régression
  coeff_dir = covariance(serieX,serieY)/variance(serieX)

  # Calculer l'ordonnée à l'origine de la droite de régression
  ord_orig = moyY - coeff_dir * moyX

  return (coeff_dir, ord_orig)
    
################################################################################################################################################################
    #####################################################################################################################################################   
   ####                                                                                                                                               ####
  ####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                #### 
 ####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                  ####
####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                    #### 
####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                     ####
####             ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                     #### 
####              ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                    ####
 ####              ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                  #### 
  ####              ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####    ####                ####
   ####                                                                                                                                               ####            
    #####################################################################################################################################################


    # Partie-3 : Programme Principal.

# Listes partie3 - ABCD
colors= ["red", "green", "blue", "orange","black","purple","cyan"] 
color = random.choice(colors)

fichierB = ""
serie_X3B = [] 
serie_Y3B = []

fichierC = "exemple.txt"
serie_X3C, serie_Y3C = lit_fichier(fichierC)

serieXD = []
serieYD = []


    #Partie-3 : A/B/C)
def Partie3_ABC():
    import random
    
  

    #3A2)
    def autre_couleur():
        global color
        color = random.choice(colors)
        print("je change de couleur et j'ai maintenant du " , color)
        label_couleur_utilise.configure(text=(f"Couleur    : {color}"),fg='white',bg='gray11', font='arial 8 bold')
    ####
    def tracer_droite():
        X1 = random.randint(50, 400)	                      
        Y1 = random.randint(50, 400)  	                   
        X2 = random.randint(50, 400)  	                   
        Y2 = random.randint(50, 400)
        canevas.create_line(X1,Y1,X2,Y2, fill = color) 
    #3A3)
    def quitter():
        fenetre.destroy()
   
    def effacer ():
        canevas.delete(ALL)
    #3B
    def creation_fichier_alea_50():
        global fichierB
        global serie_X3B, serie_Y3B
    #  Créer un nuage de points aléatoire de 50 points et le représenter graphiquement
        cree_fichier_alea(50,"fichier_alea_50.txt")
        fichierB="fichier_alea_50.txt"
        print("Fichier créé")
        label_fich_cree.configure(text=(f"{fichierB} Crée avec succés"),fg='white',bg='gray11', font='arial 8 bold')
        serie_X3B, serie_Y3B = lit_fichier(fichierB)

    def trace_nuage_alea():

        trace_Nuage(fichierB) 
    #3C
    def charger_fichier_exemple () : 
        global fichierC
        global serie_XC, serie_YC
        # fichier = input("Entrez le nom d'un fichier.txt pour tracer un nuage de points :") # 3B) le nom d'un fichier texte a input # a supprimer...
        fichierC = filedialog.askopenfile(mode='rb',title='choisir fichier').name # le point name est la pour specifier que fichier n'est plus une class mais un nom str
        serie_XC, serie_YC = lit_fichier(fichierC)
        label_fich_charge.configure(text=(f"{fichierC}"),fg='yellow',bg='gray11', font='arial 8 bold')

    def trace_nuage_exemple():

        trace_Nuage(fichierC) 

    def reg_ABC_alea(a, b):
         x1_ABC = min(serie_X3B)                   # x1 est le plus petit element de la liste
         y1_ABC = a * x1_ABC + b                      # Equation d'une droite "ax+b"
         x2_ABC = max(serie_X3B)                   # x2 est le plus grand element de la liste
         y2_ABC = a * x2_ABC + b 
         plt.close()
         plt.plot([x1_ABC, x2_ABC,], [y1_ABC, y2_ABC,], color='green') 
         plt.show()

    def reg_alea ():
        # Calculer le coefficient de corrélation des points du nuage (en prenant comme sérieX, la série des abscisses des points du nuage, et comme série Y la série des ordonnées des points du nuage)  
        corXY = correlation(serie_X3B, serie_Y3B)
        # Utiliser la fonction forte_correlation() pour décider s'il est pertinent de tracer la droite de régression ou pas  
        if forteCorrelation(serie_X3B, serie_Y3B) is True:
            label_corre_fich_cree.config(text=(f"Corrélation F.alea : {corXY}, Pertinent de tracer cette droite"),fg='white',bg='gray11', font='arial 8 bold')
            reg_ABC_alea(droite_reg(serie_X3B, serie_Y3B)[0],droite_reg(serie_X3B, serie_Y3B)[1])
        else:
            label_corre_fich_cree.config(text=(f"Corrélation F.alea : {corXY}, Non Pertinent de tracer cette droite"),fg='white',bg='gray11', font='arial 8 bold')

    def reg_ABC_exemple(a, b):
         x1_ABC = min(serie_X3C)                  # x1 est le plus petit element de la liste
         y1_ABC = a * x1_ABC + b                    # equation d'une droite "ax+b"
         x2_ABC = max(serie_X3C)                  # x2 est le plus grand element de la liste
         y2_ABC = a * x2_ABC + b 
         plt.plot([x1_ABC, x2_ABC], [y1_ABC, y2_ABC], color='red') 
         plt.show()

    def reg_exemple ():
        # Calculer le coefficient de corrélation des points du nuage (en prenant comme sérieX, la série des abscisses des points du nuage, et comme série Y la série des ordonnées des points du nuage)  
        corXY = correlation(serie_X3C, serie_Y3C)
        

        # Utiliser la fonction forte_correlation() pour décider s'il est pertinent de tracer la droite de régression ou pas  
        if forteCorrelation(serie_X3C, serie_Y3C) is True:
            label_corre_fich_charge.configure(text=(f"Corrélation F.chargé : {corXY}, Pertinent de tracer cette droite"),fg='white',bg='gray11')
            reg_ABC_exemple(droite_reg(serie_X3C, serie_Y3C)[0],droite_reg(serie_X3C, serie_Y3C)[1])

        else:
            label_corre_fich_charge.configure(text=(f"Corrélation F.chargé : {corXY}, Non Pertinent de tracer cette droite "),fg='white',bg='gray11')


  #3A1) initialisation de la fenetre abc:
    fenetre = Tk()
    fenetre.title("Partie3_ABC")
    fenetre.config(bg='grey11')
    canevas = Canvas(fenetre, width=450, height=500, background="ivory",borderwidth=5,relief='raised')
    canevas.grid(column=0, row=1,columnspan=4)
    

       # les widgets de la fenetre tkinter
  #A   
    btn_tracer_droite = Button(fenetre, font='arial 8 bold',relief='groove',text="Tracer la droite", fg='white',bg='black'                   ,command=tracer_droite)
    btn_autre_couleur = Button(fenetre, font='arial 8 bold',relief='groove',text="Changer couleur", fg='white',bg='black'                    ,command=autre_couleur)
    btn_effacer = Button(fenetre, font='arial 8 bold',relief='groove',text="Effacer", fg='white',bg='black'                                  ,command=effacer)
       

    btn_quitter = Button(fenetre, font='arial 8 bold',relief='groove',text=" Quitter ", fg='white',bg='red'                                  ,command=quitter)
  #B   
    btn_creation_fichier_alea_50= Button(fenetre, font='arial 8 bold',relief='groove',text=" Créer fichier aléatoire ", fg='white',bg='black',command=creation_fichier_alea_50)
    btn_trace_nuage_alea = Button(fenetre, font='arial 8 bold',relief='groove',text="Tracer points crée", fg='white',bg='black'              ,command=trace_nuage_alea) 
    btn_regression = Button(fenetre, font='arial 8 bold',relief='groove',text="Régression points crée", fg='white',bg='black'                ,command=reg_alea)
  #C   
    btn_charger_fichier_exemple =Button(fenetre, font='arial 8 bold',relief='groove',text='Charger fichier',fg='white',bg='black'            ,command=charger_fichier_exemple)
    btn_trace_nuage_exemple = Button(fenetre, font='arial 8 bold',relief='groove',text="Tracer nuage exemple", fg='white',bg='black'         ,command=trace_nuage_exemple) 
    btn_regression_exemple = Button(fenetre, font='arial 8 bold',relief='groove',text="Régression exemple", fg='white',bg='black'            ,command=reg_exemple)
       
       # Labels
    frame_labelsABC = Frame(fenetre,border=5,bg='gray11')

    label_fich_cree        = Label(frame_labelsABC,text='', font='arial 8 bold',bg='grey11') 
    label_fich_charge      = Label(frame_labelsABC,text='', font='arial 8 bold',bg='grey11') 

    label_corre_fich_cree  = Label(frame_labelsABC,text='', font='arial 8 bold',bg='grey11') 
    label_corre_fich_charge= Label(frame_labelsABC,text='', font='arial 8 bold',bg='grey11')  

    label_couleur_utilise  = Label(frame_labelsABC,text='', font='arial 8 bold',bg='grey11') 
       # Emplacements des widget 
    frame_labelsABC             .grid(column=0,row=3,columnspan=4,sticky='ew')
    label_fich_cree             .grid(column=0,row=0,stick='w') 
    label_fich_charge           .grid(column=0,row=1,stick='w') 
    label_corre_fich_cree       .grid(column=0,row=2,stick='w') 
    label_corre_fich_charge     .grid(column=0,row=3,stick='w') 
    label_couleur_utilise       .grid(column=0,row=4,stick='w') 

   
  #A
    btn_tracer_droite           .grid(column=0, row=4,sticky="ew")
    btn_autre_couleur           .grid(column=0, row=5,sticky="ew")
    btn_effacer                 .grid(column=0, row=6,sticky="ew")

  #B
    btn_creation_fichier_alea_50.grid(column=1, row=4,sticky="ew")
    btn_trace_nuage_alea        .grid(column=1, row=5,sticky="ew")
    btn_regression              .grid(column=1, row=6,sticky="ew")
  #C
    btn_charger_fichier_exemple .grid(column=2, row=4,sticky="ew")
    btn_trace_nuage_exemple     .grid(column=2, row=5,sticky='ew')
    btn_regression_exemple      .grid(column=2,row=6,sticky="ew")
  
    btn_quitter                 .grid(column=3, row=6,sticky="ew")
   
    

  
    # Barre de menus
    mon_menu = Menu(fenetre)
    fenetre.config(menu=mon_menu)

    # Menu Trace
    Tracer = Menu(mon_menu, tearoff=0)
  #A
    Tracer.add_command(label="1. Tracer la droite ", font='arial 8',                 command=tracer_droite)
    Tracer.add_command(label="2. Changer couleur ",font='arial 8',                   command=autre_couleur)
    Tracer.add_separator()
  #B
    Tracer.add_command(label="3. Créer un fichier",font='arial 8',                   command= creation_fichier_alea_50,)
    Tracer.add_command(label="4. Tracer points du fichier crée",font='arial 8',      command=trace_nuage_alea ,)
    Tracer.add_command(label="5. Régression du fichier crée",font='arial 8',         command=reg_alea ,)     
    Tracer.add_separator()             
  #C
    Tracer.add_command(label="6. Charger un fichier",font='arial 8',                 command=charger_fichier_exemple)               
    Tracer.add_command(label="7. Tracer les points du fichier chargé",font='arial 8',command= trace_nuage_exemple)
    Tracer.add_command(label="8. Régression du fichier chargé",font='arial 8',       command= reg_exemple)       
    Tracer.add_separator()
    Tracer.add_command(label="9. Effacer",font='arial 8 bold',                       command= effacer)   
    Tracer.add_command(label="10. Quitter ",font='arial 8 bold',                     command=quitter)
    
    mon_menu.add_cascade(label="Tracer", menu=Tracer)

    
    
    fenetre.mainloop()
####

####     

    #Partie-3 : D)

def Partie3_D() :

    #3D)
    import random 
    global serieXD
    global serieYD
    #### 

    def change_couleur ():
        global color
        color = random.choice(colors)
        print("Couleur       :",color)
        label_couleur3D.configure(text=(f"Couleur       : {color}"))
   
    def mode_dessin ():
        label_State.config(text="Dessin         : ON")  
        def dessiner(event):
            global serieXD
            global serieYD
            canevas.create_oval(event.x, event.y,event.x+5, event.y+5, fill = color ,outline=[])
            serieXD.append(event.x) 
            serieYD.append(event.y)
            print (serieXD,serieYD)
        canevas.bind("<B1-Motion>", dessiner)
    
    def delier_bouton ():
         canevas.unbind("<B1-Motion>") 
     
    def desactiver_mode_dessin (): 
        if (btn_mode_dessin['state'] == NORMAL):
            btn_mode_dessin['state'] = DISABLED 
            delier_bouton()
            label_State.config(text="Dessin         : OFF")
        else:
            btn_mode_dessin['state'] = NORMAL
            mode_dessin ()
            label_State.config(text="Dessin         : ON")  

    def trace_droiteD(a, b):
         x1_D = min(serieXD)                    # x1 est le plus petit element de la liste
         y1_D = a * x1_D + b                    # Equation d'une droite "ax+b"
         x2_D = max(serieXD)                    # x2 est le plus grand element de la liste
         y2_D = a * x2_D + b 
         plt.plot([x1_D, x2_D,], [y1_D, y2_D,], color='red') 
         plt.show()

    def droite_reg_mode_deesin ():
        corSxSy = correlation(serieXD, serieYD)

        if forteCorrelation(serieXD, serieYD) is False:
            label_coef_reg3D.configure(text=(f"Correlation : {corSxSy}, Non pértinent de tracer cette droite"),fg='white')

        else:
            label_coef_reg3D.configure(text=(f"Correlation : {corSxSy}, Pértinent de tracer cette droite"),fg='white')

            serieYD_mirroir= []
            for i in serieYD : 
                serieYD_mirroir.append(-1 * i)
            plt.plot(serieXD, serieYD_mirroir, 'o')   
            trace_droiteD(droite_reg(serieXD, serieYD_mirroir)[0],droite_reg(serieXD, serieYD_mirroir)[1])
                
    def effacer ():
        # plt.close()
        canevas.delete(ALL)
        global serieXD
        global serieYD
        serieXD[:] = [] # On vide l'entierté de la serie a chaque fois qu'on efface le dessin pour eviter l'accumulation des points
        serieYD[:] = []
     
    def quitter ():
        plt.close()
        fenetre.destroy()
# initisation fenetre D :
    fenetre = Tk ()
    fenetre.title("Partie-3: D")
    fenetre.config(bg="grey11")
   
        # Barre de menus
    mon_menu = Menu(fenetre)
    fenetre.config(menu=mon_menu)
    Dessin = Menu(mon_menu, tearoff=0)
   
# commandes menu 
    Dessin.add_command(label="1. Dessiner"              ,font= 'arial 8'      , command=mode_dessin)
    Dessin.add_command(label="2. Changer de couleur"    ,font= 'arial 8'      , command=change_couleur)
    Dessin.add_command(label="3. Résgression des points",font= 'arial 8'      , command=droite_reg_mode_deesin)
    Dessin.add_command(label="4. Effacer le dessin "    ,font= 'arial 8'      , command=effacer)
    Dessin.add_separator()
    Dessin.add_command(label="5. Dessin : ON / OFF"     ,font= 'arial 8'      , command=desactiver_mode_dessin)
    
    mon_menu.add_cascade(label="Dessin", menu=Dessin)
    
    
    
    # Les widgets:
    canevas = Canvas(fenetre, width=500, height=300, bg="DarkSlateGray",bd=5,relief='raised')


    btn_mode_dessin            = Button(fenetre, text="Mode Dessin",state= NORMAL,font='arial 8 bold',fg='white',bg='black',relief=GROOVE,command=mode_dessin)
    btn_desactiver_mode_dessin = Button(fenetre, text="Dessin : ON / OFF"        ,font='arial 8 bold',fg='white',bg='black',relief=GROOVE,command=desactiver_mode_dessin)
    btn_autre_couleur          = Button(fenetre, text="Autre couleur"            ,font='arial 8 bold',fg='white',bg='black',relief=GROOVE,command=change_couleur)
    btn_gomme_canvas           = Button(fenetre, text="Effacer"                  ,font='arial 8 bold',fg='white',bg='black',relief=GROOVE,command=effacer)

    btn_regression             = Button(fenetre, text="Régression"               ,font='arial 8 bold',fg='white',bg='black',relief=GROOVE,command=droite_reg_mode_deesin)
    btn_quitter                = Button(fenetre, text="Quitter"                  ,font='arial 8 bold',fg='white',bg='red',relief=GROOVE, command=quitter)  
   
    frame_labelsD  = Frame(fenetre,border=2,bg="gray11")
    label_State            = Label(frame_labelsD,text="Dessin         :"         ,font='arial 8 bold',fg='white',bg='grey11')
    label_couleur3D        = Label(frame_labelsD,text="Couleur       :"          ,font='arial 8 bold',fg='white',bg='grey11')
    label_coef_reg3D       = Label(frame_labelsD,text="Correlation :"            ,font='arial 8 bold',fg='white',bg='grey11') #2
    
    # Emplacements des widget
    canevas                   .grid(column=0, row=0,columnspan=3)
    
    frame_labelsD             .grid(column=0,row=1,columnspan=3,sticky='ew')
    label_State               .grid(column=0,row=0,stick='w')
    label_couleur3D           .grid(column=0,row=1,stick='w')
    label_coef_reg3D          .grid(column=0,row=2,stick='w')
  
    btn_mode_dessin           .grid(column=0, row=3,sticky="ew")
    btn_desactiver_mode_dessin.grid(column=0, row=4,sticky="ew")

    btn_autre_couleur         .grid(column=1, row=3,sticky="ew")
    btn_gomme_canvas          .grid(column=1, row=4,sticky="ew")                    
    
    btn_regression            .grid(column= 2,row=3,sticky="ew")
    btn_quitter               .grid(column=2, row=4,sticky="ew")
    







    fenetre.mainloop()
####

####     

N_Lignes = 5
serie_X3E_100 = []
serie_Y3E_100 = []
serie_X3E_N = []
serie_Y3E_N = []
#Partie-3 : E/F/G)
def Partie3_EFG() :

    #3E)N
    # serie_X3E = []
    # serie_Y3E = []
    
    nom_fichier= "villes_virgule.csv" # fichier par defaut
    def charger_fichier () : 
        global fichier
        nom_fichier = filedialog.askopenfile(mode='rb',title='choisir un fichier').name # le point name est la pour specifier que fichier n'est plus une class mais un nom str
        print(nom_fichier)
        label_nomf.config(text=nom_fichier)
    # def extraire_habitants():
    #     lit_fichier_csv = pd.read_csv(nom_fichier) #nom_fichier=str
    #  #   Extraire les nombres d'habitants inférieurs ou égaux à 500
    #     hab_2010 = lit_fichier_csv[lit_fichier_csv['nb_hab_2010'] <= 200]['nb_hab_2010']
    #     hab_2012 = lit_fichier_csv[lit_fichier_csv['nb_hab_2012'] <= 1000]['nb_hab_2012']
    #     return [list(hab_2010), list(hab_2012)]
       #  Retourner la liste des nombres d'habitants inférieurs ou égaux à 500
    
    def extraire_colonnes():
        lit_fichier_csv = pd.read_csv(nom_fichier) # nom_fichier=str

        # extraction selon lindex et le nom du fichier : (dep	nom	cp	nb_hab_1999	nb_hab_2010	nb_hab_2012	dens	surf	long	lat	alt_min)
        dep         = lit_fichier_csv['dep']
        nom         = lit_fichier_csv['nom']
        cp          = lit_fichier_csv['cp']
        nb_hab_1999 = lit_fichier_csv['nb_hab_1999']
        nb_hab_2010 = lit_fichier_csv['nb_hab_2010']
        nb_hab_2012 = lit_fichier_csv['nb_hab_2012']
        dens        = lit_fichier_csv['dens']
        surf        = lit_fichier_csv['surf']
        longitude   = lit_fichier_csv['long']
        lat         = lit_fichier_csv['lat']
        alt_min     = lit_fichier_csv['alt_min']
        alt_max     = lit_fichier_csv['alt_max']

   
        return [list(dep),list(nom),list(cp),list(nb_hab_1999),list(nb_hab_2010),list(nb_hab_2012), list(dens),list(surf),list(longitude), list(lat),list(alt_min), list(alt_max)]
   
   
   
    serie_dep          = extraire_colonnes()[0]
    serie_nom          = extraire_colonnes()[1]
    serie_cp           = extraire_colonnes()[2]
    serie_nb_hab_1999  = extraire_colonnes()[3]
    serie_nb_hab_2010  = extraire_colonnes()[4]
    serie_nb_hab_2012  = extraire_colonnes()[5]
    serie_dens	       = extraire_colonnes()[6]
    serie_surf	       = extraire_colonnes()[7]
    serie_longitude    = extraire_colonnes()[8]
    serie_lat	       = extraire_colonnes()[9]
    serie_alt_min      = extraire_colonnes()[10]
    serie_alt_max      = extraire_colonnes()[11]

    
   # Séries tronquées
    serie_dep_36568          = []
    serie_nom_36568          = []
    serie_cp_36568           = []
    serie_nb_hab_1999_36568  = []
    serie_nb_hab_2010_36568  = []
    serie_nb_hab_2012_36568  = []
    serie_dens_36568	     = []
    serie_surf_36568         = []
    serie_longitude_36568    = []
    serie_lat_36568	         = []
    serie_alt_min_36568      = []
    serie_alt_max_36568      = []


    # 
    for i in range (0,36568):
        serie_dep_36568.append(serie_dep[i])
        serie_nom_36568.append(serie_nom[i])
        serie_cp_36568.append(serie_cp[i])
        serie_nb_hab_1999_36568.append(serie_nb_hab_1999[i])
        serie_nb_hab_2010_36568.append(serie_nb_hab_2010[i])
        serie_nb_hab_2012_36568.append(serie_nb_hab_2012[i])
        serie_dens_36568.append(serie_dens[i])
        serie_surf_36568.append(serie_surf[i])
        serie_longitude_36568.append(serie_longitude[i])
        serie_lat_36568.append(serie_lat[i])
        serie_alt_min_36568.append(serie_alt_min[i])
        serie_alt_max_36568.append(serie_alt_max[i])


    #3E)
    # 100 points pour repondre a la question de l'exercice
    for i in range (0,10):
        serie_X3E_100.append(serie_nb_hab_2010[i])
        serie_Y3E_100.append(serie_nb_hab_2012[i])  

    # Choisis par l'utilisateur
    for i in range (0,N_Lignes):
        serie_X3E_N.append(serie_nb_hab_2010[i])    
        serie_Y3E_N.append(serie_nb_hab_2012[i])
    

    def trace_Nuage_liste_100():
        abscice_nuage100 = []
        ordonne_nuage100 = []
        abscice_nuage100 = serie_X3E_100
        ordonne_nuage100 = serie_Y3E_100
        plt.close()
        plt.plot(serie_X3E_100, serie_Y3E_100, 'o')
        plt.show()
        return (abscice_nuage100, ordonne_nuage100)   

    def trace_Nuage_liste_N():
        # global serie_X3E_N 
        # global serie_Y3E_N
        plt.close()
        plt.plot(serie_X3E_N, serie_Y3E_N, 'o')
        plt.show()

    def trace_Nuage_long_latT():
        plt.close()        
        plt.plot(serie_longitude_36568,serie_lat_36568, '+')
        plt.axis('equal')
        plt.show()
    
    def trace_Nuage_liste_AminLong():
                
        plt.plot(serie_longitude_36568,serie_alt_min_36568, '+')
        plt.show()

    def trace_Nuage_liste_AmaxLong():
        plt.close()       
        plt.plot(serie_longitude_36568,serie_alt_max_36568, '+')
        plt.show()

    def trace_droite_EFG_100(a, b):
         x1_EFG = min(serie_X3E_100)               #x1 est le plus petit element de la liste
         y1_EFG = a * x1_EFG + b                   # equation d'une droite "ax+b"
         x2_EFG = max(serie_X3E_100)               #x2 est le plus grand element de la liste
         y2_EFG = a * x2_EFG + b 
         plt.plot([x1_EFG, x2_EFG,], [y1_EFG, y2_EFG,], color='green') 
         plt.axis('equal')
         plt.show()

    def trace_droite_EFG_N(a, b):
         x1_EFG = min(serie_X3E_N)
         y1_EFG = a * x1_EFG + b
         x2_EFG = max(serie_X3E_N)
         y2_EFG = a * x2_EFG + b 
         plt.plot([x1_EFG, x2_EFG,], [y1_EFG, y2_EFG,], color='red') 
         plt.show()

    def tracer_droite_reg_sur_graphe_100():
        
        if forteCorrelation (serie_X3E_100,serie_Y3E_100) is True:                                                                                     
            trace_droite_EFG_100(droite_reg(serie_X3E_100,serie_Y3E_100)[0],droite_reg(serie_X3E_100,serie_Y3E_100)[1]) 
            label_coeff100.config(text="Pértinent de tracer une droite de régression",fg="white")                                           
        else:                          
            label_coeff100.config(text="Non pértinent de tracer une droite de régression",fg="white")                                           
            pass  
        
    def tracer_droite_reg_sur_graphe_N():    

        if forteCorrelation (serie_X3E_N,serie_Y3E_N) is True:
            trace_droite_EFG_N(droite_reg(serie_X3E_N,serie_Y3E_N)[0],droite_reg(serie_X3E_N,serie_Y3E_N)[1])
            label_coeffN.config(text="Pértinent de tracer une droite de régression",fg="white")                                           

        else:
            label_coeffN.config(text="Non pértinent de tracer une droite de régression",fg="white")                                           
            pass                
     
    def soummetre_N ():
        
        global N_Lignes
        global serie_X3E_N
        global serie_Y3E_N
        

        N_Lignes= entry_N.get()
        N_Lignes=int(N_Lignes)
        print(N_Lignes)
        label_entry.config(text=f"Entrez le nombre de lignes à éxtraire: N = {N_Lignes}")
        # label_Nlignes.config(text=(N_Lignes))
        serie_X3E_N = []
        serie_Y3E_N = []

        for i in range (0,N_Lignes):

            serie_X3E_N.append(serie_nb_hab_2010[i])
            serie_Y3E_N.append(serie_nb_hab_2012[i])
        entry_N.delete(0, END)
        print("serie_X3E_N=",serie_X3E_N)
        print("serie_Y3E_N=",serie_Y3E_N)

    def verif_entry(N):
      
        if N.isdigit():
            return True
        # elif N == "":
        #     # Retourne True si l'utilisateur a effacé tout le texte dans l'Entry
        #     return True
        else:
            # Retourne False dans tous les autres cas
            return False
 
    def quitter():
        
        plt.close() 
        fenetre.destroy()

    # Initialisation fenetre EFG
    fenetre = Tk()
    fenetre.title("Partie-3: EFG")
    fenetre.config(bg='grey11')
    # les widgets de la fenetre tkinter EFG .

    canevas = Canvas(fenetre, bg="DarkSlateGray",width=550,height=200,bd=5,relief='raised')

    frame_label_info_efg=Frame(fenetre,bg="gray11",padx=0)
    label_nomf =     Label(frame_label_info_efg,text="",font= "arial 8 bold",bg="gray11",fg="white")
    label_coeffN =   Label(frame_label_info_efg,text="",font= "arial 8 bold",bg="gray11",fg="white")
    label_coeff100 = Label(frame_label_info_efg,text="",font= "arial 8 bold",bg="gray11",fg="white")
    
    frame_entry=  Frame(fenetre,bg="gray11",padx=0)

    label_entry=   Label(frame_entry,text="Entrez le nombre de lignes à extraire: N = 5", font='calibri 10 bold',bg='gray11',fg='white')
    entry_N =      Entry(frame_entry,width=40,relief=RIDGE,fg='black',bg='white',justify=RIGHT,borderwidth=5, validate='key')
    # pour qu'on ne puisse pas taper nimporte quoi dans l'entry 
    entry_N['validatecommand'] = (entry_N.register(verif_entry), '%S')
    btn_soumettre=              Button(frame_entry,padx=5, font='arial 8 bold', relief='groove', text='Valider',  fg='white',bg='green', command=soummetre_N)
    
    btn_trace_nuage_100 =       Button(fenetre, font='arial 8 bold',relief='groove',text=" Tracer 100 points ",   fg='white',bg='black', command=trace_Nuage_liste_100)
    btn_tracer_droite_reg_100 = Button(fenetre, font='arial 8 bold',relief='groove',text=" Régression 100 points",fg='white',bg='black', command=tracer_droite_reg_sur_graphe_100)

    btn_trace_nuage_N =         Button(fenetre, font='arial 8 bold',relief='groove',text=" Tracer N points",      fg='white',bg='black', command=trace_Nuage_liste_N)
    btn_tracer_droite_reg_N =   Button(fenetre, font='arial 8 bold',relief='groove',text=" Régression N points",  fg='white',bg='black', command=tracer_droite_reg_sur_graphe_N)

    btn_charger =               Button(fenetre, font='arial 8 bold',relief='groove',text=" Charger fichier ",     fg='white',bg='black', command=charger_fichier)
    btn_quitter =               Button(fenetre, font='arial 8 bold',relief='groove',text=" Quitter ",             fg='white',bg='red',   command=quitter)

    btn_carte_france=           Button(fenetre, font='arial 8 bold',relief='groove',text=" Villes de France ",    fg='white',bg='gray25',command=trace_Nuage_long_latT)
    btn_trace_nuage_AminLong  = Button(fenetre, font='arial 8 bold',relief='groove',text=" Altitudes minimales ", fg='white',bg='gray25',command=trace_Nuage_liste_AminLong)
    btn_trace_nuage_AmaxLong  = Button(fenetre, font='arial 8 bold',relief='groove',text=" Altitudes maximales ", fg='white',bg='gray25',command=trace_Nuage_liste_AmaxLong)

       # Emplacements des widgets EFG.
    canevas.grid(column=0, row=0,columnspan=3,rowspan=9)
       
       # Emplacement labels EFG
    frame_label_info_efg.grid(column=0,row=10,columnspan=4,sticky='ew')
    label_nomf.          grid(column=0,row=1,stick='w')
    label_coeffN.        grid(column=0,row=3,stick='w')
    label_coeff100.      grid(column=0,row=4,stick='w')


       # Emplacement Entry EFG + labels + btn
    frame_entry.  grid(column=0,row=11,columnspan=3)
    label_entry.  grid(column=0,row=1,sticky="w")
    # label_Nlignes.grid(column=1,row=1,sticky="e")
    entry_N.      grid(column=1,row=1)
    btn_soumettre.grid(column=2,row=1,sticky="w")
       # Emplacement boutons EFG
    btn_trace_nuage_100.      grid(column=0,row=12,sticky="nsew")
    btn_tracer_droite_reg_100.grid(column=0,row=13,sticky="nsew")

    btn_trace_nuage_N.        grid(column=1,row=12,sticky="nsew")
    btn_tracer_droite_reg_N.  grid(column=1,row=13,sticky="nsew")
    
    btn_charger.              grid(column=2,row=12,sticky="nsew")
    btn_quitter.              grid(column=2,row=13,sticky="nsew")

    btn_carte_france.         grid(column=3,row=0,sticky='nsew')
    btn_trace_nuage_AminLong. grid(column=3,row=1,sticky='nsew')
    btn_trace_nuage_AmaxLong. grid(column=3,row=2,sticky='nsew')
    
   # Barre de menus EFG
    mon_menu = Menu(fenetre)
    Tracer = Menu(mon_menu, tearoff=0)  
    fenetre.config(menu=mon_menu)

    # Menu Trace EFG
    Tracer.add_command(label="1. Tracer N points",font='arial 8 bold',      command=trace_Nuage_liste_N)
    Tracer.add_command(label="2. Régression N points",font='arial 8 bold',  command=tracer_droite_reg_sur_graphe_N)
    Tracer.add_separator()
    Tracer.add_command(label="3. Tracer 100 points",font='arial 8 bold',    command=trace_Nuage_liste_100)
    Tracer.add_command(label="4. Régression 100 Points",font='arial 8 bold',command=tracer_droite_reg_sur_graphe_100)
    Tracer.add_separator()
    Tracer.add_command(label="5. Charger fichier ",font='arial 8 bold',     command=charger_fichier)  
    Tracer.add_command(label="6. Quitter ",font='arial 8 bold',             command=quitter)  
    Tracer.add_separator()
    mon_menu.add_cascade(label="Tracer", menu=Tracer)   

    
    fenetre.mainloop()
####

####   


# Fenetre principale (main_win)

main_Win = Tk()
main_Win.title("Amine-Belkhichane-22207880") 
main_Win.configure(bg="gray11")

# Widgets main_win main_win
    
frame_labelmain=Frame(main_Win)
Label1=Label(frame_labelmain,pady=50,text="Tracer des lignes",font='Garamond 15 bold',fg='ivory',bg='gray11')
Label2=Label(frame_labelmain,pady=10,text="Cliquez sur les boutons en bas pour lancer une des parties souhaitées.",font='Arial 10 bold',fg='yellow',bg='gray11')

frame_button=Frame(main_Win) 
btn1=Button(frame_button, text="Partie3_ABC",padx=220,font='Garamond 15 bold',fg='white',bg='black',command=Partie3_ABC)
btn2=Button(frame_button, text="Partie3_D"  ,padx=225,font='Garamond 15 bold',fg='white',bg='black',command=Partie3_D)
btn3=Button(frame_button, text="Partie3_EFG",padx=250,font='Garamond 15 bold',fg='white',bg='black',command=Partie3_EFG)

# Emplacement Widgets main_win
    
frame_labelmain.pack(side=TOP)
Label1.pack(side=TOP,fill=X)                                       
Label2.pack(side=TOP,fill=X)
    

frame_button.pack(side=BOTTOM) 
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)


def open_win() :
    # main_Win.destroy()  
    main_Win.mainloop()
  






######################################################################

  ##################
    ##############
  # COMMAND CENTER #
    ##############
  ##################


# Partie3_ABC()
# Partie3_D()
# Partie3_EFG()
open_win()
