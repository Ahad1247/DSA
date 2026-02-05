from typing import List

def topKFrequent(words: List[str], k: int) :
    hash_map = {}
    for word in words:
        if word in hash_map:
            hash_map[word] += 1
        else:
            hash_map[word] = 1

    # arr = []
    # while (k>0):
    #     max_key = max(hash_map, key=hash_map.get)
    #     arr.append(max_key)
    #     del hash_map[max_key]
    #     k-=1
    # return sorted(arr)  
    # 
    # Sort by frequency (descending), then lexicographically (ascending)
    sorted_words = sorted(hash_map.keys(), key=lambda x: (-hash_map[x],x))
    return sorted_words[:k]     

words = ["love","leetcode","i","love","coding","love","i","i"]
print(topKFrequent(words,2))

    