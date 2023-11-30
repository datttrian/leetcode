# import pytest
# from array_hashing import Solution as ArraySolution
# from linked_list import Solution as LinkedListSolution
# from stack import Solution as StackSolution
# from math_geometry import Solution as MathSolution
# from two_pointers import Solution as TwoPointers


# @pytest.fixture(
#     params=[
#         ArraySolution,
#         StackSolution,
#         LinkedListSolution,
#         MathSolution,
#         TwoPointers,
#     ],
# )
# def solution(request):
#     return request.param()


# @pytest.mark.parametrize(
#     ["input_num", "expected"],
#     [
#         [121, True],
#         [-121, False],
#         [10, False],
#         [0, True],
#         [12321, True],
#         [123456, False],
#     ],
# )
# def test_is_palindrome(
#     solution: object,
#     input_num: int,
#     expected: bool,
# ) -> None:
#     """Test the isPalindrome function from the given Solution class.

#     Args:
#     - solution (object): Instance of the Solution class.
#     - input_num (int): Input number.
#     - expected (bool): Expected result.

#     Returns:
#     - None
#     """
#     assert solution.isPalindrome(input_num) == expected
