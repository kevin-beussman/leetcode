class UndergroundSystem:

    def __init__(self):
        self._idcheck = {}
        self._avetimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self._idcheck[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startstop = (self._idcheck[id][0],stationName)
        triptime = t - self._idcheck[id][1]
        if startstop not in self._avetimes:
            self._avetimes[startstop] = [triptime,1]
        else:
            curtime,n = self._avetimes[startstop]
            self._avetimes[startstop] = [(curtime*n+triptime)/(n+1),n+1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self._avetimes[(startStation,endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

test = UndergroundSystem()
test.checkIn(45,"Leyton",3)
test.checkOut(45,"Waterloo",15)
print(test.getAverageTime("Leyton","Waterloo"))