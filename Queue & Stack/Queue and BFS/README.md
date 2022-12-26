# Queue and BFS

One common application of Breadth-first Search (BFS) is to find the shortest path from the root node to the target node.
<br>
<br>
![image alt text](1.png)<br>
Here if we do bfs we will get<br>
[A] -> [B,C,D] -> [C,D,E] -> [D,E,F]-> [E,F,G] ...

#### Insights

In the first round, we process the root node. In the second round, we process the nodes next to the root node; in the third round, we process the nodes which are two steps from the root node; so on and so forth.<br><br>

Similar to tree's level-order traversal, the nodes closer to the root node will be traversed earlier.<br><br>

If a node X is added to the queue in the kth round, the length of the shortest path between the root node and X is exactly k. That is to say, you are already in the shortest path the first time you find the target node.<br><br>

The processing order of the nodes is the exact same order as how they were added to the queue, which is First-in-First-out (FIFO). That's why we use a queue in BFS.
