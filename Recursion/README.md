# Principle of Recursion

Recursion is an approach to solving problems using a function that calls itself as a subroutine.<br>

You might wonder how we can implement a function that calls itself. The trick is that each time a recursive function calls itself, it reduces the given problem into subproblems. The recursion call continues until it reaches a point where the subproblem can be solved without further recursion.<br>

A recursive function should have the following properties so that it does not result in an infinite loop:<br>

A simple base case (or cases) — a terminating scenario that does not use recursion to produce an answer.<br>
A set of rules, also known as recurrence relation that reduces all other cases towards the base case.<br>
Note that there could be multiple places where the function may call itself.<br>

## Some basic / small tasks we can do in recursion.

1. Print a string in reverse order. https://leetcode.com/problems/reverse-string/<br>
2. Print a linked list.<br>

## Steps

function {F(X)}F(X), we will:<br>

1. Break the problem down into smaller scopes, <br>
2. Call function {F(x_0)}, F(x_1), ..., F(x_n)F(x) recursively to solve the subproblems of <br>
3. Finally, process the results from the recursive function calls to solve the problem corresponding to {X}X.