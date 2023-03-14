import unittest

from features.Node import Node
from features.Stack import Stack
from features.custom_queue import Queue


class TestStack(unittest.TestCase):
    def test_Stack(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push("data1")
        self.assertEqual(stack.top.data, "data1")
        stack.push("data2")
        self.assertEqual(stack.top.data, "data2")
        self.assertEqual(stack.top.next_node.data, "data1")
        stack.push("data3")
        stack.pop()
        self.assertEqual(stack.top.data, "data2")
        stack.pop()
        self.assertEqual(stack.top.data, "data1")


class TestNode(unittest.TestCase):
    def test_Node(self):
        node = Node("data1")
        self.assertEqual(node.data, "data1")
        node_2 = Node("data2", next_node=node)
        self.assertEqual(node_2.data, "data2")
        self.assertEqual(node_2.next_node.data, "data1")


class TestQueue(unittest.TestCase):
    def test_Queue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.head.next_node.data, "data2")
        self.assertEqual(queue.tail.data, "data3")
        self.assertEqual(queue.tail.next_node, None)
