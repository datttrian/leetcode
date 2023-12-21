set -xe

python -m isort leetcode --check-only
flake8 leetcode --show-source
pylint leetcode
mypy leetcode

