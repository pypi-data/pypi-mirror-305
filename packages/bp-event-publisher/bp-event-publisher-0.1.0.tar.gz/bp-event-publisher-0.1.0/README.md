This is a placeholder project for avoiding dependency confusion attacks.

1. Create a .pypirc on your home folder with pypi auth token
2. Rename the project in setup.py
3. Run `python setup.py sdist`
4. Run `pipx run twine upload dist/*`