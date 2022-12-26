# DSA Notes - Queue and Stack

### Queue -> First-in-first-out Data Structure

The queue is a typical FIFO data structure. The insert operation is also called enqueue and the new element is always added at the end of the queue. The delete operation is called dequeue. You are only allowed to remove the first element.
<br>
In python Queue and be implemented with deque which supports operations like popleft and pop and append, Spoiler alert : this is also useful for implementation of stack. So deque is out all in one solution in Python.<br>

###### Implementation

```
from collections import deque
numbers = deque([1, 2, 3, 4])
```

###### Documentation

https://docs.python.org/3/library/collections.html#collections.deque
https://realpython.com/python-deque/
