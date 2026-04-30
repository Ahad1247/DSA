from typing import List

class DisjointSet:
    def __init__(self, n):
        self.size   = [1] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    # PATH COMPRESSION
    def find_ult_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ult_parent(self.parent[node])
        return self.parent[node]


    # UNION BY SIZE
    def union_by_size(self, u, v):
        ulp_u = self.find_ult_parent(u)
        ulp_v = self.find_ult_parent(v)
        if ulp_u == ulp_v:
            return False
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v]  += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u]  += self.size[ulp_v]
        return True
        
class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[2])
        
        ds = DisjointSet(V)
        mst_w = 0
        
        for u,v,w in edges:
            if ds.union_by_size(u,v):
                mst_w += w
        
        return mst_w
                