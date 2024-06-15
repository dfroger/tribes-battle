import arcade

from . import constant as c


class Units: ...


class MeleeUnit: ...


class DistanceUnit: ...


class CivilUnit: ...


WARRIOR = arcade.Sprite(
    "sprites/units.png",
    scale=c.SPRITE_SCALING,
    image_x=18 * c.DX,
    image_y=0 * c.DY,
    image_width=c.DX,
    image_height=c.DY,
)


"""
caractéristique:
- attaque
- défense
- vitesse

"""

"""
resources:
- pierre
- bois
- bronze
- fer
- acier
"""

"""
3 compétances guerrière:
- combat à l'épee
- combat à la hache
- combat à la lancer
- cavalerie
- agilité

3 compétances civiles:
- forgeron
- travail du bois
- travail de la pierre
- paysan
"""

"""
hache: plus fort contre les boucliers/épée
épée : plus fort contre les lances


arme (main droite)
- gourdin
- hache de pierre
- hache de bronze
- hache de fer
- épée de pierre
- épée de bronze
- épée de fer
- épée de acier
- lance en bois
- lance en bronze
- lance en acier
- lance en fer
- lance amélioration: double pointe: plus fort sur unité de mélée

bouclier (main gauche)
- bouclier rond: faible sur attaque à distance
- bouclier rectange: fort sur attaque à distance, diminue mouvement, pas pour cavalier
- bois
- bronze
- fer
- acier

casque
- bois
- bronze
- fer
- acier

chausse

cuirasse

special 1

special 2
"""
