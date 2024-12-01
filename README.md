# mdformat-tables

[![Build Status][ci-badge]][ci-link]
[![codecov.io][cov-badge]][cov-link]
[![PyPI version][pypi-badge]][pypi-link]

An [mdformat](https://github.com/executablebooks/mdformat) plugin for rendering tables.

For example, converting:

```markdown
a | b | c
:- | -: | :-:
1 | 2 | 3
xxxxxx | yyyyyy | zzzzzz
```

to:

```markdown
| a      |      b |   c    |
| :----- | -----: | :----: |
| 1      |      2 |   3    |
| xxxxxx | yyyyyy | zzzzzz |
```

For further examples, see tests/fixtures.md in the repository.

## Development

This package utilises [flit](https://flit.readthedocs.io) as the build engine, and [tox](https://tox.readthedocs.io) for test automation.

To install these development dependencies:

```bash
pip install flit tox
```

To run the tests:

```bash
tox
```

To run the code formatting and style checks:

```bash
tox -e py311-pre-commit
```

or directly

```bash
pip install pre-commit
pre-commit run --all
```

To run the pre-commit hook test:

```bash
tox -e py311-hook
```

## Publish to PyPi

Either use flit directly:

```bash
flit publish
```

or trigger the GitHub Action job, by creating a release with a tag equal to the version, e.g. `v0.0.1`.

Note, this requires generating an API key on PyPi and adding it to the repository `Settings/Secrets`, under the name `PYPI_KEY`.

[ci-badge]: https://github.com/executablebooks/mdformat-tables/actions/workflows/tests.yml/badge.svg?branch=master
[ci-link]: https://github.com/executablebooks/mdformat/actions?query=workflow%3ACI+branch%3Amaster+event%3Apush
[cov-badge]: https://codecov.io/gh/executablebooks/mdformat-tables/branch/master/graph/badge.svg
[cov-link]: https://codecov.io/gh/executablebooks/mdformat-tables
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-tables.svg
[pypi-link]: https://pypi.org/project/mdformat-tables
