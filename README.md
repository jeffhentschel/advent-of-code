# Advent of Code

[Advent of code] solutions, done in python.

- [Usage](#usage)
- [Setup](#setup)

## Usage

Run today's code:

```sh
./run a
```

Run another day's code:

```sh
python -m y2022.d01.a
```

## Setup

Create a `.session` file with your session cookie:

```txt
session=123
```

Each day, you can run the following setup command.

```sh
./setup.sh
```

You can also setup another day's code.

```sh
./setup.sh 2022 06 -o
```

> ⚠️ The `-o` option will overwrite any existing code. Please use with caution.

This will create a new folder for the day with a starting template and download the day's input.

[Advent of code]: https://adventofcode.com
