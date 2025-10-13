sed -i 's/python-template/'"$1"'/g' README.md
sed -i 's/python-template/'"$1"'/g' .devcontainer/devcontainer.json
sed -i 's/Python project template/'"$2"'/g' .devcontainer/devcontainer.json
sed -i 's/python-template/'"$1"'/g' pyproject.toml
sed -i 's/Python project template/'"$2"'/g' pyproject.toml
sed -i 's/Python project template/'"$2"'/g' README.md
sed -i 's/This is a python project template that you can use to bootstrap new python project./'"Description here..."'/g' README.md
