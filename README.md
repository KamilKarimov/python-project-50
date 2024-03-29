### Hexlet tests and linter status:
[![Actions Status](https://github.com/KamilKarimov/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/KamilKarimov/python-project-50/actions)

### Python CI
[![Python CI](https://github.com/KamilKarimov/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/KamilKarimov/python-project-50/actions/workflows/pyci.yml)

### Codeclimate badges
[![Maintainability](https://api.codeclimate.com/v1/badges/b06b5068f9c1756d9643/maintainability)](https://codeclimate.com/github/KamilKarimov/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b06b5068f9c1756d9643/test_coverage)](https://codeclimate.com/github/KamilKarimov/python-project-50/test_coverage)

# **Gendiff** - compare two json and/or yaml files

## **About**
You can get a comparison of two json/yaml files - different formats can be compared too!


The output type depends on the selected format:
- **stylish** - is selected by default
- **plain**
- **json**

## Help
```bash
gendiff -h

usage: gendiff [-h] [-f [{stylish,plain,json}]] [first_file] [second_file]

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f [{stylish,plain,json}], --format [{stylish,plain,json}]
                        set format of output
```

# Installation

### You can use pip and install package from git:

    pip install --user git+https://github.com/KamilKarimov/python-project-50

### Or you can clone rep from GitHub and install by using following commands:
    git clone https://github.com/KamilKarimov/python-project-50
    cd python-project-50
    make install
    make build
    make package-install

[![asciicast](https://asciinema.org/a/2pDXgDC3pFJWL8ejNBtn1Y9ZS.svg)](https://asciinema.org/a/2pDXgDC3pFJWL8ejNBtn1Y9ZS)
[![asciicast](https://asciinema.org/a/KPpcE5gqVbVhT8bc9tu5LldkJ.svg)](https://asciinema.org/a/KPpcE5gqVbVhT8bc9tu5LldkJ)
[![asciicast](https://asciinema.org/a/3BWtlA9CPJeKo19rDJJkj4P8s.svg)](https://asciinema.org/a/3BWtlA9CPJeKo19rDJJkj4P8s)
[![asciicast](https://asciinema.org/a/ALS2PPGXkZGOfj4N3NvcYZ6eM.svg)](https://asciinema.org/a/ALS2PPGXkZGOfj4N3NvcYZ6eM)
[![asciicast](https://asciinema.org/a/IQqhrPm3v6E691BwP8abrBcxD.svg)](https://asciinema.org/a/IQqhrPm3v6E691BwP8abrBcxD)