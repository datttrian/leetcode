import pytest
from unique_binary_search_trees_ii import Solution, TreeNode


@pytest.mark.parametrize(
    ('n', 'expected'),
    [
        (0, []),
        (1, [TreeNode(1)]),
        (2, [TreeNode(1, right=TreeNode(2)), TreeNode(2, left=TreeNode(1))]),
        (
            3,
            [
                TreeNode(1, right=TreeNode(2, right=TreeNode(3))),
                TreeNode(1, right=TreeNode(3, left=TreeNode(2))),
                TreeNode(2, left=TreeNode(1), right=TreeNode(3)),
                TreeNode(3, left=TreeNode(1, right=TreeNode(2))),
                TreeNode(3, left=TreeNode(2, left=TreeNode(1))),
            ],
        ),
    ],
)
def test_generateTrees(n: int, expected: list[TreeNode | None]):
    solution = Solution()
    assert solution.generateTrees(n) == expected
