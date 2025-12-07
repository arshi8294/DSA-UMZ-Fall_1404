# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root) -> int:
        pass


if __name__ == "__main__":
    root1 = TreeNode(1,
                    TreeNode(0, TreeNode(0), TreeNode(1)),
                    TreeNode(1, TreeNode(0), TreeNode(1)))
    solution = Solution()
    print(solution.sumRootToLeaf(root1))  # => 22

    root2 = TreeNode(0)
    print(solution.sumRootToLeaf(root2))  # => 0

    root5 = TreeNode(1,
                TreeNode(0, 
                        TreeNode(1, 
                                TreeNode(1))),
                TreeNode(1,
                        TreeNode(0)))
    print(solution.sumRootToLeaf(root5))  # => 17