![Age of War](https://moodle.supinfo.com/pluginfile.php/8294/mod_assign/intro/image.png)

## 1 - Introduction

Anblisoft, le premier éditeur de jeux vidéo au monde, cherche à acquérir un studio de développement ou à intégrer une équipe capable de leur fournir un jeu Age of War pour diversifier leur portefeuille de jeux.

Votre équipe est en compétition avec plusieurs autres sous-traitants pour le développement, et le meilleur projet remportera le contrat. L'objectif principal de ce projet est de fournir une première version stable et vendable qui respecte les spécifications définies.

Vous êtes libre d'utiliser n'importe quel langage et technologie. Il vous est évidemment interdit de copier ou d'adapter un code existant. Vous n'êtes pas autorisé à utiliser une application de création de jeux sans code ou un éditeur de cartes de jeu (de plus, les outils de type blueprint doivent être très restreints).

Ce projet comprend 2 spécifications, vous ferez un choix entre ces 2 sujets/échelles et répondrez aux attentes de celui choisi :

- Le sujet orienté développement
- Le sujet orienté game-design

Le non-respect des instructions ci-dessus ou des règles de livraison se traduira par une note de 0.

## 2 - Présentation

Age of War est un mélange entre un jeu de défense et un jeu de stratégie. L'objectif est de détruire la base ennemie tout en défendant la vôtre. Vous pouvez construire des tourelles pour défendre votre base et des unités pour attaquer celle de l'ennemi. La particularité du jeu est que vous pouvez évoluer et débloquer de nouvelles unités et moyens de défense. Plus vous évoluez, plus vous deviendrez puissant.

### 2.1 - Unités

Produisez des unités à envoyer vers la base ennemie en attaquant tout sur le chemin. Vous êtes limité à 10 unités simultanément. La production d'unités prend du temps, et une file d'attente peut être créée.
Il existe 4 types d'unités : Infanterie, Support, Anti-Blindage, Lourd. Chacun est plus ou moins efficace contre un type particulier.
Elles ont différentes caractéristiques : Prix, PV, Dégâts, Vitesse de tir, Temps de construction, Type, Vitesse de déplacement et Portée.
Tuer une unité ennemie rapporte de l'or et de l'expérience.

### 2.2 - Tourelles

Vous pouvez construire jusqu'à 4 tourelles sur votre base pour vous défendre, chaque emplacement coûtant de l'argent pour être débloqué.
Elles ont différentes caractéristiques : Prix, Dégâts, Vitesse de tir et Portée. Vendre une tourelle ne rapporte que 50% de l'or dépensé.

### 2.3 - Spéciales

Utilisez de l'expérience pour évoluer vers le prochain Âge (il y en a 6 différents).
Vous pouvez également dépenser de l'expérience pour utiliser un pouvoir qui frappera aléatoirement des unités sur le terrain (plus l'Âge est avancé, plus les dégâts et la précision/saisie sont importants). Ce pouvoir a un temps de recharge.

### 2.4 - Améliorations

Vous pouvez améliorer un certain type d'unité pour le rendre plus puissant et avoir l'avantage dans le combat.
Il y a une amélioration qui débloque un type d'unité initialement verrouillé à chaque Âge (Lourd). Il doit être déverrouillé à chaque Âge pour invoquer l'unité correspondante.
Les autres améliorations sont définitives, mais chaque niveau coûte de plus en plus cher. Il en existe différentes : Dégâts de l'infanterie, Dégâts du support, Dégâts anti-blindage, Dégâts lourds, Dégâts de la tourelle, Portée du support, Portée de la tourelle, PV de l'infanterie, PV anti-blindage, PV lourd, Or par élimination.

### 2.4 - Évolution

Évoluer vers le prochain Âge nécessite un certain nombre de points d'expérience. Une fois débloqué par un joueur, l'arrière-plan du jeu change. Le joueur qui évolue débloque de nouvelles unités, tours et spéciales, augmente les points de vie de la base et obtient un nouveau design de base.

### 2.5 - Considérations

