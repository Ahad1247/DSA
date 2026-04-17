def dfsHelper(node, adj ,vis, ans):
    vis[node] = 1
    ans.append(node)
    
    for i in adj[node]:
        if not vis[i]:
            dfsHelper(i,adj,vis,ans)
            
def dfs(adj):
    # code here
    V = len(adj)
    vis = [0]*V
    ans = []
    start = 0
    
    dfsHelper(start,adj,vis,ans)
    return ans