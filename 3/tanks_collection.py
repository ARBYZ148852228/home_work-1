from random import randint
from tank import Tank
import world

_tanks = []
_canvas = None

def initialize(canv):
    global _canvas
    _canvas = canv
<<<<<<< HEAD
    player = Tank(canvas=canv, x = world.BLOCK_SIZE*2,y = world.BLOCK_SIZE*4, ammo=100, speed=2, bot=False)
    enemy = Tank(canvas=canv,x = world.BLOCK_SIZE*4, y = world.BLOCK_SIZE*6, ammo=100, speed=2, bot=True)
=======
    player = Tank(canvas=canv,
                  x=world.BLOCK_SIZE * 2,
                  y=world.BLOCK_SIZE * 4, ammo=100, speed=2, bot=False)
    enemy = Tank(canvas=canv,
                 x=world.BLOCK_SIZE * 4,
                 y=world.BLOCK_SIZE * 6, ammo=100, speed=2, bot=True)
>>>>>>> d742d6360d274e10393a8ee7985e3e7093db6595
    #neutral = Tank(canvas=canv, x=300, y=300, ammo=100, speed=2, bot=False)
    #neutral.stop()
    enemy.set_target(player)
    _tanks.append(player)
    _tanks.append(enemy)
    print(_tanks)

def get_player():
    return _tanks[0]

def update():
    for tank in _tanks:
        tank.update()
        check_collision(tank)

def check_collision(tank):
    for other_tank in _tanks:
        if tank == other_tank:
            continue
        if tank.inersects(other_tank):
            return True
    return False

def spawn_enemy():
    while True:
        pos_x = randint(200,800)
        pos_y = randint(200,600)
        t = Tank(_canvas, x=pos_x, y=pos_y, ammo=100, speed=2)
        if not check_collision(t):
             t.set_target(get_player())
             _tanks.append(t)
             return True