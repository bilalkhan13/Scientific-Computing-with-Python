from random import random, randrange
import copy

class Hat:
  def __init__(self, **all_items):
    self.contents = []
    for key, value in all_items.items():
      for n in range(value):
        self.contents.append(key)
    print(self.contents)

    self.__intial_contents = copy.copy(self.contents)

  def reset(self):
    self.contents = copy.copy(self.__intial_contents)

  def draw(self, count):
    # Draw the specified count of items from the hat, return all items if the count is > number of items
    try:
      drawn = random.sample(self.contents, count)
    except ValueError:
      drawn = copy.copy(self.contents)

    # Remove the items drawn from the hat
    for item in drawn:
      self.contents.remove(item)

    # Refill the hat if empty
    if len(self.contents) == 0:
      self.contents = copy.copy(self.__initial_contents)

    return drawn

    # if count >= len(self.contents):
    #   return self.contents
    # for itr in range(count):
    #   name = self.contents.pop(random.randrange(len(self.contents)))
    #   draw_list.append(name)
    return draw_list



