from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from src.world.blocks import Voxel

app = Ursina()

# Generate a 12x12 flat starting floor
for z in range(12):
    for x in range(12):
        Voxel(position=(x, 0, z))

# Floating monument cube
cube = Entity(
    model='cube',
    color=color.orange,
    scale=(2, 2, 2),
    position=(6, 4, 6),
    collider='box'
)

# Create the Player with first-person controls
player = FirstPersonController(
    position=(6, 2, 6)
)

def update():
    """Rotate our monument cube every frame"""
    cube.rotation_y += time.dt * 45
    cube.rotation_x += time.dt * 20

# NEW: Failsafe input handler for application control
def input(key):
    # Press Escape key to instantly close the window and quit the app
    if key == 'escape':
        application.quit()
    # Press Tab key to lock/unlock the mouse cursor anytime
    elif key == 'tab':
        mouse.locked = not mouse.locked

# Run the game
app.run()