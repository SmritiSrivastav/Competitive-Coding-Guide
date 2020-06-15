''' 
JUNE LEETCODING CHALLENGE (Week 3 Day 1)
SEARCH IN A BINARY SEARCH TREE

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2
You should return this subtree:

      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.
'''



'''
LOGIC : Use level Order Traversal
'''









# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        queue=[]
        queue.append(root)
        if(root==None):
            return None
        while(len(queue)>0):
            if(queue[0].val==val):
                return queue[0]
            else:
                p=queue[0]
                queue=queue[1:]
                if(p.left):
                    queue.append(p.left)
                if(p.right):
                    queue.append(p.right)
        return None
