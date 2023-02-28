import unittest

from features.Node import Node
from features.Stack import Stack


class TestStack(unittest.TestCase):
    def test_Stack(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push("data1")
        self.assertEqual(stack.top.data, "data1")
        stack.push("data2")
        self.assertEqual(stack.top.data, "data2")
        self.assertEqual(stack.top.next_node.data, "data1")


class TestNode(unittest.TestCase):
    def test_Node(self):
        node = Node("data1")
        self.assertEqual(node.data, "data1")
        node_2 = Node("data2", next_node=node)
        self.assertEqual(node_2.data, "data2")
        self.assertEqual(node_2.next_node.data, "data1")
