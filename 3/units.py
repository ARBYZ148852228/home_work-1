import world
import texture as skin
from hitbox import Hitbox
from tkinter import NW
from random import randint

class Unit:

 def _change_orientanion(self):
     rand = randint(0, 3)
     if rand == 0:
         self.left()
     if rand == 1:
         self.right()
     if rand == 2:
         self.forward()
     if rand == 3:
         self.backward()
    










 def intersects(self, other_unit):
     value = self._hitbox.intersects(other_unit._hitbox)
     if value:
         self._on_intersects(other_unit)
         other_unit._on_intersects(self)
         return value

 def  _on_intersects(self,other_units):
     self._undo_move()




 def undo_move(self):
     if self._dx == 0 and self._dy == 0:
         return
     self._x -= self._dx
     self._y -= self._dy
     self._update_hitbox()
     self._repaint()
     self._dx = 0
     self._dy = 0





 def create(self):
    pass




 def forward(self):
     pass





 def left(self):
    pass




 def right(self):
     pass



 def stop(self):
     pass



 def update(self):
     pass




 def AI(self):
     pass



def repaint(self):
    screen_x = world.get_screen_x(self._x)
    screen_y = world.get_screen_y(self._y)
    self.__canvas.moveto(self.__id, x=screen_x, y=screen_y)


