# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# http://bit.ly/2jvpZ2x

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
  def serialize(self, root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """

    def trav(root):
      if not root:
        val.append('#')
        return
      val.append(str(root.val))
      trav(root.left)
      trav(root.right)

    val = []
    trav(root)
    return ','.join(val)

  def deserialize(self, data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    def trav():
      val = next(vals)
      if val == '#':
        return None
      node = TreeNode(int(val))
      node.left = trav()
      node.right = trav()
      return node

    vals = iter(data.split(','))
    return trav()

    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))
