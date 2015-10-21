"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067

AVL Tree implementation - Data Structure
Node Class implementation
IFRN - Natal/RN - Brazil
2015

Contact: victor.limeira@outlook.com
"""

class already_exist(Exception):
  pass

class Node():
  def __init__(self, value):
    self.value = value
    self.pred = None
    self.left_suc = None
    self.right_suc = None
    
  def add_suc(self, value):
    """add_suc will add the successor of the current node following the
    AVL tree rules"""
    if(value > self.value):
      self.right_suc = Node(value)
      self.right_suc.pred = self
    elif(value < self.value):
      self.left_suc = Node(value)
      self.left_suc.pred = self
    else:
      raise already_exist("Value already exists.")
  
  def auto_delete(self):
    """ Auto delete the self node """
    suc_side = self.which_suc_side()
    pred_side = self.which_pred_side()
    
    #self has no successor
    if suc_side is "zero":
      if pred_side is "left":
        self.pred.left_suc = None
        return
      else:
        self.pred.right_suc = None
        return
    #self has one successor, and it is left
    elif suc_side is "left":
      #test which side of the predecessor will be updated
      if pred_side is "left":
        self.pred.left_suc = self.left_suc
        return
      else:
        self.pred.right_suc = self.left_suc
    #self has one successor, and it is right
    elif suc_side is "right":
      #test which side of the predecessor will be updated
      if pred_side is "left":
        self.pred.left_suc = self.right_suc
      else:
        self.pred.right_suc = self.right_suc
    #self has two successors - most complex case
    else:
      #TODO: check this link http://www.cs.toronto.edu/~krueger/cscB63h/lectures/tut03.txt
      pass
  
  def which_suc_side(self):
    """ Shows if the node has successors return zero,
        left or right or two to represent """
    if self.left_suc and self.right_suc:
      return "two"
    elif self.left_suc or self.right_suc:
      if self.left_suc:
        return "left"
      else:
        return "right"
    else:
      return "zero"
      
  def which_pred_side(self):
    """ Indicates which side self node is according to its predecessor"""
    if self.pred.left_suc is self:
      return "left"
    else:
      return "right"