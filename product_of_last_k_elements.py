from collections import deque
class ProductOfNumbers:

    def __init__(self):
        self.prefix = deque()
        self.prefix.append(1)

    def add(self, num: int) -> None:
        self.prefix.appendleft(self.prefix[0]*num) 
        

    def getProduct(self, k: int) -> int:
       return self.prefix[k] 


obj = ProductOfNumbers()
obj.add(2)
obj.add(3)
obj.add(0)
param_2 = obj.getProduct(2)
print(param_2)
