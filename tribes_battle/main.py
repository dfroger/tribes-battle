import arcade
from dataclasses import dataclass
import imgui
from arcade_imgui import ArcadeRenderer

from . import units as u
from .constant import *


class Tile:
    """
       y j

    3*DY   ┌────────┬───────┬───────┐
           │        │       │       │
         2 │        │       │       │
           │        │       │       │
    3*DY   ├────────NW──────NE──────┤
           │        │       │       │
         1 │        │   M   │       │
           │        │       │       │
      DY   ├────────SW──────SE──────┤
           │        │       │       │
         0 │        │       │       │
           │        │       │       │
       0   └────────┴───────┴───────┘
                0       1       2         i
           0        DX      2*DX    3*DX  x
    """

    i: int
    j: int

    w: int
    e: int
    x: int

    s: int
    n: int
    y: int

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        self.compute_x()
        self.compute_y()

    @classmethod
    def from_pixel(cls, x: int, y: int) -> "Tile":
        i = x // c.DX
        j = y // c.DY
        return cls(i, j)

    def compute_x(self):
        self.w = self.i * c.DX
        self.e = (self.i + 1) * c.DX
        self.x = (self.w + self.e) // 2

    def compute_y(self):
        self.s = self.j * c.DY
        self.n = (self.j + 1) * c.DY
        self.y = (self.s + self.n) // 2

    def __str__(self):
        return f"Tile({self.i},{self.j})"

    def __eq__(self, other) -> bool:
        return self.i == other.i and self.j == other.j


Paris = Tile(5, 5)
Londres = Tile(27, 13)

Units = []


class TribesBattle(arcade.Window):

    def __init__(self):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
        self.tile_map = None
        self.frame_count = 0
        self.selected_city = "Paris"
        imgui.create_context()
        self.renderer = ArcadeRenderer(self)

    def setup(self):
        layer_options = {"Terrain": {"use_spatial_hash": True}}
        self.tile_map = arcade.load_tilemap("map.json", c.TILE_SCALING, layer_options)
        self.warrior = u.WARRIOR

        self.warrior.center_x = 1.5 * c.DX
        self.warrior.center_y = 3.5 * c.DY

        self.paris = arcade.Sprite(
            "sprites/cities.png",
            scale=c.SPRITE_SCALING,
            image_x=0 * c.DX,
            image_y=7 * c.DY,
            image_width=c.DX,
            image_height=c.DY,
        )
        self.paris.center_x = Paris.x
        self.paris.center_y = Paris.y

        self.londres = arcade.Sprite(
            "sprites/cities.png",
            scale=c.SPRITE_SCALING,
            image_x=0 * c.DX,
            image_y=7 * c.DY,
            image_width=c.DX,
            image_height=c.DY,
        )
        self.londres.center_x = Londres.x
        self.londres.center_y = Londres.y

        self.prod = 1

        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene.add_sprite("warrior", self.warrior)
        self.scene.add_sprite("paris", self.paris)
        self.scene.add_sprite("londres", self.londres)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP:
            self.warrior.center_y += 30
        elif key == arcade.key.DOWN:
            self.warrior.center_y += -30
        elif key == arcade.key.LEFT:
            self.warrior.center_x += -30
        elif key == arcade.key.RIGHT:
            self.warrior.center_x += 30

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        tile = Tile.from_pixel(x, y)
        if tile == Paris:
            self.selected_city = "Paris"
        elif tile == Londres:
            self.selected_city = "Londres"

    def on_update(self, delta_time):
        """Movement and game logic"""
        self.frame_count += 1

    def on_draw(self):
        self.clear()
        self.scene.draw()

        arcade.draw_text(
            "Paris",
            Paris.x,
            Paris.y - c.DY,
            arcade.color.BLUE,
            c.CITY_FONT_SIZE,
            anchor_x="center",
            anchor_y="bottom",
        )

        arcade.draw_text(
            "Londres",
            Londres.x,
            Londres.y - c.DY,
            arcade.color.ORANGE,
            c.CITY_FONT_SIZE,
            anchor_x="center",
            anchor_y="bottom",
        )

        imgui.new_frame()
        imgui.begin("Ville")
        imgui.text(self.selected_city)
        clicked, current = imgui.listbox(
            "Production", self.prod, ["Guerrier", "Colon", "Lanceur de pierre"]
        )
        if clicked:
            self.prod = current
            print(self.prod)

        imgui.end()

        imgui.render()
        self.renderer.render(imgui.get_draw_data())


def main():
    window = TribesBattle()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
