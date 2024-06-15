import arcade

from .tile import Tile
from . import constant as c


class City:
    def __init__(self, title: str, sprite: arcade.Sprite, tile: Tile, color):
        self.title = title
        self.sprite = sprite
        self.sprite.center_x = tile.x
        self.sprite.center_y = tile.y
        self.tile = tile
        self.color = color

    def __str__(self):
        return f"City(tile={self.title}, i={self.tile.i}, j={self.tile.j})"

    def __repr__(self):
        return self.__str__()


def city_sprite():
    return arcade.Sprite(
        "sprites/cities.png",
        scale=c.SPRITE_SCALING,
        image_x=0 * c.DX,
        image_y=7 * c.DY,
        image_width=c.DX,
        image_height=c.DY,
    )
