"""
Author: Mannuel Victor Di Pace Maroja Limeira
#IFRN: 20121014040067

AVL Tree implementation - Data Structure
Node Class Test implementation
IFRN - Natal/RN - Brazil
2015

Contact: victor.limeira@outlook.com
"""

import unittest
from node import *
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
 
    def test_creation(self):
        self.assertEqual(self.node1.value, 1)
        self.assertEqual(self.node2.value, 2)
 
    def test_add_successor(self):
        self.node1.add_suc(3)
        self.node2.add_suc(1)
        self.assertEqual(self.node1.right_suc.value, 3)
        self.assertEqual(self.node2.left_suc.value, 1)
    
    def test_error_raise_value_already_exists(self):
        with self.assertRaises(already_exist):
            self.node1.add_suc(1)
            
    def test_node_auto_delete_two_successors(self):
        self.node2.add_suc(1)
        self.node2.add_suc(3)
        self.assertEqual(self.node2.left_suc.value, 1)
        self.assertEqual(self.node2.right_suc.value, 3)
        self.node2.left_suc.auto_delete()
        self.assertEqual(self.node2.left_suc, None)
        self.node2.right_suc.auto_delete()
        self.assertEqual(self.node2.right_suc, None)
    
    def test_factor_zero(self):
        self.assertEqual(self.node2.factor, 0)
        self.assertEqual(self.node1.factor, 0)
    
    def test_factor_update_left(self):
        self.node2.add_suc(1)
        self.assertEqual(self.node2.factor, 1)
    
    def test_factor_update_right(self):
        self.node2.add_suc(3)
        self.assertEqual(self.node2.factor, -1)
 
if __name__ == '__main__':
    unittest.main()