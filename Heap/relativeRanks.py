from typing import List
import heapq

def findRelativeRanks1(score: List[int]):
    sorted_scores = sorted(score, reverse=True)

    map = {}
    for i in range(len(sorted_scores)):
        map[sorted_scores[i]] = i+1
    print(map)
    out = []

    for score in score:
        rank = map[score]
        if rank == 1:
            out.append("Gold Medal")
        elif rank == 2:
            out.append("Silver Medal")
        elif rank == 3:
            out.append("Bronze Medal")
        else:
            out.append(str(rank))
    return out


def findRelativeRanks2(score: List[int]):
    n = len(score)
    heap = []
    for i in range(len(score)):
        heapq.heappush(heap,(-score[i],i))
    
    rank = [0]*n
    place = 1
    while heap:
        originalIndex = heapq.heappop(heap)[1]
        print(originalIndex)



score = [10,3,8,9,4]
# print(findRelativeRanks1([5,4,3,1,2]))
findRelativeRanks2(score)