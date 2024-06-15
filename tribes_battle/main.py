import arcade
from dataclasses import dataclass
import imgui
from arcade_imgui import ArcadeRenderer

from . import constant as c
from .tile import Tile
from . import unit as u
from .unit import Unit


Paris = Tile(5, 5)
Londres = Tile(27, 13)

UNITS = [
    Unit(title="warior", sprite=u.WARRIOR, tile=Tile(6, 6)),
    Unit(title="worker", sprite=u.WORKER, tile=Tile(6, 5)),
]


def find_units(tile: Tile) -> list[Unit]:
    return [u for u in UNITS if u.tile == tile]


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
        self.scene.add_sprite_list("Units")
        for unit in UNITS:
            self.scene.add_sprite("Units", unit.sprite)

        self.scene.add_sprite("paris", self.paris)
        self.scene.add_sprite("londres", self.londres)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        warrior = UNITS[0]

        if key == arcade.key.UP:
            warrior.move_up()
        elif key == arcade.key.DOWN:
            warrior.move_down()
        elif key == arcade.key.LEFT:
            warrior.move_left()
        elif key == arcade.key.RIGHT:
            warrior.move_right()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        tile = Tile.from_pixel(x, y)
        units = find_units(tile)
        print(units)

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
