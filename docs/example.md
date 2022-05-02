# Example of converting C file to Python script using C2Py

Assume we have simple "hello world" example. In Python it would be just one line:

```py
print("Hello, world!")
```

and in C it would be much longer, like:

```c
#include <stdio.h>

int main(void) {
    printf("Hello, world!\n");
    return 0;
}
```

To make things easier and keep some order in generated files, the result Python script should look like this:

```py
import sys


def main() -> int:
    print("Hello, world!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

Writing Python code in this way is recomended if it is intended for script use only (like C is). Similar example is on [Python docs page](https://docs.python.org/3/library/__main__.html#idiomatic-usage), where is explained, why to use `if __name__ == '__main__'` code block.
