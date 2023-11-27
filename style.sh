set -xe

# poetry run isort leetcode --check-only
# poetry run flake8 leetcode --show-source
# poetry run pylint leetcode
# poetry run mypy leetcode

poetry run isort leetcode/integer-to-roman/*.py --check-only
poetry run flake8 leetcode/integer-to-roman/*.py --show-source
poetry run pylint leetcode/integer-to-roman/*.py
poetry run mypy leetcode/integer-to-roman/*.py
