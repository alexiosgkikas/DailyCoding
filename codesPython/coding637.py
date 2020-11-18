"""
Daily Coding Problem: Problem #637 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Snapchat.
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], 
you should return [(1, 3), (4, 10), (20, 25)].
"""

def doOverlap(i1,i2):
    if i2[1] < i1[0] or i2[0] > i1[1]:
        return False
    return True


def mergeOverlaps(intervals):
    if len(intervals) <=1:
        return intervals
    
    #sort intervals first 
    intervals.sort(key = lambda x:x[0])
    
    merge_int = [intervals[0]]
    for i in range(1,len(intervals)):
        doMerge = False
        for j in range(0,len(merge_int)):
            if doOverlap(merge_int[j],intervals[i]):
                merge_int[j] = (min(intervals[i][0],merge_int[j][0]),max(intervals[i][1],merge_int[j][1]))
                doMerge = True
                break
        if doMerge is False:
            merge_int.append(intervals[i])
    
    return merge_int



if __name__ == "__main__":
    intervals = [(1, 3),(5, 8),(4, 10),(20, 25)]
    mergelist = mergeOverlaps(intervals)
    print(mergelist)
