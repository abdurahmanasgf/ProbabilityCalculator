import copy
import random
# Consider using the modules imported above.

class Hat():

    def __init__(self, **kwargs):
        self.contents= []
        for key, value in kwargs.items():
            while value > 0:
                value -= 1
                self.contents.append(key)
        print(self.contents)
    
    def draw(self, number):
        all_removed = []
        if number > len(self.contents):
            return self.contents
        else:
            for i in range(number):
                removed = self.contents.pop(int(random.randrange(len(self.contents))))
                all_removed.append(removed)
            return all_removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        ball_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        count += 1 if ball_req == len(expected_balls) else 0

    return count/num_experiments
