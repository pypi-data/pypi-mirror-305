from pyxel_helper.positioning import Vector2
from math import copysign, floor

class Hitbox:
    """General hitbox class for collisions. Only rectangular hitboxes are allowed"""
    def __init__(self, position: Vector2, hitbox_size: Vector2):
        """
        position is position of hitbox\n
        hitbox_size is the size of the hitbox (for rectangular) in format Vector2(length, height)\n
        """
        self.local_position = position
        self.position = position
        self.local_position = position
        self.size = hitbox_size.round()


    def __repr__(self):
        return f"Hitbox: size = {self.size} | position = {self.position}"

    def is_colliding_with_hitbox(self, other: "Hitbox") -> bool:
        """
        Checks if the two hitboxes are colliding.
        """

        selfposrounded = Vector2(0, 0)
        otherposrounded = Vector2(0, 0)

        if self.size.x % 2 == 1:
            selfposrounded.x = round(self.position.x)
        else:
            selfposrounded.x = floor(self.position.x + 0.5)
        if self.size.y % 2 == 1:
            selfposrounded.y = round(self.position.y)
        else:
            selfposrounded.y = floor(self.position.y + 0.5)
        if other.size.x % 2 == 1:
            otherposrounded.x = round(other.position.x)
        else:
            otherposrounded.x = floor(other.position.x + 0.5)
        if other.size.y % 2 == 1:
            otherposrounded.y = round(other.position.y)
        else:
            otherposrounded.y = floor(other.position.y + 0.5)

        return True if 2 * abs(selfposrounded.x - otherposrounded.x) < self.size.x + other.size.x and 2 * abs(selfposrounded.y - otherposrounded.y) < self.size.y + other.size.y else False

    def is_colliding_with_point(self, other: Vector2) -> bool:
        """
        Checks if the two point is contained in self.
        """

        return True if 2 * abs(self.position.x - other.x) < self.size.x and 2 * abs(self.position.y - other.y) < self.size.y else False

class MultiHitbox(Hitbox):
    """For when you want multiple hitboxes for one object to make more complex hitboxes"""
    def __init__(self, position: Vector2, hitboxes: list[Hitbox]):
        self.position = position
        self.local_position = position
        self.hitboxes = hitboxes
        self.size = Vector2(0, 0)

        for i in self.hitboxes:
            i.position = i.local_position + self.position
    
    def __repr__(self):
        return f"MultiHitboxes: {[repr(i) for i in self.hitboxes]}"

    def is_colliding_with_hitbox(self, other: Hitbox) -> bool:
        self.set_poses()
        return (True in [i.is_colliding_with_hitbox(other) for i in self.hitboxes])
    
    def is_colliding_with_point(self, other: Vector2) -> bool:
        self.set_poses()
        return (True in [i.is_colliding_with_point(other) for i in self.hitboxes])

    def set_poses(self):
        for i in self.hitboxes:
            i.position = i.local_position + self.position

    def update(self):
        for i in self.hitboxes:
            i.position = i.local_position + self.position
