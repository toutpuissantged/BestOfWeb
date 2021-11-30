
# BESTOFWEB

## What's this ?

bestofweb is software that allows you to quickly find
the best free streaming sites for series, movies, torrents,
manga, and others ...

## Installation

no installation needed
you just need to have python 3.x install
and to do

## Usage for windows users

![alt text](doc\image\Capture2.PNG)
allez sur le githb officiel du projet et
telecharger la derniere  version compiler du project [en suivant cet liens](https://github.com/toutpuissantged/BestOfWeb/tags)
![alt text](doc\image\Capture3.PNG)
decompresser le fichier .zip
![alt text](doc\image\Capture5.PNG)
![alt text](doc\image\Capture6.PNG)
puis lancer l'executable .exe et suivre les instructions
![alt text](doc\image\Capture7.PNG)
![alt text](doc\image\Capture8.jpeg)

## Usage for developers without nodejs

installer python 3.x
puis cloner le projet sur github apres avoir installer git en local

``` bash
gitclone https://github.com/toutpuissantged/BestOfWeb.git

```

acceder au repertoire du projet

``` bash
cd BOW

```

installer les dependances avec pip

``` bash
pip install -r requirements.txt

```

lancer le script

``` bash
python main.py

```

cette procedure est destiner au developeurs souhaitant tester rapidement le project , pour installer les usage de tests integrales veillez voir le chapitre suivant 

## usage for developers with nodejs

installer nodejs
installer python 3.x
puis cloner le projet sur github apres avoir installer git en local

``` bash
gitclone https://github.com/toutpuissantged/BestOfWeb.git

```

acceder au repertoire du projet

``` bash
cd BOW

```

installer les dependances avec pip

``` bash
pip install -r requirements.txt

```

installer les dependances npm

``` bash
npm install

```

pour lancer le developement avec du rechargement automatique

``` bash
npm run dev

```

pour lancer les tests unitaires

``` bash
npm run test

```

pour lancer la compilation du projet

``` bash
npm run build

```

## Contribution

pour contribuer au projet , vous pouvez suivre les instructions suivantes

forker le projet sur github

creer une branche pour votre contribution
faite vos modifications sur votre branche
une fois les commits creer un pull request et attendre la validation de l'administrateur

### attention

- les messages commits doivent etre explicites et en anglais pour eviter les confusions
- les tests untaire et dintegration doivent etre valider  par le serveur d'integration continue 
- ecrire des tests pour chaque fonctionnalite implementer
- suivre les regle du code et respecter les standards

## License

[MIT] (https://choosealicense.com/licenses/mit/)
