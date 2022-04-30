# 10 mille

Jeu de dés 10 mille avec PyGame.

## Règle du jeu

### Principe

Le premier joueur qui atteint les 10 000 points gagne la partie.

### Points

 - :five: -> 50 points
 - :one: -> 100 points
 - :hash::hash::hash: -> #00 points
 - :one::one::one: -> 1 000 points
 - :one::two::three::four::five: -> 1 000 points
 - :two::three::four::five::six: -> 1 000 points

### Déroulement de la partie

Tous les joueurs commence avec un score global de 0 points.

Chaque joueur joue à tour de rôle et un joueur peut lancer les dès tant qu'il 
marque des points à chaque lancé.

Une manche commence avec 5 dés. Après un lancé, le joueur peut décider des points 
qu'il conserve en mettant les dés sur le côté : 
ces dés ne peuvent plus être joués.
Il est obligatoire de mettre des points de côté pour relancer les dés restants.
Ces dés (seul ou en combinaison), mis de côté, doivent nécessairement rapporter 
des points : les dés qui ne rapportent pas de points ne peuvent être mis de côté.
Si tous les dés ont été mis de côté, alors les 5 dés peuvent être relancés par le 
joueur.

La manche du joueur s'arrête dès lors :
 - qu'il ne marque pas de points sur un lancer, il ne marque pas de points 
 sur cette manche et passe la main,
 - qu'il marque des points sur un lancer et qu'il décide de s'arrêter, tous les 
 points de la manche sont comptabilisés pour le score global du joueur.

Les combinaisons ne sont valides que sur un même lancé. Il n'est pas possible de 
créer une combinaison sur plusieurs lancés.

Le joueur peut arrêter la manche quant il le souhaite (du moment que son dernier 
lancé marque des points) sauf lorsque son score global est de 0. Il ne peut 
s'arrêter seulement lorsque la somme des points mis de côtés lors de la manche
 est égale ou supérieure à 1 000.