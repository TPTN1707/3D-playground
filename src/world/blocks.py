from ursina import *
import random

# We inherit from Button instead of Entity so the block can easily receive mouse hover and click events
class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,                                      # Set origin to bottom face for easy grid calculation
            texture='white_cube',                              # Built-in Ursina grid texture
            color=color.color(0, 0, random.uniform(0.9, 1.0)), # Slight random variation of white/gray
            highlight_color=color.lime,                        # Highlight green when the mouse hovers over it
        )

    def input(self, key):
        """This function is automatically triggered on any keyboard/mouse input"""
        if self.hovered:
            if key == 'left mouse down':
                # spawn a new voxel in the direction of the clicked face
                # mouse.normal is a 3D vector perpendicular to the clicked face (e.g., (0,1,0) for the top face)
                Voxel(position=self.position + mouse.normal)
                
            elif key == 'right mouse down':
                # Destroy this block on right click
                destroy(self)