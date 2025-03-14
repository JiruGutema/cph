trips = [[2,1,5],[3,3,7]]
capacity = 4

prefix = [0]*1000

for i in range(len(trips)):
    trip = trips[i]
    prefix[trip[1]] += trip[0]
    prefix[trip[2]] -= trip[0]

for i in range(1, len(prefix)):
    prefix[i] = prefix[i] + prefix[i-1]

for tot in prefix:
    if tot > capacity:
        print(False)
        break 
else:
    print(True)

