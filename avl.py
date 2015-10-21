"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067

AVL Tree implementation - Data Structure
AVL tree Class implementation
IFRN - Natal/RN - Brazil
2015

Contact: victor.limeira@outlook.com
"""

from node import *

class empty_tree(Exception):
  pass

class node_not_found(Exception):
  pass

class AVL():
  def __init__(self, node=None):
    if node is not None:
      self.root = Node(node)
    else:
      self.root = None
  
  def insert(self, value):
    """ Add a value to the AVL tree"""
    if self.root is None:
      self.root = Node(value)
      return
    
    node_to_add = self.find_last_match(self.root, value)
    return node_to_add.add_suc(value)
  
  def delete(self, value):
    """ Delete the node that matches the value """
    if self.root is None:
      raise empty_tree()
    else:
      node_to_delete = self.find_last_match(self.root, value)
      if value is node_to_delete.value:
        node_to_delete.auto_delete()
      else:
        raise node_not_found()
    return
        
  
  def find_last_match(self, node, value):
    """ Find the last node on tracking the most approximate value """
    while True:
      if value > node.value:
        if node.right_suc is not None:
          return find_last_match(node.right_suc, value)
        else:
          return node
      elif value < node.value:
        if node.left_suc is not None:
          return find_last_match(node.left_suc, value)
        else:
          return node
      else:
        return node