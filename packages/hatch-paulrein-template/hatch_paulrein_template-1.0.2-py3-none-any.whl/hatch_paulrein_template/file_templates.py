# file_templates.py
import pprint

from hatch.template import File
from hatch.utils.fs import Path


class MkdocsYml(File):
    """
    Create a `mkdocs.yml` file.
    """

    TEMPLATE = """\
site_name: {project_name} Docs

theme: {theme}

plugins: 
  - search
  - mkdocstrings:
      handlers:
        python:
          docstring_section_style: list
          show_inheritance_diagram: true
          show_symbol_type_heading: true
          show_signature_annotations: true
          separate_signature: true
          docstring_style: google
          paths: [src]
  - print-site

markdown_extensions:
  - toc
  - def_list
  - footnotes
  - sane_lists
  - admonition
  - markdown_sub_sup
  - mkdocs-click 
  - markdown_checklist.extension
  - mdx_math

nav:
  - Home: 'index.md'
  - tutorials.md
  - how-to-guides.md
  - reference.md
  - explanation.md
"""

    def __init__(self, template_config: dict, plugin_config: dict) -> None:
        # defaults
        theme = "readthedocs"

        if "theme" in plugin_config:
            theme = plugin_config["theme"]
        super().__init__(
            Path("mkdocs.yml"), self.TEMPLATE.format(theme=theme, **template_config)
        )


class IndexMd(File):
    """
    Create an `docs/index.md` file.
    """

    TEMPLATE = """\
# {project_name}
{proj_description}

## Table Of Contents

The documentation follows the best practice for
project documentation as described by Daniele Procida
in the [Diátaxis documentation framework](https://diataxis.fr/)
and consists of four separate parts:

1. [Tutorials](tutorials.md)
2. [How-To Guides](how-to-guides.md)
3. [Reference](reference.md)
4. [Explanation](explanation.md)

Quickly find what you're looking for depending on
your use case by looking at the different pages.
"""

    def __init__(self, template_config: dict, plugin_config: dict) -> None:
        # defaults
        proj_description = "This is a super cool project."

        if template_config["description"] != "":
            proj_description = template_config["description"]
        super().__init__(
            Path("docs/index.md"),
            self.TEMPLATE.format(proj_description=proj_description, **template_config),
        )


class TutorialsMD(File):
    """
    Create a `docs/tutorials.md` file.
    """

    TEMPLATE = """
This part of the project documentation focuses on a
**learning-oriented** approach. You'll learn how to
get started with the code in this project.

> **Note:** Expand this section by considering the
> following points:

- Help newcomers with getting started
- Teach readers about your library by making them
    write code
- Inspire confidence through examples that work for
    everyone, repeatably
- Give readers an immediate sense of achievement
- Show concrete examples, no abstractions
- Provide the minimum necessary explanation
- Avoid any distractions
"""

    def __init__(self, template_config: dict, plugin_config: dict) -> None:
        # defaults

        super().__init__(
            Path("docs/tutorials.md"),
            self.TEMPLATE.format(**template_config),
        )


class HowToGuidesMD(File):
    """
    Create a `docs/how-to-guides.md` file.
    """

    TEMPLATE = """
This part of the project documentation focuses on a
**problem-oriented** approach. You'll tackle common
tasks that you might have, with the help of the code
provided in this project.
"""

    def __init__(self, template_config: dict, plugin_config: dict) -> None:
        # defaults

        super().__init__(
            Path("docs/how-to-guides.md"),
            self.TEMPLATE.format(**template_config),
        )


class ReferenceMD(File):
    """
    Create a `docs/reference.md` file.
    """

    TEMPLATE = """
# Reference documentation for `{project_name}`

This part of the project documentation focuses on
an **information-oriented** approach. Use it as a
reference for the technical implementation of the
`{project_name}` project code.
"""

    def __init__(self, template_config: dict, plugin_config: dict) -> None:
        # defaults

        super().__init__(
            Path("docs/reference.md"),
            self.TEMPLATE.format(**template_config),
        )


class ExplanationMD(File):
    """
    Create a `docs/explanation.md` file.
    """

    TEMPLATE = """
This part of the project documentation focuses on an
**understanding-oriented** approach. You'll get a
chance to read about the background of the project,
as well as reasoning about how it was implemented.

> **Note:** Expand this section by considering the
> following points:

- Give context and background on your library
- Explain why you created it
- Provide multiple examples and approaches of how
    to work with it
- Help the reader make connections
- Avoid writing instructions or technical descriptions
    here
"""

    def __init__(self, template_config: dict, plugin_config: dict) -> None:
        # defaults

        super().__init__(
            Path("docs/explanation.md"),
            self.TEMPLATE.format(**template_config),
        )


class Nisse(File):
    """
    Create a `config_values.md` file.

    This is a debugging aid, dumping the contents of `template_config` and `plugin_config`
    for inspection after the creation of the new project.
    """

    TEMPLATE = """\
Just a file to output the config values.

`template_config`:
{templateconfig}

`plugin_config`:
{pluginconfig}

"""

    def __init__(self, template_config: dict, plugin_config: dict) -> None:
        # defaults
        template_config_string = pprint.pformat(template_config)
        plugin_config_string = pprint.pformat(plugin_config)

        super().__init__(
            Path("config_values.md"),
            self.TEMPLATE.format(
                templateconfig=template_config_string,
                pluginconfig=plugin_config_string,
                **template_config,
            ),
        )
