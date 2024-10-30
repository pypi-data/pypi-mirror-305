# hatch-paulrein-template

[![PyPI - Version](https://img.shields.io/pypi/v/hatch-paulrein-template.svg)](https://pypi.org/project/hatch-paulrein-template)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-paulrein-template.svg)](https://pypi.org/project/hatch-paulrein-template)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)
- [Changes](#changes)

## Installation

```console
pipx inject hatch hatch-paulrein-template
```

## License

`hatch-paulrein-template` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

## Changes

This plug-in is meant to augment the default Hatch template, not replace it.

The following changes to Hatch default template are made:

`pyproject.toml`
:   Add `versioningit` to build dependencies
:   Change `[tool.hatch.version]` to use `versioningit` 
:   Add `[tool.hatch.env]` and  `[tool.hatch.env.collectors.mkdocs.docs]` tables
:   Add `[tool.hatch.envs.docs]` table with `detached = false` after `[tool.hatch.env.collectors.mkdocs.docs]`
:   Add `[tool.versioningit.next-version]` and `[tool.versioningit.format]` tables
:   Add `[tool.ruff.lint]` and `[tool.ruff.format]` tables

`__about__.py`
:   Modify the `__version__` definition

`cli/__init__.py`
:   make help a normal option and not a group.
:   add click-logging

`mkdocs.yml`
:   Write a better configuration

`docs/`
:   Add stub files for a [Diátaxis](https://diataxis.fr/) based documentation.


