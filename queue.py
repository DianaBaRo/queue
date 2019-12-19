# queue is an abstract data type
# Basic operations: enqueue() and dequeue(), peek()
# FIFO structure, first in first out
# Can be implemented with dynamic arrays as well as with linked lists.
# Important when implementing BFS algorithms for graphs
# Applications:
    # When a resource is shared with several consumers, like CPU scheduling
   # When data is tranferred asynchronously between two processes, like IO buffers
   # Operational research apps or stochastic models

#Stack application:
  # back button in web browsers
  # undo operation in softwares( Photoshop or Paint)
  # Stack memory stores local variables and function calls

#FIFO

class Queue:
    
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        data = self.queue[0]
        return data

    def sizeQueue(self):
        return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.sizeQueue())

print("Popped ", queue.dequeue())
print("Popped ", queue.dequeue())
print(queue.sizeQueue())
print("Peeked: ", queue.peek())
print(queue.sizeQueue())
