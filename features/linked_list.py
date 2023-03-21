class Node:
    ll_lst = []

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node
        ll_string += ' None'
        print(ll_string)
        return f"{ll_string}"

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        if self.tail is None:
            self.tail = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        self.tail.next_node = new_node
        self.tail = new_node

    def to_list(self):
        ll_lst = []
        node = self.head
        if node is None:
            return None
        while node:
            ll_lst.append(node.data)
            node = node.next_node
        return ll_lst

    def get_data_by_id(self, data):
        ll_lst = self.to_list()
        for d in ll_lst:
            try:
                if d.get('id') == data:
                    return d
            except AttributeError:
                print(f"Данные не являются словарем или в словаре нет {data}.")
