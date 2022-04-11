#!/usr/bin/env bash
find  \
    -not \( -path ./.tox -prune \) \
    -not \( -path ./.venv -prune \) \
    -not \( -path ./.git -prune \) \
    -not \( -path ./.vscode -prune \) \
    -regex '\(.*__pycache__.*\)?\(.*\.pyc\)?\(.*\.egg\-info.*\)?\(.*dist.*\)?\(.*build.*\)?' \
    -exec rm -rf {} 2> /dev/null \;