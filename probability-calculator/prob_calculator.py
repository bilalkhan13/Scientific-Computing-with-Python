from random import random, randrange


class Hat:
  def __init__(self, **all_items):
    self.content = []
    for key, value in all_items.items():
      for n in range(value):
        self.content.append(key)
    print(self.content)

  def draw(self, number):
    draw_list = []
    if number >= len(self.content):
      return self.content
    for itr in range(number):
      name = self.content.pop(random.randrange(len(self.content)))
      draw_list.append(name)
    return draw_list



