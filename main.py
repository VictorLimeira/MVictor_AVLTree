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
  avl = AVL(1)
  avl.insert(2)
  avl.insert(3)
  avl.insert(4)
  avl.insert(5)
  
  print(avl.print_inorder())
  print("")
  avl.print_visual_tree()
  print("")
  avl.search(3)
  avl.search(6)
  print("")
  avl.delete(3)
  avl.print_visual_tree()
  avl.insert(3)
  print("")
  print("")
  avl.delete(5)
  avl.print_visual_tree()