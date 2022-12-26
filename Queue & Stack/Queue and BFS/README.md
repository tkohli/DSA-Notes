# Queue and BFS

One common application of Breadth-first Search (BFS) is to find the shortest path from the root node to the target node.
<br>
<br>
![image alt text](1.png)<br>
Here if we do bfs we will get<br>
[A] -> [B,C,D] -> [C,D,E] -> [D,E,F]-> [E,F,G] ...

#### Insights

In the first round, we process the root node. In the second round, we process the nodes next to the root node; in the third round, we process the nodes which are two steps from the root node; so on and so forth.<br>

Similar to tree's level-order traversal, the nodes closer to the root node will be traversed earlier.<br>

If a node X is added to the queue in the kth round, the length of the shortest path between the root node and X is exactly k. That is to say, you are already in the shortest path the first time you find the target node.<br>

The processing order of the nodes is the exact same order as how they were added to the queue, which is First-in-First-out (FIFO). That's why we use a queue in BFS.

## BFS Template Python

```
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
```

## BFS Template Java

```
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    Set<Node> visited;  // store all the nodes that we've visited
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    add root to visited;
    // BFS
    while (queue is not empty) {
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                if (next is not in visited) {
                    add next to queue;
                    add next to visited;
                }
            }
            remove the first node from queue;
        }
        step = step + 1;
    }
    return -1;          // there is no path from root to target
}
```

Note we have seen this same using 2 queues it is just clean to implement.
