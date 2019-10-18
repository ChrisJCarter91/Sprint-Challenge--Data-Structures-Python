class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

#append an element at the end of the buffer

  def append(self, item):
    if self.current == self.capacity:
      self.current = 0
    self.storage[self.current] = item
    self.current += 1

  def get(self):
    full = []
    for item in self.storage:
      if item != None:
        full.append(item)
    return full