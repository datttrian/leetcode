set -xe
python -m isort src
docker run -e VALIDATE_EDITORCONFIG=false -e VALIDATE_GITLEAKS=false -e VALIDATE_JSCPD=false -e VALIDATE_JSON=false -e VALIDATE_MARKDOWN=false -e VALIDATE_BASH=false -e RUN_LOCAL=true -v "$(pwd)":/tmp/lint github/super-linter
