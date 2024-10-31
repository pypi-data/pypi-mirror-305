from pyxel_helper.collision import Hitbox, MultiHitbox
from pyxel_helper.positioning import Vector2
from pyxel_helper.sprites import Sprite, Animated_sprite
from typing import Callable
from math import floor, copysign, ceil

class Character_body:
    def __init__(self, position: Vector2, hitbox: Hitbox | MultiHitbox, sprite: Sprite | Animated_sprite, update: Callable):
        self.position = position
        self.hitbox = hitbox
        self.sprite = sprite
        self.updateCustom = update
        self.game_fps = 60
        self.frozen = False
        self.grounded = False
        self.hit_ceil = False
        self.wallL = False
        self.wallR = False
        self.direction = 1
    
    def move_and_slide(self, velocity: Vector2, static_hitbox: Hitbox = Hitbox(Vector2(0, 0), Vector2(0,0))):
        
        velocity2 = velocity * (1.0 / float(self.game_fps))

        if not self.frozen:
            self.wallL = False
            self.wallR = False
            for i in range(ceil(abs(velocity2.x))):
                self.position.x += velocity2.x / ceil(abs(velocity2.x))
                self.hitbox.position = self.position + self.hitbox.local_position
                if static_hitbox.is_colliding_with_hitbox(self.hitbox):
                    if velocity2.x > 0:
                        self.wallR = True
                    else:
                        self.wallL = True
                    while True:
                        self.position.x -= copysign(0.05, velocity2.x)
                        self.hitbox.position = self.position + self.hitbox.local_position
                        if not static_hitbox.is_colliding_with_hitbox(self.hitbox):
                            break
                    break
                    
            self.grounded = False
            self.hit_ceil = False
            for i in range(ceil(abs(velocity2.y))):
                self.position.y += velocity2.y / ceil(abs(velocity2.y))
                self.hitbox.position = self.position + self.hitbox.local_position
                if static_hitbox.is_colliding_with_hitbox(self.hitbox):
                    if velocity.y > 0:
                        self.grounded = True
                    else:
                        self.hit_ceil = True
                    velocity.y = 0.0
                    while True:
                        self.position.y -= copysign(0.05, velocity2.y)
                        self.hitbox.position = self.position + self.hitbox.local_position
                        if not static_hitbox.is_colliding_with_hitbox(self.hitbox):
                            break
                    break
    
    def update(self, frozen: bool):
        self.frozen = frozen
        self.sprite.position = self.position + self.sprite.local_position
        self.hitbox.position = self.position + self.hitbox.local_position
        self.updateCustom(self)
        self.sprite.current_anim.flipped_x = True if self.direction == -1 else False