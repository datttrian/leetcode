set -xe
python -m isort leetcode
docker run -e VALIDATE_EDITORCONFIG=false -e VALIDATE_GITLEAKS=false -e VALIDATE_JSCPD=false -e VALIDATE_JSON=false -e VALIDATE_MARKDOWN=false -e RUN_LOCAL=true -v "$(pwd)":/tmp/lint github/super-linter
pytest leetcode
