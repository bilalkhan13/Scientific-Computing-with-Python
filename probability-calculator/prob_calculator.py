import random
import copy

class Hat:
    def __init__(self, **color_balls):
        self.contents = []

        for key, value in color_balls.items():
            for n in range(value):
                self.contents.append(key)

        self.INITIAL_CONTENTS = copy.copy(self.contents)

    def reset(self):
        self.contents = copy.copy(self.INITIAL_CONTENTS)

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
            self.contents = copy.copy(self.INITIAL_CONTENTS)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_count = 0

    for experiment in range(num_experiments):
        expected_balls_working_copy = copy.copy(expected_balls)
        hat.reset()
        returned_balls = hat.draw(num_balls_drawn)

        for ball_color, ball_count in expected_balls.items():
            for i in range(ball_count):

                if ball_color in returned_balls:
                    returned_balls.remove(ball_color)
                    expected_balls_working_copy[ball_color] -= 1

            if sum(v for v in expected_balls_working_copy.values()) == 0:
                expected_count += 1

    probability = expected_count / num_experiments
    return probability
