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
    node_to_add.add_suc(value)
    self.check_imbalance(node_to_add)
    return
  
  def delete(self, value):
    """ Delete the node that matches the value """
    if self.root is None:
      raise empty_tree()
    else:
      node_to_delete = self.find_last_match(self.root, value)
      if value is node_to_delete.value:
        node_to_delete.auto_delete()
        #no root detected, delete root node
        if self.root.value is None:
          self.root = None
      else:
        raise node_not_found()
    return
        
  
  def find_last_match(self, node, value):
    """ Find the last node on tracking the most approximate value """
    while True:
      # try to find the right subtree
      if value > node.value:
        if node.right_suc is not None:
          return self.find_last_match(node.right_suc, value)
        else:
          return node
      # try to find the left subtree
      elif value < node.value:
        if node.left_suc is not None:
          return self.find_last_match(node.left_suc, value)
        else:
          return node
      # value found
      else:
        return node
  
  def check_imbalance(self, node):
    """ Check if the node and its predecessors is unbalanced and execute the
    rotatinos """
    if -1 <= node.factor <= 1:
      #balanced
      #check next (root or not)
      if node.pred is not None:
        return self.check_imbalance(node.pred)
      else:
        return
    else:
      #imbalanced
      #test if it is right or left imbalance
      if node.factor is -2:
        return node.rotate_left()
      else:
        return node.rotate_right()
  
  def print_inorder(self, node=None):
    """ Return a list with inorder elements of the tree """
    if node is None:
      node = self.root
      
    inorder_values = []
    
    if node.left_suc:
      inorder_values += self.print_inorder(node.left_suc)
    
    inorder_values += [node.value]
    
    if node.right_suc:
      inorder_values +=self.print_inorder(node.right_suc)
    
    return inorder_values
  
  def print_visual_tree(self, depth=0, node=None):
    """ Print the tree and each node factor in a visual way """
    if node is None:
      node = self.root
    
    # Print right node
    if node.right_suc is not None:
      self.print_visual_tree(depth + 1, node.right_suc)

    # Print self node
    print("    " * depth + str(node.value) + "(" + str(node.factor) + ")")

    # Print left node
    if node.left_suc is not None:
      self.print_visual_tree(depth + 1, node.left_suc)
    
    return
  
  def search(self, value):
    """ Return if the element was found or not """
    if self.root:
      print self.root.find_value(value)
    else:
      print("Empty tree")