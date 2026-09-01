from ursina import *
# Import the built-in First-Person Controller prefab from Ursina
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Create a flat green floor so the player has a surface to stand on
floor = Entity(
    model='plane',
    color=color.green,
    scale=(50, 1, 50),       # Large flat plane (50x50 units)
    position=(0, 0, 0),
    collider='box'           # Enable physical collision box so the player doesn't fall through
)

# Create our rotating orange cube, placed slightly above the floor
cube = Entity(
    model='cube',
    color=color.orange,
    scale=(2, 2, 2),
    position=(0, 2, 10),     # Raised to Y=2 so it hovers above the green floor
    collider='box'           # Enable collision for the cube
)

# Create the Player with first-person controls (movement & mouse look)
# This automatically handles W, A, S, D, mouse rotation, and Spacebar to jump
player = FirstPersonController(
    position=(0, 1, 0)       # Start the player slightly above the floor
)

def update():
    """This function rotates the floating cube every frame"""
    cube.rotation_y += time.dt * 45
    cube.rotation_x += time.dt * 20

# Run the game window
app.run()