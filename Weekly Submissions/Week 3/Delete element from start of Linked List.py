# Node class 
class Node:
    # Function to initialize the node object 
    def __init__(self, data=None, next=None):
        self.data = data # Assign data
        self.next = next # Initialize next as null 

# Linked List class 
class LinkedList:
    # Function to initialize the LinkedList object 
    def __init__(self):
        self.head = None
        
    # print function prints contents of linked list starting from head
    def print(self):
        # if linked list is empty
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        #taking empty string and appending values
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> '
            itr = itr.next
        print(llstr)

    # Function to insert a new node at the beginning
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
       
    #remove first element of the singly linkedlist
    def remove_first(self):
      # if linked list is empty
      if self.head is None:
        print("Empty,nothing to remove") 
        return None
      self.head = self.head.next

# Code execution starts here    
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining("Red")
    ll.insert_at_begining("Green")
    ll.insert_at_begining("Black")
    ll.insert_at_begining("Yellow")
    print ("Created Linked List: ")
    ll.print()
    print ("Linked List after deletion at first position: ")
    ll.remove_first()
    ll.print()