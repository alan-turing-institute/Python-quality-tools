# VS Code Python Workspace Config

## REG Handbook

For more info on this setup, plus tips and tricks on using VS Code for Python, see this [WIP page in the REG handbook](https://github.com/alan-turing-institute/REG-handbook/blob/how-tos/python/content/docs/how_tos/python.md) (TODO: Change this link when PR merged)

## Extensions

This VS Code config relies on having the following extensions installed:

- [Python (pre-release)](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - adds core functionality for linting/navigating/debugging/etc.
- [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) - auto-generate template docstrings
- [Black formatter (pre-release)](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) - auto-format code with `black`
- [isort (pre-release)](https://marketplace.visualstudio.com/items?itemName=ms-python.isort) - auto-format code with `isort`

NB: The `black` and `isort` pre-release packages are currently designed to work with the Python pre-release version. This is likely to be consolidated/improved in the future.

Generally I use the settings across all projects so have it in my User settings rather than Workspace settings (i.e. in `~/Library/Application Support/Code/User/settings.json` rather than `<PROJECT_ROOT>/.vscode/settings.json`).

Other useful extensions for Python include:

- [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) - improved auto-completion/code suggestions
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent) - improves editor behaviour for matching indentation across lines
- [Python Type Hint](https://marketplace.visualstudio.com/items?itemName=njqdev.vscode-python-typehint) - helps with completing type-hints
