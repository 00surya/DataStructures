# Simple Linked List - deletion in O(1) insertion O(n)

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList1:

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self,data):
        # inserting element with the time complexity of O(n).

        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node

        else:
            last = self.head
            while last.next:
                last = last.next

            last.next = new_node

    def pop(self):
        # Deletion of node with the time complexity of O(1)

        if self.head==None:
            return None
        else:
            del_val = self.head
            self.head = self.head.next

            return del_val.data


    def traverse(self,data):
        # traversing with the time complexity O(n)

        last = self.head
                
        while last.next:
            if last.data==data:
                break
            last = last.next

        if last.data!=data:
            # print(False)
            return False
        else:
            # print(True)
            return True


# l_list = LinkedList1()

# l_list.push(10)
# l_list.push(20)
# l_list.push(30)
# l_list.traverse(10)
# l_list.print_list()




# Simple Linked List - deletion in O(1) insertion O(1)

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList2(LinkedList1):

    def __init__(self):
        self.head = None
        self.tail = None

    # inserting element with the time complexity of O(1).
    def push(self,data):

        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            
        else:
            self.tail.next = new_node
            self.tail = new_node




l_list = LinkedList2()

l_list.push(10)
l_list.push(20)
l_list.push(30)

# l_list.pop()


l_list.print_list()


print(f"element_present: {l_list.traverse(40)}")
