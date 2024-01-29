from my_node import Node

class Traverse(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self.headval = None
    def listPrint(self):
        my_value = self.headval
        while my_value is not None:
            print(Node(my_value))
            my_value = my_value.next
def main():
    number_of_nodes = int(input("How many data items do you intend to enter: "))
    while number_of_nodes > 0:
        my_node = input("Enter a data item: ")
        node_elements = Traverse(my_node)
        node_elements.next = number_of_nodes
        node_elements.listPrint()
        number_of_nodes -= 1
if __name__ == '__main__':
    main()