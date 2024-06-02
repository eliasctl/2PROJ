import pyglet

# Set screen width and height
screen_width = 800
screen_height = 600

# Create the game window
gameWindow = pyglet.window.Window(screen_width, screen_height, caption="Game Menu")

# Load the skeleton warrior image frames
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart/Troop/caveman gifs/skeletonwarriorwalk.gif"), 1, 7)
frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\caveman gifs\skeletonwarriorattack.gif"), 1, 5)
frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\caveman gifs\skeletonspearmanwalk.gif"), 1, 7) """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\caveman gifs\skeletonspearmanattack.gif"), 1, 4) """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\caveman gifs\skeletonarcherwalk.gif"), 1, 8) """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\caveman gifs\skeletonarcherattack.gif"), 1, 15) """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\samurai gifs\samuraiarcherattack.gif"), 1, 14) """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\samurai gifs\samuraiarcherwalk.gif"), 1, 8) """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\samurai gifs\samuraiattack.gif"), 1, 4) """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\samurai gifs\samuraiwalk.gif"), 1, 9)  """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\samurai gifs\samuraicommanderattack.gif"), 1, 5)  """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\samurai gifs\samuraicommanderwalk.gif"), 1, 9)   """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Moderns gifs\Modern 1\WalkModern1.gif"), 1, 7)   """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Moderns gifs\Modern 1\AttackModern1.gif"), 1, 4)    """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Moderns gifs\Modern 2\WalkModern2.gif"), 1, 8)  """   
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Moderns gifs\Modern 2\AttackModern2.gif"), 1, 4)  """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Moderns gifs\Modern 3\WalkModern3.gif"), 1, 8)  """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Moderns gifs\Modern 3\AttackModern3.gif"), 1, 4)  """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Robots gifs\Robot 1\WalkRobot1.gif"), 1, 8) """
""" frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Robots gifs\Robot 1\AttackRobot1.gif"), 1, 8) """
"""frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Robots gifs\Robot 2\WalkRobot2.gif"), 1, 6) """
"""frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Robots gifs\Robot 2\AttackRobot2.gif"), 1, 11)""" 
"""frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Robots gifs\Robot 3\WalkRobot3.gif"), 1, 8)"""
frame_images = pyglet.image.ImageGrid(pyglet.image.load("pixelart\Troop\Robots gifs\Robot 3\AttackRobot3.gif"), 1, 4)



# Create an animation from the image frames
animation = pyglet.image.Animation.from_image_sequence(frame_images, 0.1, loop=True)

# Create a sprite from the animation
skeleton_warrior_sprite = pyglet.sprite.Sprite(animation)

# Troop 1
troopSize = min(screen_width, screen_height) // 20
troopRect = pyglet.shapes.Rectangle(screen_width // 3.85 - troopSize // 2, screen_height * 4 // 4.1 - troopSize // 2, troopSize, troopSize)

# Main game loop
@gameWindow.event
def on_draw():
    gameWindow.clear()
    troopRect.draw()
    skeleton_warrior_sprite.draw()

pyglet.app.run()
