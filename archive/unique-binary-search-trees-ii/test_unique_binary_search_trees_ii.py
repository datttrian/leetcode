from typing import List, Union

import pytest
from unique_binary_search_trees_ii import Solution, TreeNode


@pytest.mark.parametrize(
    ('n', 'expected'),
    [
        (0, []),
        (1, [TreeNode(1)]),
        (2, [TreeNode(1, None, TreeNode(2)), TreeNode(2, TreeNode(1))]),
        # (
        #     3,
        #     [
        #         TreeNode(1, None, TreeNode(2, None, TreeNode(3))),
        #         TreeNode(1, None, TreeNode(3, TreeNode(2))),
        #         TreeNode(2, TreeNode(1), TreeNode(3)),
        #         TreeNode(3, TreeNode(1, None, TreeNode(2))),
        #     ],
        # ),
        # Add more test cases as needed
    ],
)
def test_generateTrees(n: int, expected: List[TreeNode]):
    solution = Solution()
    result = solution.generateTrees(n)

    assert len(result) == len(expected)

    # Compare each tree structure
    for res_tree, exp_tree in zip(result, expected):
        assert compare_trees(res_tree, exp_tree)


def compare_trees(
    tree1: Union[TreeNode, None],
    tree2: Union[TreeNode, None],
) -> bool:
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False

    return (
        tree1.val == tree2.val
        and compare_trees(tree1.left, tree2.left)
        and compare_trees(tree1.right, tree2.right)
    )
