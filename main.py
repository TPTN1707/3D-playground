from ursina import *

# Initialize the Ursina 3D Engine window
app = Ursina()

# Create a basic 3D entity (a cube)
# We define its model shape, color, scale, and position in 3D space
cube = Entity(
    model='cube',
    color=color.orange,
    scale=(2, 2, 2),       # Width, Height, Depth
    position=(0, 0, 8)     # X=0 (Center), Y=0 (Center), Z=8 (8 units away from camera)
)

def update():
    """This function is automatically called by the engine on every frame"""
    # Rotate the cube around its Y and X axes
    # Multiplying by time.dt ensures consistent rotation speed across different frame rates (FPS)
    cube.rotation_y += time.dt * 45  # Rotate 45 degrees per second around Y-axis
    cube.rotation_x += time.dt * 20  # Rotate 20 degrees per second around X-axis

# Start the application loop
app.run()