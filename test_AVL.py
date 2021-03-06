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
        self.avl30 = AVL(30)
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
        
    def test_delete_root(self):
        self.avl2.delete(2)
        self.assertEqual(self.avl2.root, None)
    
    def test_left_rotation_no_lefts(self):
        self.avl1.insert(2)
        self.avl1.insert(3)
        self.assertEqual(self.avl1.root.right_suc.value, 3)
        self.assertEqual(self.avl1.root.left_suc.value, 1)
        self.assertEqual(self.avl1.root.value, 2)
    
    def test_left_rotation_with_lefts(self):
        self.avl30.insert(40)
        self.avl30.insert(29)
        self.avl30.insert(39)
        self.avl30.insert(41)
        self.avl30.insert(43)
        self.assertEqual(self.avl30.root.value, 40)
        self.assertEqual(self.avl30.root.right_suc.value, 41)
        self.assertEqual(self.avl30.root.left_suc.value, 30)
        self.assertEqual(self.avl30.root.left_suc.right_suc.value, 39)
        self.assertEqual(self.avl30.root.left_suc.left_suc.value, 29)
    
    def test_right_rotation_with_rights(self):
        self.avl30.insert(29)
        self.avl30.insert(39)
        self.avl30.insert(28)
        self.avl30.insert(27)
        self.avl30.insert(26)
        self.assertEqual(self.avl30.root.value, 28)
        self.assertEqual(self.avl30.root.right_suc.value, 30)
        self.assertEqual(self.avl30.root.left_suc.value, 27)
        self.assertEqual(self.avl30.root.right_suc.left_suc.value, 29)
        self.assertEqual(self.avl30.root.right_suc.right_suc.value, 39)
 
if __name__ == '__main__':
    unittest.main()