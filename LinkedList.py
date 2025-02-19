class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, initialValue=0):
        self.head = Node(initialValue)
        
    def insertEnd(self, val):
        newNode = Node(val)
        curr = self.head
        
        while curr.next is not None:
            curr = curr.next 
        curr.next = newNode
        
    def insertBeginning(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insertAny(self,position, val):
        count = 0
        if not position:
            self.insertBeginning(val)
            return 
        
        curr = self.head
        while curr != None and count < position-1:
            curr = curr.next
            count += 1

        newNode = Node(val)
        temp = curr.next
        curr.next = newNode
        newNode.next = temp

    def __str__(self):
        curr = self.head
        result = ""
        while curr is not None:
            result += str(curr.val) + " --> "
            curr = curr.next
        result += "None"
        return result

    def __len__(self):
        count = 0
        curr = self.head
        while curr is not None:
            curr = curr.next
            count += 1 
        return count
def helper():
    linkedlist = LinkedList(100)
    linkedlist.insertEnd(200)
    linkedlist.insertBeginning(500)
    linkedlist.insertAny(0, 700)
    linkedlist.insertEnd(300)
    print(linkedlist)   
    print(len(linkedlist))
if __name__ == "__main__":
    helper()
