<h1 align="center">  🌸  Blossy CLI  🌸  </h1>

A multiuse utility CLI tool developed using:

- Python
- Typer (CLI building)
- Sly Lex Yacc (parsing)

## 🛠 Features

- [x] Calculate the value of an expression
- [x] Count the number of characters in a text file
- [x] Solve percentage equations
- [x] Generate random numbers
- [x] Stardardize the names of the files in a directory

## 🏁 How to Install

To install the CLI, you'll only need to have Python installed on your machine. Then, run the following command:

```bash
$ python3 -m pip install blossy
```

## ⚙️ Behavior

To have full instructions on how to use the CLI, run the following command:

```bash
$ blossy --help
```

### Calculate

This command will calculate the value of an expression. The following operators are supported:

- (expr)
- \+ expr
- \- expr
- expr ^ expr
- expr * expr
- expr / expr
- expr + expr
- expr - expr

Here's an example of how to use the command:

```bash
$ blossy calc "2*3+4^6"
4102
```

You can also use the `--visualize` flag to see the steps of the calculation, illustrated using postfix notation and a stack:

```bash
$ blossy calc "2*3+4^6" --visualize

$                                                          2 3 * 4 6 ^ +₂ $

> Stack 2

$ 2                                                          3 * 4 6 ^ +₂ $

> Stack 3

$ 2 3                                                          * 4 6 ^ +₂ $

> 2 * 3 = 6

$ 6                                                              4 6 ^ +₂ $

> Stack 4

$ 6 4                                                              6 ^ +₂ $

> Stack 6

$ 6 4 6                                                              ^ +₂ $

> 4^6 = 4096

$ 6 4096                                                               +₂ $

> 6 + 4096 = 4102

$ 4102                                                                    $

> The result is 4102
```

### Count

This command will count the number of characters in a text file. Here's an example of how to use the command:

```bash
$ blossy count file.txt
```
