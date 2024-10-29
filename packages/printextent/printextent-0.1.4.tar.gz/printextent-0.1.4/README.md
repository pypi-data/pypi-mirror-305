# What is it?

printextent is a Python library for customizing print statements in a different variety of ways.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install printextent.

```bash
pip install printextent
```

## Usage

```python
import printextent

# prints out "Hello World! This is a test sentence!" in the color blue while also being bolded.
printextent.colorPrint("Hello World! This is a test sentence!", "Blue", "Bold")

# prints out "Hello World! This is a test sentence!" in a rainbow pattern.
printextent.colorPrint("Hello World! This is a test sentence!", "Rainbow")

# prints out "Hello World! This is a test sentence!" while under a typewriter effect.
printextent.typewritePrint("Hello World! This is a test sentence!")

```

## License

[MIT](https://choosealicense.com/licenses/mit/)