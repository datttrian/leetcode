set -xe
poetry run isort leetcode/roman-to-integer/roman_to_integer.py --check-only
poetry run flake8 leetcode/roman-to-integer/roman_to_integer.py --show-source
poetry run pylint leetcode/roman-to-integer/roman_to_integer.py
poetry run mypy leetcode/roman-to-integer/roman_to_integer.py
