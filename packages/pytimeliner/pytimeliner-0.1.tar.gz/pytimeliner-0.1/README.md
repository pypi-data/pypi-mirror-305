<class>
<h2><p align="center">
  PyTimeliner
</p></h2>

<p align="center"><a href="https://github.com/nowte/PyTimeliner/issues"><img alt="Issues open" src="https://img.shields.io/github/issues-raw/nowte/PyTimeliner?style=for-the-badge" height="20"/></a>
<a href="https://github.com/nowte/PyTimeliner/"><img alt="Last commit" src="https://img.shields.io/github/last-commit/nowte/PyTimeliner?style=for-the-badge" height="20"/></a>
<a href="https://github.com/nowte/PyTimeliner/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/nowte/PyTimeliner?style=for-the-badge" height="20"/></a>
<a href="https://github.com/nowte/PyTimeliner/releases"><img alt="Latest version" src="https://img.shields.io/github/v/tag/nowte/PyTimeliner?label=Latest%20Version&style=for-the-badge" height="20"/></a>
<a href="https://pypi.org/project/PyTimeliner/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/PyTimeliner?style=for-the-badge" height="20"/></a>
<a href="https://pypi.org/project/PyTimeliner/"><img alt="Downloads" src="https://img.shields.io/pypi/dm/PyTimeliner?style=for-the-badge" height="20"/></a></p>

**PyTimeliner** is a Python package for organizing events and dates in a chronological timeline with multilingual support. This package enables you to add events in various languages and create a well-ordered timeline.

## Features

- Add and display events in different languages
- Automatically organizes events in chronological order
- Useful for developers working on event-based projects

## Installation

### Using `setup.py`

First, clone the repository and navigate to the project directory. Then, install the package with:

```bash
pip install -e .
```

# Using `requirements.txt`
Alternatively, if you want to install dependencies separately, you can create a requirements.txt file. Install the package dependencies with:
```bash
pip install -r requirements.txt
```

This package uses googletrans for translation support. If you are using requirements.txt, make sure it contains:
```bash
googletrans==4.0.0-rc1
```

## Usage
Using PyTimeliner, you can easily add events and display them in a timeline format.

### Example Usage
```bash
from pytimeliner.timeliner import Timeliner

# English timeline
timeline = Timeliner(language='en')
timeline.add_event("2024-01-01", "New Year")
timeline.add_event("2024-12-25", "Christmas")
timeline.display_timeline()

# Spanish timeline
timeline_es = Timeliner(language='es')
timeline_es.add_event("2024-01-01", "New Year")
timeline_es.add_event("2024-12-25", "Christmas")
timeline_es.display_timeline()
```

## Output
```bash
English:

2024-01-01: New Year
2024-12-25: Christmas
```
```bash
Spanish:

2024-01-01: Año Nuevo
2024-12-25: Navidad
```

## Running Tests
To run tests, use the tests folder which contains test files:

```bash
python -m unittest discover -s tests
```

## Contributing
If you want to contribute, feel free to open an issue or submit a pull request. All contributions are welcome!