# zTest
A testing library for Python3's input() method

## Importing
```python
import zTest
```
or
```python
from zTest import zTest
```
## Usage
Just call zTest with a list of strings in the order you want them to be called.
```python
zTest(["input 1", "input 2", ...])
```
Optionally it can be called with a boolean value to indicate if you want an exception to be raised when the test cases have completed
```python
zTest(["input 1", "input 2", ..."], True)
```

## How it works
zTest overwrites python's built-in method for input with a method that returns a string from the dictionary provided when calling the test. When the tests complete, it restores the input function to the built-in version and either returns input to the user, or raises an exception.
