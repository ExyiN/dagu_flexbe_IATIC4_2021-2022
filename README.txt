# ProjetIF
## Projet Interfilière IATIC - MT - SEE - SNPI 2021-2022 - Véhicule Autonome : Dagu
## Comportement Flexbe - Par Jacques Tea (IATIC 4)

### Installation
- Prérequis : Avoir ROS installé et le dossier YOLO
- Tuto d'installation de Flexbe : http://wiki.ros.org/flexbe

1. Dans le dossier `catkin_ws/src/`, cloner les dépôts git suivants :
- `git clone https://github.com/team-vigir/flexbe_behavior_engine.git`
- `git clone https://github.com/FlexBE/flexbe_app.git`

2. Mettre le dossier `dagu_behaviors` dans `catkin_ws/src/`
3. Revenir au dossier `catkin_ws` et faire `catkin_make`

### Informations
Ceci est le dossier comprenant le comportement Flexbe du Dagu. Il est spécifique à la structure des fichiers de la Jetson Nano, il faut donc faire des modifications pour l'exécuter sur un autre pc. Voir les fichier dans `catkin_ws/src/dagu_behaviors/dagu_flexbe_states/src/dagu_flexbe_states/` : il faut changer les chemins au début des fichiers pour s'adapter à votre machine et enlever les lignes relatives aux `pipes` et décommenter la génération aléatoire d'entiers dans l'état initial.
