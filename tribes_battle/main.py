import arcade
from dataclasses import dataclass
import imgui
from arcade_imgui import ArcadeRenderer

from . import city as t
from . import constant as c
from . import unit as u
from .city import City
from .tile import Tile
from .unit import Unit


UNITS = [
    Unit(title="warior", sprite=u.WARRIOR, tile=Tile(6, 6)),
    Unit(title="worker", sprite=u.WORKER, tile=Tile(6, 5)),
]

CITIES = [
    City(
        title="Paris", sprite=t.city_sprite(), tile=Tile(5, 5), color=arcade.color.BLUE
    ),
    City(
        title="Londes",
        sprite=t.city_sprite(),
        tile=Tile(27, 13),
        color=arcade.color.ORANGE,
    ),
]


def find_units(tile: Tile) -> list[Unit]:
    return [u for u in UNITS if u.tile == tile]


def find_city(tile: Tile) -> City | None:
    for city in CITIES:
        if city.tile == tile:
            return city
    return None


class UICities:
    def __init__(self):
        self.selected = "Paris"
        self.prod = 1

    def on_draw(self):
        imgui.new_frame()
        imgui.begin("Ville")
        imgui.text(self.selected)
        clicked, current = imgui.listbox(
            "Production", self.prod, ["Guerrier", "Colon", "Lanceur de pierre"]
        )
        if clicked:
            self.prod = current
            print(self.prod)
        imgui.end()


class UIUnits:
    def __init__(self):
        self.selected = ""


class TribesBattle(arcade.Window):

    def __init__(self):
        super().__init__(c.SCREEN_WIDTH, c.SCREEN_HEIGHT, c.SCREEN_TITLE)
        self.tile_map = None
        self.frame_count = 0
        imgui.create_context()
        self.renderer = ArcadeRenderer(self)

    def setup(self):
        layer_options = {"Terrain": {"use_spatial_hash": True}}
        self.tile_map = arcade.load_tilemap("map.json", c.TILE_SCALING, layer_options)

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # units
        self.scene.add_sprite_list("Units")
        for unit in UNITS:
            self.scene.add_sprite("Units", unit.sprite)

        # cities
        self.scene.add_sprite_list("Cities")
        for city in CITIES:
            self.scene.add_sprite("Cities", city.sprite)

        self.ui_cities = UICities()

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
        print("units:", units)

        city = find_city(tile)
        print("city:", city)
        if city is not None:
            self.ui_cities.selected = city.title

    def on_update(self, delta_time):
        """Movement and game logic"""
        self.frame_count += 1

    def on_draw(self):
        self.clear()
        self.scene.draw()

        for city in CITIES:
            arcade.draw_text(
                city.title,
                city.tile.x,
                city.tile.y - c.DY,
                city.color,
                c.CITY_FONT_SIZE,
                anchor_x="center",
                anchor_y="bottom",
            )

        self.ui_cities.on_draw()

        imgui.render()
        self.renderer.render(imgui.get_draw_data())


def main():
    window = TribesBattle()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
