set -xe

poetry run isort leetcode --check-only
poetry run flake8 leetcode --show-source
poetry run pylint leetcode
poetry run mypy leetcode
