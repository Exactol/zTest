# zTest
A input() testing library for Python 3

# Importing
```python
import zTest
```
or
```python
from zTest import zTest
```
# Usage
Just call zTest with a list of strings in the order you want them to be called.
```python
zTest(["input 1", "input 2", ...])
```
# How it works
zTest overwrites python's built-in method for input with a method that returns a string from the dictionary provided when calling the test.
