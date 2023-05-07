from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Block(Button):
    def __init__(self,positio = (0,0,0)):
        super().__init__(
            parent = scene,
            position = positio,
            model = "cube",
            origin_y = 0.5,
            textture = "white_cube",
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.green)

    def input(self,key):
        if key == "escape":
            quit()
        if self.hovered:
            if key == "left mouse down":
                destroy(self)
            if key == "right mouse down":
                block = Block(positio=self.position + mouse.normal)

for z in range(32):
    for x in range(32):
        for y in range(1):
            block = Block((x,y,z))

app = Ursina()

player = FirstPersonController()

app.run()
