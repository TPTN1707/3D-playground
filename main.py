from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from src.world.blocks import Voxel

app = Ursina()

# Generate a 12x12 flat starting floor made of interactive Voxel blocks
for z in range(12):
    for x in range(12):
        # We place each block at coordinates (x, 0, z)
        Voxel(position=(x, 0, z))

# Keep our floating orange monument cube in the sky
cube = Entity(
    model='cube',
    color=color.orange,
    scale=(2, 2, 2),
    position=(6, 4, 6),      # Placed near the center of our 12x12 grid
    collider='box'
)

# Create the Player with first-person controls starting in the center of the grid
player = FirstPersonController(
    position=(6, 2, 6)       # Raised slightly so the player lands on the voxels safely
)

def update():
    """Rotate our monument cube every frame"""
    cube.rotation_y += time.dt * 45
    cube.rotation_x += time.dt * 20

# Run the game
app.run()