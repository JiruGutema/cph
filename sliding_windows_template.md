# General Template I
```
def dynamicwindowatmost(self, nums: str) -> int:
        n = len(nums)
        ans = 0
        Window = # initialize  
        left = 0 
        for right in range(n):
            Window = # update the window with right  
            while window is invalid:
                Window = # remove the left part  
                left += 1  # update left pointer
               
            ans = # update the answer 

        return ans
```
# General Template II
```
def dynamicwindowatleast(self, nums: str) -> int:
        n = len(nums)
        ans = 0
        window = # initialize  
        left = 0 
        for right in range(n):
            Window = # update the window with right  
            while window is valid:
                ans = # update the answer 
                Window = # remove the left part  
                left += 1  # update left pointer
               
           
        return ans
```