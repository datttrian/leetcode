# pytest --cache-clear --junitxml=pytest.xml --cov=leetcode leetcode/ | tee pytest-coverage.txt
poetry run pytest --cache-clear --junitxml=pytest.xml --cov=leetcode leetcode/ | tee pytest-coverage.txt
