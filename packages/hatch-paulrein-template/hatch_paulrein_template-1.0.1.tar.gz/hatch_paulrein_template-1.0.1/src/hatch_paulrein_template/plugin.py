# plugin.py
from hatch.template import File, find_template_files
from hatch.template.plugin.interface import TemplateInterface

from . import file_templates


class PaulReinTemplate(TemplateInterface):
    """
    The main plugin class.
    """

    PLUGIN_NAME = "paulrein-template"  #: The name of the plugin.

    def initialize_config(self, config: dict) -> None:
        """
        Allow modification of the configuration passed to every file for new projects
        before the list of files are determined.

        This is the plug-in's chance to add stuff to the general config dictionary.
        The default plugin, e.g., uses this to add a dependency on `click` for CLI-projects.
        We then further add a dependency on `click-logging` in that same case.

        Args:
            config: Equivalent to the `template_config` dictionary.

        """
        if config["args"]["cli"]:
            config["dependencies"].add("click-logging")

    def get_files(self, config: dict) -> list[File]:
        """
        Add to the list of files for new projects that are written to the file system.

        Args:
            config: Equivalent to the `template_config` dictionary.

        Returns:
            A list of [File][hatch.template.File]-subclasses that should be added to the output.

        """
        return list(find_template_files(file_templates))

    def finalize_files(self, config: dict, files: list) -> None:
        """
        Allow modification of files for new projects before they are written to the file system.

        This is the plugin's opportunity to do final fixes to the contents of files. This is mostly
        to change things that other plugins have added (like the default plugin). We use it adjust
        `__about__.py` to use project metadata instead of a hardcoded value, `cli/__init__.py` to
        change the help option to not use a group and also to add the relevant lines for `click-logging`.
        We also add a lot of tables to the `pyproject.toml` file, as well as modify the version-calculation
        to use `versioningit`.

        Args:
            config: Equivalent to the `template_config` dictionary.
            files:  List of the files that have been added.

        """
        for template_file in files:
            # Modify `__about__.py` to use the metadata version
            if template_file.path.name.endswith("__about__.py"):
                lines = template_file.contents.splitlines()
                lines = lines[
                    :-1
                ]  # Remove the last line (the original `__version__` definition)
                lines.append("from importlib.metadata import version")
                lines.append("")
                lines.append(
                    f'__version__ = version("{config["project_name_normalized"]}")'
                )
                template_file.contents = "\n".join(lines)

            # Modify `cli/__init__.py` to adjust click to not create a group (which implies subcommands) and to use
            # click_logging for verbosity.
            # Note that we don't need to check the `args` key, if the file wasn't generated we simply won't match
            # anything.
            if template_file.path.match("cli/__init__.py"):
                lines = template_file.contents.splitlines()
                # We check line by line because we cannot be sure if the default template has added the licensing text
                # or not, thus screwing up the line numbers.
                for i, line in enumerate(lines):
                    # There is only one import in the default template
                    if line.startswith("import"):
                        lines[i] = (
                            f'import logging\nimport click\nimport click_logging\n\nlogger = logging.getLogger("{config["project_name_normalized"]}")\nclick_logging.basic_config(logger)\n'
                        )
                    if line.startswith("@click.group"):
                        # Make help a normal option and not a group. Also add the verbosity option.
                        lines[i] = (
                            '@click.command(context_settings={"help_option_names": ["-h", "--help"]})\n@click_logging.simple_verbosity_option(logger)'
                        )
                template_file.contents = "\n".join(lines)

            if template_file.path.match("pyproject.toml"):
                lines = template_file.contents.splitlines()
                # We know that the build requirements are on the second line
                lines[1] = 'requires = ["hatchling", "versioningit"]'
                # We check line by line because we need to find the
                # `[tool.hatch.version]` header and modify the next line
                for i, line in enumerate(lines):
                    if line.startswith("[tool.hatch.version]"):
                        lines[i + 1] = 'source = "versioningit"'
                lines.append("""
[tool.hatch.env]
requires = ["hatch-mkdocs"]

[tool.hatch.env.collectors.mkdocs.docs]
path = "mkdocs.yml"

[tool.hatch.envs.docs]
detached = false

[tool.versioningit]
vcs = "hg"

[tool.versioningit.next-version]
method = "smallest"

[tool.versioningit.format]
distance = "{next_version}.dev{distance}+{vcs}{rev}"
# Example formatted version: 1.2.4.dev42+ge174a1f

dirty = "{base_version}+d{build_date:%Y%m%d}"
# Example formatted version: 1.2.3+d20230922

distance-dirty = "{next_version}.dev{distance}+{vcs}{rev}.d{build_date:%Y%m%d}"
# Example formatted version: 1.2.4.dev42+ge174a1f.d20230922

[tool.ruff.lint]
# On top of the defaults (`E4`, E7`, `E9`, and `F`), enable some other categories as well
select = ["E4", "E7", "E9", "F", "I", "ANN", "S", "B", "A", "C4", "EXE", "PIE", "RUF"]
ignore = ["ANN101"]

[tool.ruff.format]
# Enable reformatting of code snippets in docstrings.
docstring-code-format = true
                """)
                template_file.contents = "\n".join(lines)
