import unittest


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node


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
