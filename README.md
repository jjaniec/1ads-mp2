# 1ADS-MP2 - *"Just Get 10"*

## Synopsis

All the code present in this repository was written in the context of a project
evaluation that was submitted to SUPINFO students asking them to write a clone
of Veewo's "Just Get 10" in Python, with the main goal to get used to create GUI
with Pygame.  
Being a group project, it involved three persons:
 * DOURNEAU Pierre-Louis ([@pldiiw][pldiiw])
 * JANIEC Joffrey ([@jjaniec][jjaniec])
 * POISSON Mathias ([@mathiaspoisson][mp])

## Code Guidelines

### PEP-8

The *de facto* coding conventions to follow in Python are the ones defined in
the [PEP-8][pep8]. To ensure this guideline is followed, we used the [pylint
linting tool][pylint].

### Function Annotations

We agreed to use the so-called [function annotations][fa]. They help sketch the
flow of the code when implementing a new feature and detecting bugs ahead of run
time.

## Project Hierarchy

All games source files can be found in the `src` directory.  
Tests are under the `test` directory.

## Installation

Requires Python 3.5+.

Clone the repository:

    git clone https://github.com/pldiiw/1ads-mp2.git

## Tests

There's a test suite inside the `test` directory.

To run them, just execute the test script:

    ./run_tests.bash

It requires mypy. If don't have it, just run:

    sudo pip3 install mypy-lang

## LICENSE

This project is under the Unlicense. See LICENSE file for more information.  
EXCEPTING the version tagged as v1.0.0, which is licensed to SUPINFO
International University under the terms of the [FreeBSD License][freebsd].

[freebsd]: https://en.wikipedia.org/wiki/BSD_licenses#2-clause
[pldiiw]: https://github.com/pldiiw
[jjaniec]: https://github.com/jjaniec
[mp]: https://github.com/mathiaspoisson
[pep8]: https://www.python.org/dev/peps/pep-0008
[pylint]: https://www.pylint.org
[fa]: https://www.python.org/dev/peps/pep-3107
