from typing import List
import time

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        visited = set()
        queue = [(0,target)]
        while queue:
            step,trgt = queue.pop(0)
            if trgt == "0000":
                return step
            if trgt in deadends:
                continue
            for i,w in enumerate(trgt):
                if int(w) != 0:
                    wp = (int(w) + 1) % 10
                    trgtp = trgt[:i] + str(wp) + trgt[i+1:]

                    wm = (int(w) - 1) % 10
                    trgtm = trgt[:i] + str(wm) + trgt[i+1:]

                    if trgtp not in visited:
                        queue.append((step+1,trgtp))
                        visited.add(trgtp)
                    if trgtm not in visited:
                        queue.append((step+1,trgtm))
                        visited.add(trgtm)

        return -1

# deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
# target = "8888"
# deadends = ["0201","0101","0102","1212","2002"]
# target = "0202"
deadends = ["1000","9000","0100","0900","0010","0090","0001","0009"]
target = "8888"
test = Solution()
start_time = time.time()
print(test.openLock(deadends,target))
print("--- %.8f seconds ---" % (time.time() - start_time))