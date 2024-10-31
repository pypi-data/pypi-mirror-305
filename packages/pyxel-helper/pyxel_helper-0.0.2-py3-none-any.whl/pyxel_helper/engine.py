import pyxel
from pyxel_helper.sprites import Sprite, Animated_sprite
from pyxel_helper.collision import Hitbox
from pyxel_helper.positioning import Vector2
from pyxel_helper.character_body import Character_body

class Game:
    """The full game, holds all game objects and manages pyxel stuff"""
    def __init__(self, dimensions: Vector2, pyxres_path: str, title: str, bg_col: int, fps: int = 60):
        self.res_path = pyxres_path
        self.title = title
        self.dimensions = dimensions
        self.bg_col = bg_col
        self.fps = fps
        self.bodies: list[Character_body] = []
        self.sprites: list[Sprite] = []
        self.animated_sprites: list[Animated_sprite] = []
        self.frozen = False
        pyxel.init(self.dimensions.x, self.dimensions.y, self.title, fps=self.fps)
        pyxel.load(self.res_path)
    
    def start(self):
        """Runs the game"""
        pyxel.run(self.update, self.draw)
    
    def add_object(self, object):
        """Adds a gameObject to the game"""
        if type(object) == Animated_sprite:
            object.game_fps = self.fps
            self.animated_sprites.append(object)
        
        elif type(object) == Sprite: 
            self.sprites.append(object)

        elif type(object) == Character_body:
            object.game_fps = self.fps
            if type(object.sprite) == Animated_sprite:
                self.add_object(object.sprite)
            else:
                self.add_object(object.sprite)
            self.bodies.append(object)

    def draw(self):
        """Main draw function, gets run every frame"""
        toDraw = self.sprites + self.animated_sprites
        toDraw.sort(key=lambda x: x.z_position)
        [i.draw() for i in toDraw]

    def update(self):
        pyxel.cls(self.bg_col)
        if not self.frozen:
            [i.update() for i in self.animated_sprites]
        [i.update(self.frozen) for i in self.bodies]