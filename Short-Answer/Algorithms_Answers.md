#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    This would be O(n) because n^2 === n


b)
This would be Log(n) because j is doubling each round


c)
    This would be n because it recureses and subtract 1 each time

## Exercise II

The best algorithm for this problem would be to use Binary seatch strategy 

low = 0
high = n
mid = n // 2

while low <= high:
    if egg breaks:(we are too high)
        high = mid - 1
        mid = high - low // 2
    if egg does not break: (we are not high enough)
        low = mid + 1 
        mid = high - low // 2 


repeat this step until we narrow it down two floors:
    if the final two swquences are Break then No Breakm then we know f is the latter floor

    if the final two swquences are no break and then break, then we knoe f is the former floor

This would have a tuntime complexity of O(log n) since the field of possible correct answers is being halved on very loop

