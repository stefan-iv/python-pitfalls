#!/bin/bash

rm -rf .venv
poetry env use 3.13.5
source .venv/bin/activate
poetry install --no-root -vvvv
