from features.Node import Node


class Stack:
    stack = []

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        popped_data = self.top
        if self.top is None:
            return None
        else:
            self.top = self.top.next_node
            return popped_data.data
