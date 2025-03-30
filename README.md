## Projet des Coding Weeks 2022/2023 des Sudistes

## L'équipe des Sudistes : 

Manon ARFIB, Louisa ARFIB, Juliette VEDRENNE, Cécile HUIN


## Description

Identifier pour une photo d'un momument donnée le monument auquel elle correspond parmi les 23 sur lesquels le modèle a été entraîné.


## Installation 

1) Créer un dossier .vscode/settings.json en suivant les étapes ci-dessous : 
- ctr + P (Windows) ou cmd + P (macOs)
- taper >Settings dans la barre de recherche qui vient de s'afficher
- puis sélectionner Workspace settings (JSON)
- compléter :

 {"terminal.integrated.env.osx" : {
    "PYTHONPATH" : <chemin absolu vers réperoire landmark_recognition>
}
}

/!\ sur windows, remplacer les \ par des /

2) Créer un environnement virtuel. Pour ne pas push cet environnement, le nom choisi dans .gitignore
est virtual_env_cw. (Aide pour créer l'environnement dans help_virtual_environnement)

3) Installer les packages du fichier requirements.txt avec la commande pip -r requirements.txt
(remarque : os est une librairie standard de python)

4) Se placer à la racine (landmark_recognition) à chaque fois qu'on lance une fonction car les chemins 
sont définis de manière absolue.

5) Lancer le modèle et l'entraîner en lançant la fonction src/create_model.py

## Pour tester l'algorithme de reconnaissance des bâtiments

# dans VS Code

1) Pour tester sur des images :
Les placer dans le dossier data/data_to_test 
Lancer main.py

2) Appuyer sur une touche quelconque du clavier pour faire défiler les images et leur descrition.

Remarque : les images qui sont testées sont celles du fichier data/data_test

Deux photos de bâtiments que l'algorithme ne doit pas reconnaître : 
le Puy-en-Velay et le lycée Masséna (à Nice)

Six photos de monuments que l'algorithme doit reconnaître : 
Une photo de la major, de la promenade des anglais, du pont d'Avignon et du pavillon noir et dux photos 
du théâtre antique d'Orange

# sur l'application Web

1) Lancer le fichier app.py
Attendre que * Debugger PIN: 418-333-113 s'affiche

2) Aller sur ton moteur de recherche préféré 

3) Taper dans la barre de recherche "localhost:5000"
On arrive sur la page d'accueil du projet.

4) Cliquer sur l'onglet Landmark Recognition

5) Rentrer le chemin du dossier contenant les images à reconnaître (ne doit pas être dans le dossier landmark_recognition). (Accéder au chemin en faisant clic droit > propriétés)

6) Cliquer sur Submit, les images s'affichent avec le nom du monument correspondant.

### Démarche à suivre pour enrichir la base de données avec un nouveau bâtiment

1) Importer les photos dans un dossier data/dataset/ville/monument à partir de GoogleImages via 
le code javascript et le module download_images.py du dossier download_images 
/!\ Ajouter au moins 25 photos.

2) Lancer le traitement des photos (modification de la taille en 224x224) en lançant le module 
src/database_creation/creation_dataset_224.py

3) Dans src/utils/dico.py, modifier la fonction create_dico_cities_landmarks : ajouter dans l'ordre alphabétique (ville puis monument) : "ville, monument"
Remarque : pour vérifier que l'ordre est correct, lancer create_dico : l'ordre doit être le même, les seules différences sont les espaces et les majuscules.

4) Ajouter la description du monument sous fichier texte dans data/text_files

5) Créer un nouveau modèle et l'entraîner : lancer src/create_model.py (en ayant supprimé l'ancien dossier 
model_updated_model)

6) Eventuellement tester la reconnaissance du nouveau bâtiment avec src/check_new_model.py

7) Lancer la fonction main.py


## License

MIT License

Copyright (c) 2022, Les Sudistes, CodingWeeks CentraleSupélec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

