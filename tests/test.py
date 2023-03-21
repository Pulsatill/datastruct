import unittest
import pytest

from features.Node import Node
from features.Stack import Stack
from features.custom_queue import Queue
from features.linked_list import LinkedList


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
        self.assertEqual(queue.dequeue(), "data1")
        self.assertEqual(queue.head.data, "data2")
        self.assertEqual(queue.tail.data, "data3")
        self.assertEqual(queue.dequeue(), "data2")
        self.assertEqual(queue.head.data, "data3")
        self.assertEqual(queue.tail.data, "data3")


class TestLinkedList(unittest.TestCase):
    def test_LinkedList(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 1})
        ll.insert_at_end({'id': 2})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(ll.head.data, {'id': 1})
        self.assertEqual(ll.tail.data, {'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertEqual(ll.print_ll(), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")


class TestLinkedListData(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixture(self, capsys):
        self.capsys = capsys

    def test_get_data_by_id(self):
        ll2 = LinkedList()
        ll2.insert_beginning({'id': 5, 'username': 'lazzy508509'})
        ll2.insert_at_end({'id': 6, 'username': 'mik.roz'})
        ll2.insert_at_end({'id': 7, 'username': 'mosh_s'})
        ll2.insert_beginning({'id': 4, 'username': 'serebro'})
        self.assertEqual(ll2.to_list(), [{'id': 4, 'username': 'serebro'},
                                        {'id': 5, 'username': 'lazzy508509'},
                                        {'id': 6, 'username': 'mik.roz'},
                                        {'id': 7, 'username': 'mosh_s'}])
        self.assertEqual(ll2.get_data_by_id(5), {'id': 5, 'username': 'lazzy508509'})
        ll2.get_data_by_id(88)
        stdout, stderr = self.capsys.readouterr()
        self.assertEqual("Данные не являются словарем или в словаре нет 88.", stdout)
