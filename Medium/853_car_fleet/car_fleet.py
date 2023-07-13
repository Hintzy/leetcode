"""
Problem logic:

Calculate the time it will take the lead car to reach the destination (distance target - position car / speed car),
increment a car fleet value by one
Pop next value from the stack, while the car behind it has equal or lesser time that car ahead continue to pop values
until you reach a value that takes longer, at which point you increment the car fleet count again.
Go through the entire stack until you reach the end.
"""

from ds_templates import test_series
from test_cases import cases


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    times = []
    fleet_count = 1
    for i, pos in enumerate(position):
        time = round(((target - pos) / speed[i]), 2)
        times.append(time)
    # create a lead time value and increment fleet
    lead_time = times.pop(0)
    # while there are values in the speed stack keep popping values off the stack until you hit one that's greater than
    # the lead time.  This value becomes the next lead time and increment the fleet count by 1
    while times:
        next_car = times.pop(0)
        if next_car > lead_time:
            lead_time = next_car
            fleet_count += 1

    return fleet_count

# tar = 100
# pos = [10, 20, 30]
# spds = [10, 20, 10]
#
# print(carFleet(tar, pos, spds))

test_series.test_series(carFleet, cases)