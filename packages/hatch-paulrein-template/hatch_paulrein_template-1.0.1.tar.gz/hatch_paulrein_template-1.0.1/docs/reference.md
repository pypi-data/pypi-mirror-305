# Reference documentation for `hatch-paulrein-template`

This part of the project documentation focuses on
an **information-oriented** approach. Use it as a
reference for the technical implementation of the
`hatch-paulrein-template` project code.

## Template plug-ins

At the time of writing, 2024-10-24, hatch documentation does not detail the template system.
According to [the author](https://github.com/pypa/hatch/discussions/143#discussioncomment-2263137),
he is not happy with the template system and has therefore not documented it.

A template-plugin consists of three modules (well, strictly speaking, you could put all of it in one module, but that would get confusing very quickly). 

Many of these methods take either or both of two dictionaries of configuration information. One, the `template_config` contains much of the generic data from hatch central `config.toml` plus information from the commandline (like the new project's name). Plugins can add to this information as they see fit, like adding extra dependencies, or adding extra key/values. (The default template adds the full license text, e.g.)

The second dictionary, `plugin_conf`, is specific to the plugin and contains the key/values (if any) from the plugin table in `config.toml`. (In this specific case, from the `[template.plugins.paulrein-template]` table.)

### Contents of `template_config`

Most of this is taken from the central `config.toml` file. Project and package names are obviously from the invocation of `hatch new`.
The `args` key shows whether the user requested a CLI-application.

````` python
template_config:
{'name': 'Paul Reinerfelt',
 'email': 'Paul.Reinerfelt@gmail.com',
 'licenses': {'headers': True, 'default': ['MIT']},
 'description': '',
 'dependencies': set(),
 'package_name': 'frasse',
 'project_name': 'frasse',
 'project_name_normalized': 'frasse',
 'args': {'cli': False},
 'readme_file_path': 'README.md',
 'package_metadata_file_path': 'src/frasse/__about__.py',
 'license_data': {'MIT': 'MIT License\n'
                         '\n'
                         'Copyright (c) <year> <copyright holders>\n'
                         '\n'
                         'Permission is hereby granted, free of charge, to any '
                         'person obtaining a copy of this software and '
                         'associated documentation files (the "Software"), to '
                         'deal in the Software without restriction, including '
                         'without limitation the rights to use, copy, modify, '
                         'merge, publish, distribute, sublicense, and/or sell '
                         'copies of the Software, and to permit persons to '
                         'whom the Software is furnished to do so, subject to '
                         'the following conditions:\n'
                         '\n'
                         'The above copyright notice and this permission '
                         'notice shall be included in all copies or '
                         'substantial portions of the Software.\n'
                         '\n'
                         'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY '
                         'OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT '
                         'LIMITED TO THE WARRANTIES OF MERCHANTABILITY, '
                         'FITNESS FOR A PARTICULAR PURPOSE AND '
                         'NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR '
                         'COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES '
                         'OR OTHER LIABILITY, WHETHER IN AN ACTION OF '
                         'CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR '
                         'IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER '
                         'DEALINGS IN THE SOFTWARE.\n'},
 'license_expression': 'MIT',
 'license_header': '# SPDX-FileCopyrightText: 2024-present Paul Reinerfelt '
                   '<Paul.Reinerfelt@gmail.com>\n'
                   '#\n'
                   '# SPDX-License-Identifier: MIT\n',
 'license_files': ''}
`````

### Contents of `plugin_conf`

The `plugin_conf` dictionary contains any keys (and their values, of course) that are defined under

`[template.plugins.paulrein-template]`

in the `config.toml` file. (I.e. the plug-in's own configuration, to be interpreted as it wants.)


## Modules

### `hooks.py`

This module just defines a single function, decorated to mark it as a Pluggy-registration function. The name of the function tells Hatch that we want to register a new template plugin.

::: hatch_paulrein_template.hooks
    options:
        heading_level: 4
  
### `plugin.py`

This is the main plugin class, the one we registered in hooks. 

It has to implement [`hatch.template.plugin.interface.TemplateInterface`][hatch.template.plugin.interface.TemplateInterface].
The interface specifies three methods that corresponds to different phases of the template execution:

1. `initialize_config` is called first. It allows the plugin to add extra data to the config before any files use it. 
2. `get_files` usually uses a utility function, `find_template_files`, to list the  sub-classes of [File][hatch.template.File] from a specified module. The central code will then load and instantiate those classes.
3. Lastly, `finalize_files` provides an opportunity to modify the generated contents of files before they are actually written to disk.


::: hatch_paulrein_template.plugin
    options:
        heading_level: 4
  
### `file_templates.py`

These are the actual file templates. 

::: hatch_paulrein_template.file_templates
    options:
        heading_level: 4
  


