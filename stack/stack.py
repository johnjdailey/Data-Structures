"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# 1. Implement the Stack class using an array as the underlying storage structure.

#class Stack:
#    def __init__(self):
#        self.size = 0
#        # self.storage = ?
#        self.storage = []
#
#    def __len__(self):
#        return self.size
#
#    def push(self, value):
#        self.size +=1
#        return self.storage.append(value)
#
#    def pop(self):
#        if self.size != 0:
#            self.size -= 1
#            return self.storage.pop()


# 2. Re-implement the Stack class, this time using the linked list implementation as the underlying storage structure.

# Linear data structure made up of nodes and refs to the next node

# Lets make some node class

class Node:
    def __init__(self, value, next_node = None):
        # Value that the node is holding
        self.value = value
        # Ref to the next node in the chain
        self.next_node = next_node
    
    def get_value(self):
        """
        Method to get the value of a node
        """
        return self.value

    def get_next(self):
        """
        Method to get the node's "next_node"
        """
        return self.next_node

    def set_next(self, new_next):
        """
        Method to update the node's "next_node" to the new_next
        """
        self.next_node = new_next


# Now lets think of how we can make nodes interact in a way that consolidates their pieces together

# Lets make a LinkedList class
# Think of the idea of having a head and a tail like a snake 
# Where the snake can grow based upon having more links in it

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # Wrap the value in a new Node
        new_node = Node(value)
        # Check if the linked list is empty
        if self.head is None and self.tail is None:
            # Set the head and tail to the new node
            self.head = new_node
            self.tail = new_node
        # Otherwise the list must have at least one item in there
        else:
            # Update the last node's "next_node" to the new node
            self.tail.set_next(new_node) # (last node in chain).next_node = new_node
            # Update the "self.tail" to point to the new node that we just added
            self.tail = new_node

    def remove_tail(self):
        """
        remove the last node in the chain and return its value
        """
        # Check for empty list
        if self.head is None and self.tail is None:
            # return None
            return None
        # Check if there is only one node
        if self.head == self.tail:
            # Store the value of the node that we are going to remove
            value = self.tail.get_value()
            # Remove the node
            # Set head and the tail to None
            self.head = None
            self.tail = None
            # Return the stored value
            return value
        # Otherwise
        else:
            # Store the value of the node that we are going to remove
            value = self.tail.get_value()
            # We need to set the "self.tail" to the second to last node
            # We can only do this by traversing the whole list from beginning to end

            # Starting from the head
            current_node = self.head

            # Keep iterating until the node after "current_node" is the tail
            while current_node.get_next() != self.tail:
                # Keep looping
                current_node = current_node.get_next()

            # At the end of the iteration set "self.tail" to the current_node
            self.tail = current_node
            # Set the new tail's "next_node" to None
            self.tail.set_next(None)
            # Return Value
            return value

    def remove_head(self):
        # Check for empty list
        if self.head is None and self.tail is None:
            # Return None
            return None
        if self.head == self.tail:
            # Store the value of the node that we are going to remove
            value = self.head.get_value()
            # Remove the node
            # Set head and the tail to None
            self.head = None
            self.tail = None
            # Return the stored value
            return value
        else:
            # Store the old head's value
            value = self.head.get_value()
            # Set self.head to old head's next
            self.head = self.head.get_next()
            # Return the value
            return value 


class Stack():
    """Linked list is the underlying storage structure"""
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.remove_tail()


# 3. 
