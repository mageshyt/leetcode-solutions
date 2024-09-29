from collections import defaultdict
class AllOne:

    def __init__(self):
        self.container= defaultdict(int)

        

    def inc(self, key: str) -> None:
        self.container[key]+= 1


        

    def dec(self, key: str) -> None:
        if key in self.container:
            self.container[key]-= 1
            if self.container[key]==0:
                del self.container[key]

        

    def getMaxKey(self) -> str:
        if not self.container:
            return ""
        maxVal=max(self.container.values())
        for key,val in self.container.items():
            if val==maxVal:
                return key

        

    def getMinKey(self) -> str:
        if not self.container:
            return ""
        minVal=min(self.container.values())
        for key,val in self.container.items():
            if val==minVal:
                return key
        

        

s=AllOne()
print(s.inc("hello"))
print(s.inc("hello"))
print(s.getMaxKey())
print(s.getMinKey())
print(s.inc("leet"))
print(s.getMaxKey())
print(s.getMinKey())
print(s.container)
