import matplotlib.pyplot as plt
import numpy as np
import math
import time
import random

def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

random.seed(1)

NUM_DRONES = 10000
AIRSPACE_SIZE = 128000 # 128 km
CONFLICT_RADIUS = 500  # Meters.

def gen_coord():
    return int(random.random() * AIRSPACE_SIZE)

positions = [[gen_coord(), gen_coord()] for i in range(NUM_DRONES)]

@timer_func
def count_conflicts(positions, radius):
    """
    Given `positions` of a number of drones and a `radius` calculate
    how many are within the conflict radius of another.
    """
    N = len(positions)
    conflicts = [ 0 ] * N

    for i in range(N):
        for j in range(i + 1, N):
            # get drones positions
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            # calculate distance between drones
            if (x2-x1)**2 + (y2-y1)**2 <= radius**2:
                conflicts[i] = 1
                conflicts[j] = 1

    return sum(conflicts)

@timer_func
def fast_count_conflicts(positions, radius):
    """
    Given `positions` of a number of drones and a `radius` calculate
    how many are within the conflict radius of another.
    """
    positions = sorted(positions)
    N = len(positions)
    conflicts = set()

    for i in range(N):
        j = i - 1
        while j >= 0 and abs(positions[i][0] - positions[j][0]) <= radius:
                if (positions[j][0]-positions[i][0])**2 + (positions[i][1]-positions[j][1])**2 <= radius**2:
                    conflicts.add(i)
                    conflicts.add(j)
                j -= 1

        j = i + 1
        while j < N and abs(positions[i][0] - positions[j][0]) <= radius:

                if (positions[j][0]-positions[i][0])**2 + (positions[i][1]-positions[j][1])**2 <= radius**2:
                    conflicts.add(i)
                    conflicts.add(j)
                j += 1

    return len(conflicts)


if __name__ == '__main__':
    conflicts = count_conflicts(positions, CONFLICT_RADIUS)
    print(f'conflicts: {conflicts}')

    conflicts = fast_count_conflicts(positions, CONFLICT_RADIUS)
    print(f'conflicts: {conflicts}')
