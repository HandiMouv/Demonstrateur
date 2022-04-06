# Demonstrateur
## Table des matières
- [Présentation](#pres)
- [Initialisation](#init)
- [Utilisation](#usage)
- [Documentation](#docu)
- [Auteur](#auteur)

## <a name="pres"/> Présentation
Ce programme représente notre démonstrateur. Il s'agit d'un serveur de socket qui va recevoir les ordres envoyés par la Raspberry et faire mouvoir le curseur de la souris de l'ordinateur.<br>
Les commandes données ci-dessous sont à executer sous linux ou un git bash.
## <a name="init" /> Initialisation
1) Téléchargez le repo sur votre ordinateur, la destination n'a pas d'importance.<br>
```bash
git clone https://github.com/HandiMouv/Demonstrateur
```
2) Installez python3-venv<br>
```bash
sudo apt-get install -y python3-venv
```
3) Placez vous dans le repo téléchargé.<br>
```bash
cd Demonstrateur
```
4) Préparation de l'environnement python.<br>
```bash
python3 -m venv env #creation de l environnement virtuel python
source ./env/bin/activate #active l environnement virtuel
pip install -r requirements.txt #installation des dependances
```

5) Sortir de l'environnement virtuel si vous souhaitez.
```bash
deactivate
```

Apres cette manipulation, le projet est prêt à etre éxécuté.

## <a name="usage"/> Utilisation
1) Placez vous dans le repo téléchargé.<br>
```bash
cd Demonstrateur
```
2) Activer l'environnement virtuel pour que le programme ait accès aux dépendances.
```bash
source ./env/bin/activate #active l environnement virtuel
```
4) Lancez le serveur qui qui va réceptionner les ordres sous forme de sockets.<br>
```bash
python3 MASTER_SERVER.py
```
Le serveur est donc à l'écoute et va recevoir les ordres et mouvoir le curseur de la souris.<br>

5) Sortir de l'environnement virtuel si vous souhaitez une fois que le serveur ne tourne plus.
```bash
deactivate
```
## <a name="docu"/> Documentation
**Comment le programme réceptionne les sockets ?**<br>
-> [Connexions de la Raspberry PI](https://github.com/HandiMouv/Presentation-Generale/blob/main/DOCUMENTATION/Connexions%20du%20Raspberry%20PI%20.pdf)

## <a name="auteur"/> Auteur
Charles SAISON<br>
Henri PETRELLI
