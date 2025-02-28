# 找出二叉搜尋樹中兩個節點的最近公共祖先（LCA）

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        # 如果 p 和 q 都在 root 的左子樹
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # 如果 p 和 q 都在 root 的右子樹
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # 如果 p 和 q 分別在 root 的兩側，則 root 是 LCA
        else:
            return root

##題目重點        
# 1.善用二元搜尋樹（BST）的特性：
#   左子樹 所有節點的值都比當前節點小。
#   右子樹 所有節點的值都比當前節點大
# 2.當你需要訪問節點的值時，你應該使用 節點名.val
#   root.left  # 直接訪問左子樹
#   root.right  # 直接訪問右子樹    
