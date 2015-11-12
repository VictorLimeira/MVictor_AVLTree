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
    self.factor = 0
    
  def add_suc(self, value):
    """add_suc will add the successor of the current node following the
    AVL tree rules"""
    #added node to the right subtree
    if(value > self.value):
      self.right_suc = Node(value)
      self.right_suc.pred = self
      self.right_suc.update_factor_insert()
    #added node to the left subtree
    elif(value < self.value):
      self.left_suc = Node(value)
      self.left_suc.pred = self
      self.left_suc.update_factor_insert()
    else:
      raise already_exist("Value already exists.")
  
  def auto_delete(self):
    """ Auto delete the self node """
    suc_side = self.which_suc_side()
    if self.pred is not None:
      pred_side = self.which_pred_side()
    else:
      pred_side = None
    
    #self has no successor
    if suc_side is "zero":
      if pred_side is "left":
        self.pred.left_suc = None
        return self.update_factor_delete()
      elif pred_side is "right":
        self.pred.right_suc = None
        return self.update_factor_delete()
      #self is the root node
      else:
        self.value = None
        return
    #self has one successor, and it is left
    elif suc_side is "left":
      #test which side of the predecessor will be updated
      if pred_side is "left":
        self.pred.left_suc = self.left_suc
        return self.update_factor_delete()
      else:
        self.pred.right_suc = self.left_suc
        return self.update_factor_delete()
    #self has one successor, and it is right
    elif suc_side is "right":
      #test which side of the predecessor will be updated
      if pred_side is "left":
        self.pred.left_suc = self.right_suc
        return self.update_factor_delete()
      else:
        self.pred.right_suc = self.right_suc
        return self.update_factor_delete()
    #self has two successors - most complex case
    else:
      # find the most left node on the right subtree
      # substitute the value and exclude the most left node
      most_left = self.find_most_left(self.right_suc)
      self.value = most_left.value
      most_left.auto_delete()
      return self.update_factor_delete()
  
  def which_suc_side(self):
    """ Shows if the node has successors
        return zero, left or right, or two to represent successors """
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
    try:
      left = self.pred.left_suc
    except:
      return None
      
    if left is self:
      return "left"
    else:
      return "right"
      
  def find_most_left(self, node):
    """ Find the most left node on the right subtree """
    if node.left_suc is None:
      return node
    else:
      return self.find_most_left(node.left_suc)
  
  def update_factor_insert(self):
    """ Update the factor of a insertion """
    if self.which_pred_side() is "left":
      self.pred.factor += 1
      if self.pred.factor is 0 or self.pred.factor is 2:
        return
      else:
        return self.pred.update_factor_insert()
    elif self.which_pred_side() is "right":
      self.pred.factor -= 1
      if self.pred.factor is 0 or self.pred.factor is -2:
        return
      else:
        return self.pred.update_factor_insert()
    #root detected
    else:
      return
  
  def update_factor_delete(self):
    """ Update the factor of a deletion """
    #left subtree deleted
    if self.pred.value > self.value:
      self.pred.factor -= 1
      if self.pred.factor is not 0:
        return
      else:
        if self.pred:
          return self.pred.update_factor_insert()
        else:
          return
    #right subtree deleted
    elif self.pred.value < self.value:
      self.pred.factor += 1
      if self.pred.factor is not 0:
        return
      else:
        if self.pred:
          return self.pred.update_factor_insert()
        else:
          return
    #root detected
    else:
      return
  
  def rotate_left(self):
    """ Rotates left and test its subcases """
    #self is the top node
    #clone nodes that will be changed
    bot = self.right_suc.right_suc
    mid = self.right_suc
    top = self
    top_left = self.left_suc
    mid_left = mid.left_suc
    
    #swap values of top and mid
    top.value, mid.value = mid.value, top.value
    
    #update links to mid turns into top left:
    # 1 - Bot predecessor turns into top
    bot.pred = top
    # 2 - Top right successor turns into bot
    top.right_suc = bot
    # 3 - Deal with the lefts
    # Two lefts
    if mid.left_suc and top.left_suc:
      # Change mid and top's lefts
      top_left.pred = mid
      top_left.right_suc = mid.left_suc
      mid_left.pred = top_left
      # Mid left link turns into top's left
      mid.left_suc = top_left
      # Update top factor
      top.factor += 2
      mid.factor += 1
    # One left
    elif mid.left_suc or top.left_suc:
      # TODO
      pass
    # No lefts
    else:
      top.left_suc = mid
      mid.pred = top
      mid.right_suc = None
      # Update factor
      top.factor += 2
      mid.factor += 1
      return
  
  def rotate_right(self):
    """ Rotates right and test its subcases """
    pass
  
  def find_value(self, value):
    if self.value is value:
      return "Valor encontrado"
    elif self.value > value:
      if self.left_suc:
        return self.left_suc.find_value(value)
      else:
        return "Valor nao encontrado"
    elif self.value < value:
      if self.right_suc:
        return self.right_suc.find_value(value)
      else:
        return "Valor nao encontrado"