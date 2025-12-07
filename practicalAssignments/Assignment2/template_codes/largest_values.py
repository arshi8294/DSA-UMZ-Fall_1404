class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root):
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # Test 1: [1,3,2,5,3,None,9]
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(3)
    root1.right.right = TreeNode(9)
    print(solution.largestValues(root1))  # [1,3,9]
    
    # Test 2: [1,2,3]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    print(solution.largestValues(root2))  # [1,3]
    
    # Test 3: [7]
    root3 = TreeNode(7)
    print(solution.largestValues(root3))  # [7]
    
    # Test 4: []
    root4 = None
    print(solution.largestValues(root4))  # []