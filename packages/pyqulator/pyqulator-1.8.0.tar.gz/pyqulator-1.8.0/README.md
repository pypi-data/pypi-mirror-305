# Pyqulator

![Static Badge](https://img.shields.io/badge/License-GNU_GPL_v3-blue)
![Static Badge](https://img.shields.io/badge/PyQt-6-green)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A fully functional calculator written in PyQt 6 and using SymPy for calculations. Qt Designer and Qt Linguist were used to create the interface.

## Features
+ Simple and lightweight
+ Standard, engineer and paper modes
+ Unit converter
+ Save journal as .txt
+ Move line up/down in paper mode
+ Available in 3 languages
+ Remember mode, window size and user settings for next launch

## Installation
### From PyPi
```
pip install pyqulator
```
### From source
```
git clone https://github.com/limafresh/pyqulator.git
cd pyqulator
pip install .
```

## Usage
```
pyqulator
```

## Create shortcut in application menu (Linux only)
```
pyqulator_create_shortcut
```
If the installation was for all users:
```
sudo pyqulator_create_shortcut
```

## Screenshots
*Standard mode*

![Screenshot](https://raw.githubusercontent.com/limafresh/pyqulator/main/screenshots/screenshot1.png)

*Engineer mode*

![Screenshot](https://raw.githubusercontent.com/limafresh/pyqulator/main/screenshots/screenshot2.png)

*Paper mode*

![Screenshot](https://raw.githubusercontent.com/limafresh/pyqulator/main/screenshots/screenshot3.png)

*Unit converter*

![Screenshot](https://raw.githubusercontent.com/limafresh/pyqulator/main/screenshots/screenshot4.png)
