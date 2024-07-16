from collections import defaultdict, deque
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        # Initialize an empty graph using a dictionary where each node will map to a list of tuples.

        graph: dict[int, list[tuple[int, str]]] = defaultdict(list)
        
        # Use a deque (double-ended queue) for a breadth-first traversal of the tree starting with the root.
        queue: deque[Optional[TreeNode]] = deque([root])

        # Perform a breadth-first search (BFS) to build the graph representation of the tree.
        while queue:
            # Pop the leftmost node from the queue.
            node = queue.popleft()

            if node is not None:
                # If the node has a left child, add it to the graph and queue.
                if node.left:
                    # Append the parent-child relationship to the graph for both directions.
                    graph[node.left.val].append((node.val, "U"))  # 'U' indicates moving up to the parent.
                    graph[node.val].append((node.left.val, "L"))  # 'L' indicates moving left to the child.
                    queue.append(node.left)

                # If the node has a right child, add it to the graph and queue.
                if node.right:
                    # Append the parent-child relationship to the graph for both directions.
                    graph[node.right.val].append((node.val, "U"))  # 'U' indicates moving up to the parent.
                    graph[node.val].append((node.right.val, "R"))  # 'R' indicates moving right to the child.
                    queue.append(node.right)

        # Use another deque to perform a BFS to find the shortest path from startValue to destValue.
        search_queue: deque[tuple[int, str]] = deque([(startValue, "")])
        
        # Use a set to keep track of visited nodes to avoid revisiting them.
        seen: set[int] = set()

        # Perform BFS to find the shortest path.
        while search_queue:
            # Pop the leftmost element from the search queue.
            cur_val, cur_path = search_queue.popleft()

            # If the current node has already been visited, skip it.
            if cur_val in seen:
                continue

            # Mark the current node as visited.
            seen.add(cur_val)

            # If we have reached the destination node, return the path taken.
            if cur_val == destValue:
                return cur_path

            # For each child of the current node, if it hasn't been visited, add it to the search queue.
            for child, direction in graph[cur_val]:
                if child not in seen:
                    # Append the child node and the updated path (with the direction) to the search queue.
                    search_queue.append((child, cur_path + direction))

        # If no path is found, return an empty string.
        return ""
