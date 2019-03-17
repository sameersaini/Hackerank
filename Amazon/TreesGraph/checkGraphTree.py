"""
A graph is a valid tree if all there is no cycle and all nodes can be visited by traversing the tree
To check Cycle:
    For every visited vertex 'v', if there is an connected node 'u'
    such that u has already been visited and u is not parent of v,
    then there is a cycle in graph.
    I have used DFS here to visit every node.
To check visited:
    iterate over the visited array to check all nodes have been visited
"""

class Solution(object):
    def checkCyclic(self, adjList, visited, vertex, parent):
        visited[vertex] = True
        for node in adjList[vertex]:
            if not visited[node]:
                if self.checkCyclic(adjList, visited, node, vertex):
                    return True

            elif node != parent:
                return True

        return False

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adjList = {i: [] for i in range(n)}
        visited = {i: False for i in range(n)}

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        if self.checkCyclic(adjList, visited, 0, -1):
            return False

        for node in visited:
            if not visited[node]:
                return False

        return True

