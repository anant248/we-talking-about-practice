# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # using a priority queue for kth smallest
        # traverse the full BST, adding to pq of max size k
        # add -ve values to pq, so then at the end we return top of pq

        pq = []

        def dfs(root):
            if not root:
                return
            
            heapq.heappush(pq, -root.val)
            if len(pq) > k:
                heapq.heappop(pq)
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)        
        return -heapq.heappop(pq)
