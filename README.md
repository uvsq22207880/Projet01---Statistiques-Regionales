# README :

# L'url de dépôt du projet sur GitHub :

- https://github.com/uvsq22207880/Projet01---Statistiques-Régionales

# Groupe de TD :

- S2BITD-02

# Les étudiants du groupe :

 - Amine Belkhichane 
 - Quentin Palmyre ?
 - Eva Bouala ?
 
# Utilisation du programme :

- Après avoir téléchargé ou copié le programme v2.1.1 et ouvert dans Visual Studio Code :
- Décommenter tout en bas dans le "command center" (la partie à utiliser souhaitée), dans notre cas on décommentera "open_win()" pour avoir accès à la fenetre mère du programme). Après avoir lancé le programme dans un débugueur une fenêtre où il y a marqué deux labels ; "Tracer des lignes" et "Cliquez ci-dessous pour lancer chacune des parties souhaitées. "  , choisir l'un des trois boutons pour lancer l'un des trois sous-programmes respectivement :

  - Partie3_ABC.
  - Partie3_D.
  - Partie3_EFG.

- Pour les lancer appuyez sur leurs boutons respectifs. 


# # La partie ABC :  

Contient 12 widgets : 
- Le bouton Tracer la droite : trace une droite aléatoire (de différentes couleurs).
 - Le bouton Afficher couleur : afficher la couleur utilisée.
- Le bouton Créer fichier : crée fichier de deux clones de nombres aléatoires (float).
 - Le bouton Tracer points crée : permet de tracer les points du fichier crée (sur une fenêtre matplotlib).
- Le bouton Régression : permet de tracer la droite de régression de ce même fichier crée .
 - Le bouton Charger fichier : permet de charger n'importe quel fichier.txt (un fichier texte) sur l'ordinateur.                   
- Le bouton Tracer nuage exemple : permet de tracer les points de ce fichier et sa droite de régression si cela est pertinent).
 - Le bouton effacer : pour effacer tout le contenue du Canvas.
- Le bouton quitter : pour fermer la fenêtre partie3_ABC.

- Mais aussi un menu qui repends toutes les fonctions de la fenêtre.

# # La Partie3_D : 

Contient 7 widgets :
- Le bouton mode dessin : permet de dessiner un nuage de points sur le Canvas.
 - Le bouton désactiver mode dessin : permet de désactiver la possibilité de dessiner.
- Le bouton autre couleur : permet de changer de couleur.
 - Le bouton régression : permet de tracer la droite de régression "si c'est pertinent" en affichant le coefficient de corrélation sinon il ne retournera rien sauf le coefficient de corrélation.
 - Le bouton effacer : permet d'effacer tout ce qu'il y a sur le Canvas.
- Le bouton quitter : permet de fermer la fenêtre partie3_D.
 - En haut à droite de la fenetre Partie3_D : un menu appelé dessin qui comporte les mêmes commandes que les boutons sauf pour : "5.Desactiver mode dessin" qui en plus grise le bouton mode dessin en plus de le désactiver  .    
              
# # Partie3_EFG : 

Contient 8 widgets :
- Le fichier présent par défaut en dur est "villes_virgule.csv" dans cette partie .

- Pour l’entry : comme le label marqué sur le côté l'indique : il faut préciser le nombre de lignes a extraire du fichier chargé (villes_virgule.csv) pour nous.
- Le bouton charger fichier : permet de charger un nouveau fichier dans le programme.
- Les boutons "tracer 100 points" et "régression 100 points"; permettent respectivement de tracer un nuage de 100 points et de dire s'il est pertinent de tracer leur droite de régression ou pas.
- Pareillement pour les boutons "tracer N points" et "régression N points" sauf que N est définis selon la valeur entré dans la case entry (est appliqué seulement après avoir appuyé sur LE BOUTON SOUMMETRE "EN VERT" ).
- Apres avoir finis appuyez sur le bouton rouge "Quitter" pour fermer la fenêtre partie3_EFG.


# Commandes utiles pour git-bash ;)

- Créer un nouveau référentiel : git init 
- Ajouter des fichiers à l’index : git add <fichier> 
- Commiter les changements à l'index : git commit -m "Message de commit"
- Pousser le référentiel sur un serveur distant : git push <serveur> <branche> 
- Récupérer les modifications du serveur distant : git pull <serveur> <branche> 
- Fusionner des branches locales ou distantes : git merge <branche1> <branche2> 
- Cloner un dépôt distant dans un nouveau référentiel local : git clone <url_du_dépôt_distant>
