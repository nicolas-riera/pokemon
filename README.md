# Pokémon

![pythonversion](https://img.shields.io/badge/python-3.x-blue)
![pygame](https://img.shields.io/badge/pygame-required-green)

## Run and Build from source

### Requirements
- Python **3.x**
- pygame -> ```python -m pip install pygame```
- PyInstaller -> ```python -m pip install pyinstaller```

### Run

From the root folder, run :

```bash
python main.py
```

### Build

To build the game (in .exe for Windows, in .app on MacOs, and as a binary file on Linux), use pyinstaller :

```bash
pyinstaller main.py --onefile --noconsole --icon=assets/img/logo.ico --hidden-import=pygame --name "Pokémon" --add-data="assets;assets" --add-data="data;data"
```

On ```--add-data```, replace ";" by ":" if you are on MacOS or Linux.

# Authors

This project has been realised by [Nicolas](https://github.com/nicolas-riera), [André](https://github.com/andrebtw) and [Hugo](https://github.com/hugo-belaloui).
