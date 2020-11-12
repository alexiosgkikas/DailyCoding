"""
Daily Coding Problem: Problem #648 [Medium]
Good morning! Here's your coding interview problem for today.
This question was asked by Snapchat.
Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.
"""

class Node:
    def __init__(self,value,_next = None,random = None):
        self.value = value
        self._next = _next
        self.random = random
    
    def printList(self):
        if self.value:
            print("value: ",self.value,"random: ",self.random.value)
            if self._next:
                self._next.printList()


def cloneSingleLinkList(head):
    #create copy of every node between the original nodes
    curr = head
    while curr!= None:
        new_node = Node(curr.value)
        new_node._next = curr._next
        curr._next = new_node
        curr = new_node._next
    #connect random pointers to new nodes(new nodes are between originals ,every 2nd node)
    curr = head
    while curr!= None:
        curr._next.random = curr.random._next
        curr = curr._next._next
    # detach connections between duplicate nodes, to seperate lists  
    curr = head
    curr_new = head._next # holds new head for the new list
    while curr._next != None:
        temp = curr._next
        curr._next = curr._next._next
        curr = temp

    return curr_new



    
    
if __name__ == "__main__":
    head = Node(10)
    n1 = Node(20)
    n2 = Node(3)
    n3 = Node(5)
    n4 = Node(6)
    head._next = n1
    head.random = n2
    n1._next = n2
    n1.random = n4
    n2._next = n3
    n2.random = head
    n3._next = n4
    n3.random = n1
    n4.random = n1
    print("======== Original List =========")
    head.printList()
    print("======== Clone Single List =========")
    head2 =cloneSingleLinkList(head)
    head2.printList()



    

