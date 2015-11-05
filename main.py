"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067

AVL Tree implementation - Data Structure
IFRN - Natal/RN - Brazil
2015

Contact: victor.limeira@outlook.com
"""

from node import *
from avl import *

if __name__ == '__main__':
  avl = AVL(1)
  avl.insert(2)
  avl.insert(3)
  avl.insert(4)
  avl.insert(5)
  print(avl.print_inorder())
  avl.print_visual_tree()