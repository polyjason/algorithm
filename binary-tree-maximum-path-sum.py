# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
       def maxPathWithRoot(root):
          if not root.left and not root.right:
              return root.val,root.val
          elif root.left and not root.right:
              max_child,child_sum = maxPathWithRoot(root.left)
              return max(max_child,max(root.val,child_sum+root.val)),max(root.val,child_sum+root.val)
          elif root.right and not root.left:
              max_child,child_sum = maxPathWithRoot(root.right)
              return max(max_child,max(root.val,child_sum+root.val)),max(root.val,child_sum+root.val)
          else:
              max_left_child,child_left_sum = maxPathWithRoot(root.left)
              max_right_child,child_right_sum = maxPathWithRoot(root.right)
              return max(max_left_child,max_right_child,(root.val +(child_left_sum if child_left_sum>0 else 0) + (child_right_sum if child_right_sum > 0 else 0))),max(child_left_sum,child_right_sum, 0)+root.val
        return maxPathWithRoot(root)[0]

