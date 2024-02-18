# Time Based Key-Value Store
#from typing import List, Optional
#from functools import lru_cache
#from collections import defaultdict
#import heapq

class TimeMap:

    def __init__(self):
        self._keystorage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self._keystorage:
            self._keystorage[key].append((timestamp,value))
        else:
            self._keystorage[key] = [(timestamp,value)]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self._keystorage:
            return ""
        vals_times = self._keystorage[key]

        
        L, R = 0, len(vals_times)-1
        if L != R:
            while L != R-1:
                M = (L+R)//2
                if vals_times[M][0] == timestamp:
                    L = M
                    break
                elif vals_times[M][0] > timestamp:
                    R = M
                else:
                    L = M

        if vals_times[R][0] <= timestamp:
            return vals_times[R][1]
        elif vals_times[L][0] <= timestamp:
            return vals_times[L][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

def main():
    obj = TimeMap()
    # obj.set("12345","13",2)
    # param_2 = obj.get("12345",1)
    # print(param_2)
    obj.set("foo","bar",1)
    
    print(obj.get("foo",1))
    print(obj.get("foo",2))
    obj.set("foo","bar2",4)
    print(obj.get("foo",4))
    print(obj.get("foo",5))

if __name__ == "__main__":
    main()