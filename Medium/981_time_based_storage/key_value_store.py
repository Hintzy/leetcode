"""
If key doesn't exist, create key and populate with [time, val]  (setdefault)
If key exists, append current [time, val] to the list of [time, val]'s
"""
import bisect


class TimeMap:

    def __init__(self):
        self.data = {}

    def __repr__(self):
        return f'{self.data}'

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((timestamp, value))
        else:
            self.data.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        if timestamp < self.data[key][0][0]:
            return ""
        elif timestamp >= self.data[key][-1][0]:
            index = len(self.data[key]) - 1
            return self.data[key][index][1]
        else:
            l, r = 0, len(self.data[key]) - 1
            while l <= r:
                mid = (l + r) // 2
                if (self.data[key][mid][0] <= timestamp < self.data[key][mid+1][0]):
                    return self.data[key][mid][1]
                elif timestamp < self.data[key][mid][0]:
                    r = mid - 1
                else:
                    l = mid + 1


tm1 = TimeMap()
print(tm1.set("foo","bar",1))
print(tm1.get("foo",1))
print(tm1.get("foo",3))
print(tm1.set("foo","bar2",4))
print(tm1.get("foo",4))
print(tm1.get("foo",5))
print(tm1.set("foo","zigzag",7))
print(tm1.set("foo","conundrum",8))
print(tm1.set("foo","hyperbole",9))
print(tm1.set("foo","silhouette",10))
print(tm1.set("foo","blasphemy",11))
print(tm1.get("foo", 9))


# tm1.set('OW', 'win', 1)
# tm1.set('OW', 'win', 2)
# tm1.set('OW', 'loss', 4)
# tm1.set('OW', 'win', 16)
# tm1.set('Diablo', 'win', 8)
# tm1.set('Diablo', 'die', 10)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)