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
        self.node1.add_suc(3)
        self.node2.add_suc(1)
 
    def test_creation(self):
        self.assertEqual(self.node1.value, 1)
        self.assertEqual(self.node2.value, 2)
 
    def test_add_successor(self):
        self.assertEqual(self.node1.right_suc.value, 3)
        self.assertEqual(self.node2.left_suc.value, 1)
    
    def test_error_raise_value_already_exists(self):
        with self.assertRaises(already_exist):
            self.node1.add_suc(1)
 
if __name__ == '__main__':
    unittest.main()