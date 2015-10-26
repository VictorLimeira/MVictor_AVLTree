"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067

AVL Tree implementation - Data Structure
AVL Class Test implementation
IFRN - Natal/RN - Brazil
2015

Contact: victor.limeira@outlook.com
"""

import unittest
from avl import *
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        self.avl1 = AVL(1)
        self.avl2 = AVL(2)
        self.avl_empty = AVL()
 
    def test_creation(self):
        self.assertEqual(self.avl1.root.value, 1)
        self.assertEqual(self.avl2.root.value, 2)
    
    def test_creation_empty(self):
        self.assertEqual(self.avl_empty.root, None)
    
    def test_insert_value_to_left(self):
        self.avl2.insert(1)
        self.assertEqual(self.avl2.root.left_suc.value, 1)
    
    def test_insert_value_to_right(self):
        self.avl2.insert(3)
        self.assertEqual(self.avl2.root.right_suc.value, 3)
    
    def test_insert_raise_error(self):
        with self.assertRaises(already_exist):
            self.avl2.insert(2)
    
    def test_delete(self):
        self.avl2.insert(1)
        self.avl2.insert(3)
        # test left deletion
        self.avl2.delete(1)
        self.assertEqual(self.avl2.root.left_suc, None)
        # test right deletion
        self.avl2.delete(3)
        self.assertEqual(self.avl2.root.right_suc, None)
 
if __name__ == '__main__':
    unittest.main()