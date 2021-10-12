# Projet django
## Installation setup 
## Sources utilisées

### Login 
Pour comprendre la logique de la connexion Built-in de Django, j'ai utilisé ces tutoriaux :

- [Login system simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html)
- [MDN](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication)

### Blog
[Blog](https://tutorial.djangogirls.org/fr/)

### Chat
J'ai voulu en profiter pour en apprendre plus sur les websockets et sur l'encapsulation. pour cela, j'ai suivi ce tutoriel :
- [Tutorial Part 2: Implement a Chat Server
](https://channels.readthedocs.io/en/stable/tutorial/part_1.html)
- Il faut donc monter une image comme il est expliqué dans la partie 2
```bash
docker run -p 6379:6379 -d redis:5
```
J'ai essayé d'extraire mon image, pour que ça soit plus simple, mais je ne suis pas sûr que cela ait fonctionné. 
J'ai partagé mon image dans le mail : C'est le fichier `Desktop02fee89f17ad.tar`
De ce que j'ai compris, pour la monter, il faut faire cette commande : 
```bash
docker load -i <path-to-image>Desktop02fee89f17ad.tar
```
en l'occurance, si on souhaite la monter depuis le projet :
# Etape 1:
Ne pas toucher de son emplacement
# Etape 2:
Ouvrir un terminal dans le projet, à la racine de celui ci
```bash
docker load -i <path-to-where-my-project-is-installed>/timogo/Desktop02fee89f17ad.tar
```

