# Auteur : VIDAL Antoine
# Nom du projet : Dagu - Voiture autonome

# Ce fichier liste les constantes utilisées pour la détection de panneau ainsi que les états du véhicule.

from enum import Enum

# Liste des panneaux que le Dagu peut détecter

class signs(Enum):
  GN_DEFAULT = 0
  GN_STOP = 1
  GN_SPEED_50 = 2
  GN_YIELD = 3
  GN_FORBIDDEN = 4
  GN_DANGER = 5


# Listes des états dans lequel le Dagu peut se retrouver
# Chaque état est représenté sous une chaîne de caractères.

GW_IDLE = 'Idle'
GW_STOPPED = 'Stopped'
GW_MOVING = 'Moving'
GW_WAITING = 'Waiting'