Le joueur gagne si la base ennemie tombe à 0 PV. Les unités de support ont toujours une portée (et tirent en marchant). Dans le dernier Âge, une unité ultime est disponible.
Les différents Âges sont : Homme des Cavernes, Spartiate, Égyptien, Médiéval, Renaissance, Moderne et Futuriste. Vous êtes libre de choisir votre univers et vos Âges tant qu'ils sont cohérents et appropriés.
Voici un exemple jouable : [Age of War 2 - Jouer maintenant](https://www.gameflare.com/online-game/age-of-war-2).

Voici une bande-annonce et un déroulement du jeu :

[![Bande-annonce](https://img.youtube.com/vi/fVgJBKhW-cE/0.jpg)](https://www.youtube.com/watch?v=fVgJBKhW-cE)

[![Déroulement](https://img.youtube.com/vi/S2RMa7loMt4/0.jpg)](https://www.youtube.com/watch?v=S2RMa7loMt4)

Source : [MaxGames - Guide Age of War 2](https://www.maxgames.com/guides/age-of-war-2.html)

## 3 - Expression fonctionnelle

### 3.1 - Généralités

Vous implémenterez le jeu tel que spécifié dans la section précédente. La qualité graphique, l'environnement visuel et sonore, la jouabilité et l'équilibrage du jeu seront essentiels.

### 3.2 - IA et Mode Local

Vous créerez un mode de jeu local avec 4 niveaux de difficulté. Vos IA feront certainement de meilleurs choix de gameplay, mais seront également aidées par une augmentation des dégâts et des PV, ainsi que par plus d'or et d'expérience gagnés.
En mode local, il sera possible d'augmenter la vitesse du jeu.

### 3.3 - Internationalisation

Pour répondre aux besoins du marché, votre jeu sera disponible dans au moins

 5 langues.

Vous choisirez l'un des 2 sujets suivants :

## 4 - [Sujet 1] Spécifications de développement

### 4.1 - Limites

Le choix de ce sujet vous limitera dans les technologies : vous ne pourrez pas utiliser de moteur de jeu tel que Unity ou Unreal Engine. Vous pouvez proposer un jeu pouvant être joué via un exécutable ou sur un navigateur Web.

### 4.2 - Multijoueur

Deux joueurs sur le même réseau pourront concourir l'un contre l'autre.

## 4 - [Sujet 2] Spécifications de game-design

### 4.1 - Limites

Vous êtes libre d'utiliser n'importe quel moteur de jeu tel que Unity ou Unreal Engine. Vous pouvez proposer un jeu pouvant être joué via un exécutable ou sur un navigateur Web.

### 4.2 - Multijoueur

Il ne s'agit pas d'être connecté au même réseau et d'héberger un jeu sur l'ordinateur d'un joueur, mais de profiter d'un jeu entièrement en ligne. Les joueurs peuvent créer un compte en ligne pour jouer avec des joueurs du monde entier ; ils ont une liste d'amis pour échanger des messages instantanés et les inviter à des jeux. Il est également possible de rechercher des adversaires via un système de matchmaking avec un système de notation Elo. Les joueurs ont un profil avec des statistiques et la possibilité de personnaliser la photo de profil en fonction du nombre de jeux et de victoires. Les joueurs dans le jeu peuvent s'échanger des messages instantanés entre eux.

## 5 - Livraison

Votre rendu sera un fichier ZIP contenant vos codes sources, des fichiers supplémentaires (sons, images, etc.), une documentation utilisateur et une documentation technique expliquant vos choix et/ou détails de mise en œuvre.

La documentation utilisateur est un manuel de jeu, destiné à tout utilisateur, et explique comment jouer. Un utilisateur doit avoir toutes les informations pour lancer le jeu et comprendre tous ses détails, règles, modes, etc.

La documentation technique est destinée aux professionnels du domaine et devrait décrire en profondeur les choix et les mises en œuvre. Elle contiendra au moins les éléments suivants :

- Justification du choix du langage de programmation et de la bibliothèque graphique.
- Description des structures de données.
- Comportement des IA.
- Gestion physique.
- Choix de game design (statistiques, types d'unités/tourelles, prix, etc.).
- Explication des processus utilisés pour gérer les jeux multijoueurs.
- etc.

Votre rendu doit contenir un exécutable, un installeur ou un lien pour lancer facilement le jeu pour un utilisateur normal, sur plusieurs architectures. Tout rendu nécessitant une installation lourde de logiciels supplémentaires ou une manipulation avancée de l'utilisateur sera considéré comme inadéquat. Un jeu qui met en œuvre des fonctionnalités disparates sans créer un jeu fonctionnel ne sera pas non plus considéré comme un rendu valide.

## 6 - Échelle de notation

[Détails de l'échelle de notation pour le Sujet 1 et le Sujet 2]
