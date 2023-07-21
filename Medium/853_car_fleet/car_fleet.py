"""
Problem logic:

Calculate the time it will take the lead car to reach the destination (distance target - position car / speed car).
Store those values in a list.  Zip those values with the start positions and sort the list in reverse order by position.
Initialize the fleets list with the first car, since it will always be a fleet. Iterate through the remainder of the
list to see if there's any collisions with cars behind the first. If there's a collision simply continue onto the next
vehicle in the queue. If there's no collision, append the car fleet list with the last car and continue.

Result is the length of the car fleet list.
"""

from ds_templates import test_series
from test_cases import cases


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    times = [((target - position[i]) / speed[i]) for i in range(len(position))]
    paired = sorted(zip(position, times), reverse=True)
    fleets = [paired[0]]
    if len(paired) > 1:
        for pos, time in paired[1:]:
            if time <= fleets[-1][-1]:
                continue
            else:
                fleets.append((pos, time))
    return len(fleets)


test_series.test_series(carFleet, cases)
