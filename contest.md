1.
<!-- If adding n doesn't exceed s, it increments curr by n. -->
<!-- If adding n would exceed s, it just adds the remaining difference (s - curr). -->
<!-- In both cases, count is incremented. -->

n,s = list(map(int, input().split()))
 
count = 0
curr = 0
 
while curr < s:
 
    if s - curr >= n:
        curr += n
    else:
        curr += s - curr
    count += 1
 
print(count)

2. 
<!-- if the top of the stack and the current character are not the same, pop the top of the stack -->
<!-- otherwise, push the current character to the stack -->

n= map(int, input())
s = input()

stack = []

for char in s:
    if stack and stack[-1] != char:
        stack.pop()
    else:
        stack.append(char)

print(len(stack))

3. 

<!--If smallest_p is empty, add the first number to it.
    Otherwise:
    If num is smaller than or equal to the first element in smallest_p, insert it at the front (appendleft()).
    Otherwise, insert it at the back (append()). -->

from collections import deque
text_cases = int(input())
 
for _ in range(text_cases):
    smallest_p = deque()
    n = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        if not smallest_p:
            smallest_p.append(num)
        else:
            if smallest_p[0] >= num:
                smallest_p.appendleft(num)
            else:
                smallest_p.append(num)
    print(*smallest_p)
4. 

<!-- If the id is already in the display, skip it. -->
<!-- If the display is full, remove the last element. -->
<!-- Add the id to the front of the display. -->

from collections import deque
 
n,k = list(map(int, input().split()))
ids = list(map(int, input().split()))
 
curr_display = deque()
display_set = set()
 
for id in ids:
    if id in display_set:
        continue
    if len(curr_display) == k:
        removed_id = curr_display.pop()
        display_set.remove(removed_id)
    curr_display.appendleft(id)
    display_set.add(id)
    
print(len(curr_display))
print(*(curr_display))

5. 
<!-- Purpose of seen Dictionary: -->
<!-- The dictionary has two keys: '0' and '1', each of which stores a list of indices of subsequences that are waiting for the next character to be '0' or '1', respectively. -->

<!-- Here’s how it helps: -->

<!-- Tracking Available Subsequences: -->
<!-- When processing the string, if the current character (char) is '0' or '1', we look at seen[char] to check if there’s any subsequence that is ready to accept this character. -->
<!-- If there is a subsequence waiting for '0' or '1', we use the last available subsequence and add the current character to it. -->
<!-- If there isn’t a subsequence ready for the current character, we start a new subsequence and assign it to the opposite character for the next step (because subsequences must alternate). -->
<!-- How it Works: -->
<!-- seen[char] Tracks the Next Expected Character: -->

<!-- The key idea here is that a subsequence will alternate between 0 and 1. -->
<!-- If we are adding a 1, the next character in the subsequence should be a 0, and vice versa. -->
<!-- seen['1'] keeps track of subsequences that expect a 0 next, and seen['0'] tracks subsequences that expect a 1 next. -->
<!-- When Processing the String: -->

<!-- If the character (char) can be added to an existing subsequence: -->
<!-- The subsequence that is ready for this character (seen[char] has an entry) is selected. -->
<!-- The current character is added to that subsequence. -->
<!-- Then, we update seen so that this subsequence now expects the opposite character (because subsequences alternate between 0 and 1). -->
<!-- If no subsequence can be used: -->
<!-- A new subsequence is created for the current character. -->
<!-- The new subsequence is added to the seen dictionary with the opposite character as the expected next one. -->
<!-- Example: -->
<!-- Let's take the string 101010 as an example: -->

<!-- Processing the first character ('1'): -->

<!-- seen['1'] is empty, so no subsequence can be used for this 1. -->
<!-- A new subsequence is created: parts = [[1]]. -->
<!-- Now, seen['0'] needs to expect the next character (which should be '0'), so seen['0'] = [0]. -->
<!-- Processing the second character ('0'): -->

<!-- seen['0'] is not empty, so we can use the subsequence that expects '0'. -->
<!-- Pop the subsequence at index 0 from seen['0'], and add this 0 to it: parts = [[1, 2]]. -->
<!-- Now, this subsequence expects '1', so we append index 0 to seen['1']. -->
<!-- Processing the third character ('1'): -->

<!-- seen['1'] is not empty, so we can use the subsequence that expects '1'. -->
<!-- Pop the subsequence at index 0 from seen['1'], and add this 1 to it: parts = [[1, 2, 3]]. -->
<!-- Now, this subsequence expects '0', so we append index 0 to seen['0']. -->
<!-- Processing the fourth character ('0'): -->

<!-- seen['0'] is not empty, so we can use the subsequence that expects '0'. -->
<!-- Pop the subsequence at index 0 from seen['0'], and add this 0 to it: parts = [[1, 2, 3, 4]]. -->
<!-- Now, this subsequence expects '1', so we append index 0 to seen['1']. -->
<!-- Processing the fifth character ('1'): -->

<!-- seen['1'] is not empty, so we can use the subsequence that expects '1'. -->
<!-- Pop the subsequence at index 0 from seen['1'], and add this 1 to it: parts = [[1, 2, 3, 4, 5]]. -->
<!-- Now, this subsequence expects '0', so we append index 0 to seen['0']. -->
<!-- Processing the sixth character ('0'): -->

<!-- seen['0'] is not empty, so we can use the subsequence that expects '0'. -->
<!-- Pop the subsequence at index 0 from seen['0'], and add this 0 to it: parts = [[1, 2, 3, 4, 5, 6]]. -->
<!-- Now, this subsequence expects '1', so we append index 0 to seen['1']. -->
