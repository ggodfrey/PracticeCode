from itertools import combinations as e;golf=lambda c:min([a for a in range(99)if a not in sum([[sum(y)for y in e(c,i+1)]for i in range(len(c))],[0])])
#The above is a 151 character solution to a program that returns the smallest number that can't be paid for with exact change
#Given a list of coins (with repeats)
#Broken up:
#from itertools import combinations as e;
#This imports a function which returns combinations (e([1, 2, 3], 2) will return [1,2],[2,3],[1,3] of a list.
#We import as e to save characters
#golf=lambda c
#This is a way to define a python function on line line to save space
#min([a for a in range(99) if a not in...
#Will find the smallest number between 0 and 99 not in the following list:
#sum([[sum(y)for y in e(c,i+1)]for i in range(len(c))],[0])])
#This loops through the combinations of each length (length specified by i)
#And sums them up then appends them to a list
#This list is 2D so we use sum(*2Dlist*,[0]) to make it 1D with 0 at the start