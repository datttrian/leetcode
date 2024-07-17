from collections import defaultdict, deque
from typing import Optional


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
        graph: dict[int, list[tuple[int, str]]] = defaultdict(list)

        queue: deque[Optional[TreeNode]] = deque([root])
        while queue:
            node = queue.popleft()

            if node is not None:
                if node.left:
                    graph[node.left.val].append((node.val, "U"))
                    graph[node.val].append((node.left.val, "L"))
                    queue.append(node.left)
                if node.right:
                    graph[node.right.val].append((node.val, "U"))
                    graph[node.val].append((node.right.val, "R"))
                    queue.append(node.right)

        seen: set[int] = set()

        search_queue: deque[tuple[int, str]] = deque([(startValue, "")])
        while search_queue:
            cur_val, cur_path = search_queue.popleft()

            if cur_val in seen:
                continue

            seen.add(cur_val)

            if cur_val == destValue:
                return cur_path

            for child, direction in graph[cur_val]:
                if child not in seen:
                    search_queue.append((child, cur_path + direction))

        return ""
