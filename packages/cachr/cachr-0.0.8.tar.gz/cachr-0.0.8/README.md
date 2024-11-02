 ```commandline
 ██████╗ █████╗  ██████╗██╗  ██╗██████╗   
██╔════╝██╔══██╗██╔════╝██║  ██║██╔══██╗  
██║     ███████║██║     ███████║██████╔╝  
██║     ██╔══██║██║     ██╔══██║██╔══██╗  
╚██████╗██║  ██║╚██████╗██║  ██║██║  ██║  
 ╚═════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝  
```

# cachr: superfast, composable caching for Python
|         |                                                                                                                                                                                                                               |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Testing | ![Codecov](https://img.shields.io/codecov/c/github/mike-huls/cachr)  |
| Package | [![PyPI Latest Release](https://img.shields.io/pypi/v/cachr.svg)](https://pypi.org/project/cachr/) [![PyPI Downloads](https://img.shields.io/pypi/dm/cachr.svg?label=PyPI%20downloads)](https://pypistats.org/packages/cachr) |
| Meta    | ![GitHub License](https://img.shields.io/github/license/mike-huls/cachr)                                                                                                                                                      |

**cachr** is a Python package that provides superfast, composable caches designed to 
optimize your applications in an easy and intuitive way.
It aims to be the go-to package to use and build caches that make your applications 
superfast, memory-efficient and user-friendly.
```shell
pip install cachr
```

## Table of Contents
- [Main Features](#main-features)
- [Usage Example](#Usage-example)
- [Installation](#Installation)
- [Dependencies](#Dependencies)
- [License](#license)
- [Documentation](#documentation)
- [Development](#development)
- [Contributing to Cachr](#Development)

## Main Features
- 🐍 Pure Python
- 🖌 Easily extendable
- 👨‍🎨 User-friendly

## Usage Example
At the moment there are five caches available for use: 
- LFUCache: Removes the least frequently used item in the cache when it overflows
- LRUCache: A Least Recently Used Cache removes the least recently used item when it overflows
- RandomReplaceCache: randomly expells an item from the cache when it overflows
- TTLCache: A Time-To-Live-cache acts like a LRUCache and also removes an entry from the cache after a certain expiration time
- SlidingWindowCache: Like a TTLCache but it renews the expiration date eacht time an item is requested from the cache.

All caches are added to your code in two ways: by `decorator` or as a regular object.
Decorator:
```python
import time
from cachr import LRUCache


# 1. Decorate your function
@LRUCache(capacity=2)
def add(i, y):
    time.sleep(1)
    print("adding..")
    return i + y


print(add(1, 2))    # <-- takes a second to calculate
print(add(1, 2))    # <-- takes value from cache immediately 
print(add(1, 2))    # <-- takes value from cache immediately 
```

Object:
```python
from cachr import TTLCache

my_cache =  TTLCache(capacity=25, ttl_seconds=60)

def very_expensive_function(number:int) -> int:
    return number * number

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 3, 5, 7, 9, 1, 1, 1, 1]:
    value_from_cache = my_cache.get(i)
    if value_from_cache is not None:
        print(f"Answer for {i} is {value_from_cache}")
        continue
    print(f"calculating expensive function for {i}..")
    my_cache.put(key=i, value=very_expensive_function(number=i))
```



## Installation
```sh
pip install cachr
```
The source code is currently hosted on GitHub at:
https://github.com/mike-huls/cachr

Binary installers for the latest released version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/cachr).

## Dependencies
Cachr has no Python dependencies

## License
[MIT](LICENSE.txt)

## Documentation
🔨 Under construction

## Development
Find the changelog and list of upcoming features [here](doc/CHANGELOG.md).
<br>
**Contributions** are always welcome; feel free to submit bug reports, bug fixes, feature requests, documentation improvements or enhancements!

<hr>

[Go to Top](#table-of-contents)
