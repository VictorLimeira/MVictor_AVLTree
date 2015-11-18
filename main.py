"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067

AVL Tree implementation - Data Structure
IFRN - Natal/RN - Brazil
2015

Contact: victor.limeira@outlook.com
"""
from avl import *

if __name__ == '__main__':
  
  ## Left rotation
  # avl = AVL(30)
  # avl.insert(40)
  # avl.insert(29)
  # avl.insert(39)
  # avl.insert(41)
  # avl.insert(43)
  # avl.print_visual_tree()
  
  ## Right rotation
  # avl = AVL(30)
  # avl.insert(29)
  # avl.insert(39)
  # avl.insert(28)
  # avl.insert(27)
  # avl.insert(26)
  # avl.print_visual_tree()
  
  ## Left-Right rotation
  # avl = AVL(30)
  # avl.insert(28)
  # avl.insert(29)
  # avl.print_visual_tree()
  
  ## Right-Left rotation
  avl = AVL(30)
  avl.insert(32)
  avl.insert(31)
  avl.print_visual_tree()