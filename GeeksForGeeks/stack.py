class stack:
    def __init__(self):
        self._stack = []

    def push(self, x):
        self._stack.insert(0, x)
        print(self._stack)

    def peek(self):
        if len(self._stack) == 0:
            return None

        return self._stack[0]

    def pop(self):
        retVal = None
        
        if len(self._stack) > 0:
            retVal = self._stack.pop(0)
        
        return retVal

class queue:
    def __init__(self):
        self._queue = []
    
    def enqueue(self, x):
        self._queue.append(x)
        print(self._queue)
    
    def dequeue(self):
        retVal = None

        if len(self._queue) > 0:
            retVal = self._queue.pop(0)

        print(self._queue)

        return retVal

    
