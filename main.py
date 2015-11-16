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
  
  avl = AVL(30)
  avl.insert(40)
  avl.insert(29)
  avl.insert(39)
  avl.insert(41)
  avl.insert(43)
  
  avl.print_visual_tree()