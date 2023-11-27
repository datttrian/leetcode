set -xe

poetry run isort leetcode/roman-to-integer/*.py --check-only
poetry run flake8 leetcode/roman-to-integer/*.py --show-source
poetry run pylint leetcode/roman-to-integer/*.py
poetry run mypy leetcode/roman-to-integer/*.py
