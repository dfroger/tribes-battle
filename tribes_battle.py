import arcade
import imgui
from arcade_imgui import ArcadeRenderer

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Tribes battle"
CITY_FONT_SIZE = 15

TILE_SCALING = 1
CHARACTER_SCALING = 1

# sprites/ files
dx = 30
dy = 30


class TribesBattle(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.tile_map = None
        self.frame_count = 0
        imgui.create_context()
        self.renderer = ArcadeRenderer(self)

    def setup(self):
        layer_options = {"Terrain": {"use_spatial_hash": True}}
        self.tile_map = arcade.load_tilemap("map.json", TILE_SCALING, layer_options)
        self.warrior = arcade.Sprite(
            "sprites/units.png",
            scale=CHARACTER_SCALING,
            image_x=18 * dx,
            image_y=0 * dy,
            image_width=dx,
            image_height=dy,
        )
        self.warrior.center_x = 1.5 * dx
        self.warrior.center_y = 3.5 * dy

        self.city = arcade.Sprite(
            "sprites/cities.png",
            scale=CHARACTER_SCALING,
            image_x=0 * dx,
            image_y=7 * dy,
            image_width=dx,
            image_height=dy,
        )
        self.city.center_x = 5.5 * dx
        self.city.center_y = 5.5 * dy

        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene.add_sprite("warrior", self.warrior)
        self.scene.add_sprite("city", self.city)

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

    def on_update(self, delta_time):
        """Movement and game logic"""
        self.frame_count += 1

    def on_draw(self):
        self.clear()
        self.scene.draw()

        arcade.draw_text(
            "Paris",
            5.5 * dx,
            4.5 * dy,
            arcade.color.BLACK,
            CITY_FONT_SIZE,
            anchor_x="center",
            anchor_y="bottom",
        )

        imgui.new_frame()
        imgui.begin("Example: simple text")
        imgui.text("Simple text")
        imgui.end()
        imgui.render()
        self.renderer.render(imgui.get_draw_data())


def main():
    window = TribesBattle()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
