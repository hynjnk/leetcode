# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        self.cloneNodes = dict()
        return self.cloneDfs(node)

    def cloneDfs(self, node: 'Node'):
        if node.val in self.cloneNodes:
            return self.cloneNodes[node.val]

        cloneNeighbors = []
        clone = Node(node.val, cloneNeighbors)
        self.cloneNodes[clone.val] = clone

        for neighbor in node.neighbors:
            cloneNeighbors.append(self.cloneDfs(neighbor))

        return clone
