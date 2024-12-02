# mdformat-tables

[![Build Status][ci-badge]][ci-link]
[![PyPI version][pypi-badge]][pypi-link]

An [mdformat](https://github.com/hukkin/mdformat) plugin for rendering tables.

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

[ci-badge]: https://github.com/hukkin/mdformat-tables/actions/workflows/tests.yaml/badge.svg?branch=master
[ci-link]: https://github.com/hukkin/mdformat-tables/actions?query=workflow%3ACI+branch%3Amaster+event%3Apush
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-tables.svg
[pypi-link]: https://pypi.org/project/mdformat-tables
