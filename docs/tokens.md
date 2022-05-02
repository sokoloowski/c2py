# Tokens in C

Basing on [educative.io](https://www.educative.io/edpresso/what-are-tokens-in-the-c-language), in the C language, the following 6 types of tokens are available:

1. Keywords
2. Identifiers
3. Constants
4. Operators
5. Special Characters
6. Strings

## Keywords

Keywords are words whose meaning has already been defined by the computer - they are pre-defined words in the C compiler. Each keyword is meant to perform a specific function in a C program. Keywords are case sensitive and are written in lower case. The C language has 32 keywords, they are:

<style>table:nth-of-type(1) thead { display: none; }</style>

|            |            |            |          |
| :--------: | :--------: | :--------: | :------: |
|   `auto`   |  `break`   |   `case`   |  `char`  |
|  `const`   | `continue` | `default`  |   `do`   |
|  `double`  |   `else`   |   `enum`   | `extern` |
|  `float`   |   `for`    |   `goto`   |   `if`   |
|   `int`    |   `long`   | `register` | `return` |
|  `short`   |  `signed`  |  `sizeof`  | `static` |
|  `struct`  |  `switch`  | `typedef`  | `union`  |
| `unsigned` |   `void`   | `volatile` | `while`  |

For list of keywords in C check [C language reference](https://en.cppreference.com/w/c/keyword)

## Identifiers

Each program element in a C program is called an identifier. An identifier is a variable that holds a value and stores it in the memory.

### Rules for declaring identifiers

- The identifier should consist of alphabets from `a` to `z` and `A` to `Z`.
- It may contain numerical values from `0` to `9`.
- It may contain the underscore value.
- The starting character of an identifier must always be a letter.

Example: variables, functions, labels, etc.

### Regular expresion for identifiers

```regexp
^[a-zA-Z][a-zA-Z0-9_]*$
```

## Constants

A constant is a fixed value that cannot be altered during the execution of a program. C constants can be classified into two categories, which can be divided into the following types:

1. primary constants
   - numeric
     - integer
     - float
   - character
      - single character
      - string
   - logical
2. secondary constants
   - array
   - structure
   - union
   - pointer
   - enum

## Operators

Operators are symbols that provide instructions for the performance of various mathematical and logical operations. Operators are tools that can alter data and variable values.

Operators are classified into the following eight types:

1. Arithmetic Operators
2. Relational Operators
3. Logical Operators
4. Increment/Decrement Operators
5. Assignment Operator
6. Bitwise Operators
7. Conditional Operators
8. Special Operators

For list of operators in C check [C language reference](https://en.cppreference.com/w/c/language/operator_precedence).

## Special characters

All the characters other than `a` to `z`, `A` to `Z`, and `0` to `9` are special characters. Example: `{`,`}`,`[`,`]`,`(`,`)`.

A character data type consumes 8-bits of memory, which means that one can store anything in a character whose ASCII value lies between -127 and 127. Thus, it can hold any of the 256 different possible values.

### Regular expresion for special characters

```regexp
[^a-zA-Z0-9]
```

## Strings

A string is an array of characters ended with a null character (`\0`). This null character indicates that string has ended. Strings are always enclosed with double quotes (`""`).

For example:

```c
char string[20] = {'s', 't', 'u', 'd', 'y', '\0'};
char string[20] = "study";
char string[] = "study";
```
