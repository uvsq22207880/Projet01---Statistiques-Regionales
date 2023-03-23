# l'url de dépôt du projet sur github:
https://github.com/uvsq22207880/Projet01---Statistiques-Regionales

# Groupe de TD : 
-S2BITD-02

# les étudiants du groupe : 
 - Amine Belkhichane 
 - Quentin Palmyre ?
 - Eva Bouala ?
 
# README : /utilisation du programme/
-apres avoir telechargé ou copié le programme v2.1.1:
- decommenter tout en bas dans le "command center" la partie a utiliser souhaité , dans notre cas on decommenteras "open_win()" (pour avoir accées a tout le programme) , apres avoir lancé le programme dans un debbugueur (pour l'instant) une fenetre ou il ya marqué deux labels "tracer des lignes" apparrait , choisir l'un des trois boutons pour lancer l'un des trois sous programmes respectivement partie3_ABC, Partie3_D, Partie3_EFG .

La partie ABC :  

Contient 12 widgets : 
- Le bouton Tracer la droite : trace une droite aleatoire (de differentes couleurs).
- Le bouton Afficher couleur : afficher la couleur utilisé.
- Le bouton Creer fichier : crée fichier de deux clones de nombres aleatoires (float).
- Le bouton Tracer points crée : permet de tracer les points du fichier crée (sur une fenetre matplotlib).
- Le bouton Regression : permet de tracer la droite de regression de ce meme fichier crée .
- Le bouton Charger fichier : permet de charger n'importe quel fichier.txt (un fichier texte) sur l'ordinateur.                   
- Le bouton Tracer nuage exemple : permet de tracer les points de ce fichier et sa droite de regression si cela est pertinent ).
- Le bouton effacer : pour effacer tout le contenue du canvas.
- Le bouton quitter : pour fermer la fenetre partie3_ABC.

- Mais aussi un menu qui repends toutes les fonctions de la fenetre

La Partie3_D : 

Contient 7 widgets :
- Le bouton mode dessin: permet de dessiner un nuage de points sur le canvas.
- Le bouton desactiver mode dessin :permet de désactiver la possibilité de dessiner.
- Le bouton autre couleur : permet de changer de coleur.
- Le bouton regression : permet de tracer la droite de regression "si c'est pertinent" en affichant le coefficient de correlation sinon il ne retourneras rien sauf le coefficient de correlation.
- Le bouton effacer : permet d'effacer tout ce qu'il y a sur le canvas.
- Le bouton quitter : permet de fermer la fenetre partie3_D.

- En haut a droite : un menu appelé dessin qui comporte les memes commandes que les boutons sauf pour : "5.Desactiver mode dessin" qui en plus grise le bouton mode dessin en plus de le desactiver  .    
              
Partie3_EFG : 

Contient 8 widgets :
- Le fichier present par defaut en dur est "villes_virgule.csv" dans cette partie .

- Pour l'entry: comme le label marqué sur le coté l'indique : il faut preciser le nombre de lignes a extraire du fichier chargé (villes_virgule.csv)pour nous.
- Le bouton charger fichier : permet de charger un nouveau fichier dans le programme.
- Les boutons "tracer 100 points" et "regression 100 points"; permettent respectivemnt de tracer un nuage de 100 points et de dire s'il est perinent de tracer leur droite de regression ou pas.
- Pareillement pour les boutons "tracer N points" et "regression N points" sauf que N est definis selon la valeur entré dans la case entry (est appliqué seulemnt apres avoir appuyé sur LE BOUTON SOUMMETRE "EN VERT" ).
- Apres avoir finis appuyez sur le bouton rouge "quitter" pour fermeer la fenetre partie3_EFG.


# Commandes necessaires pour git ;)

-Créer un nouveau référentiel: git init 

-Ajouter des fichiers à l'index: git add <fichier> 

-Commiter les changements à l'index : git commit -m "Message de commit"
 
-Pousser le référentiel sur un serveur distant: git push <serveur> <branche> 

-Récupérer les modifications du serveur distant : git pull <serveur> <branche> 

-Fusionner des branches locales ou distantes : git merge <branche1> <branche2> 

-Cloner un dépôt distant dans un nouveau référentiel local : git clone <url_du_dépôt_distant>

