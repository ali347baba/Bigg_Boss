from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise

app = Ursina()
player = FirstPersonController()
player.y = 200
player.cursor.visible = False
window.exit_button.visible = False
grass_Tex = 'Grass_Block_Tex.png'
grass_Model = 'minecraft_grass_block.fbx'
Zombie1 = load_texture('zombie.png')
def input(key):
    if key == 'escape':
        quit()

def update():
    if player.y < -3:
        player.y = 10
    zombie1.look_at(player, 'forward')
    zombie1.rotation_x = 0
    genTerr()

noise = PerlinNoise(octaves=2, seed=2123)
amp = 3
freq = 12

shells = []
shellWidth = 10
for i in range(shellWidth*shellWidth):
    ent = Entity(model=grass_Model, texture=grass_Tex, collider='box')
    shells.append(ent)

def genTerr():
    global amp, freq
    for l in range(shellWidth*shellWidth): # len(shells)):
        x = shells[l].x = floor((i/shellWidth) + player.x - 0.5*shellWidth)
        z = shells[l].z = floor((i%shellWidth) + player.z - 0.5*shellWidth)
        y = shells[l].y = floor(noise([x/freq, z/freq]) * amp)

Zombie = load_model('zombie.fbx')
zombie1 = Entity(model=Zombie, texture=Zombie1, scale=0.07, double_sided=True, y=3.1)

app.run()
