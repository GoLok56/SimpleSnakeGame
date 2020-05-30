class GameObject:
  def __init__(self, x, y, on_collided=None):
    self.x = x
    self.y = y
    self.on_collided = on_collided

  def move(self, max_row, max_column):
    pass

  def check_for_event(self, event):
    pass