import pytest
from simplify_path import Solution


@pytest.mark.parametrize(
    ('path', 'expected'),
    [
        ('/home/', '/home'),
        ('/../', '/'),
        ('/home//foo/', '/home/foo'),
        ('/a/./b/../../c/', '/c'),
        ('/a//b////c/d//././/..', '/a/b/c'),
        ('/', '/'),
        ('/.', '/'),
        ('/..', '/'),
        ('/../../../../../a', '/a'),
    ],
)
def test_simplifyPath(path: str, expected: str):
    solution = Solution()
    result = solution.simplifyPath(path)
    assert result == expected
