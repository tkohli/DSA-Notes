"""
https://leetcode.com/problems/open-the-lock/description/

Basic idea is to start from 0000 we can goto 1000,0100,0010,0001,9000,0900,0090,0009
and then from each point goto these similar values need to keep track of visited and blocked values
"""
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbor(code):
            for i in range(4):
                x = int(code[i])
                for diff in (-1, 1):
                    tmp = (x+diff+10) % 10
                    yield code[:i]+str(tmp)+code[i+1:]

        # so it takes O(1) time to search, would also work as visited set
        deadSet = set(deadends)
        if "0000" in deadSet:
            return -1
        queue = deque(["0000"])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return steps
                # to generate all neighbor we could use tmp list or generator \
                for nei in neighbor(cur):
                    if nei not in deadSet:
                        deadSet.add(nei)
                        queue.append(nei)
            steps += 1
        return -1
