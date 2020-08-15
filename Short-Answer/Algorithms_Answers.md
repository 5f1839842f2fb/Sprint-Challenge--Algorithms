#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  O(n)


b)  O(nlogn)


c)  O(n)

## Exercise II

Go to the middle floor and drop an egg.
If the egg breaks, divide the building in half and mark off the floors from your current to the highest
If the egg doesn't break, divide the building in half and mark off the floors from the lowest to the current
Repeat until only one floor is not marked off.

Runtime complexity: O(logn) - Number of operations increase as input size increases, but not linearly because you 
                                don't have to check every floor.
    