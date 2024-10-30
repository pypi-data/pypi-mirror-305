# hooks.py
from hatchling.plugin import hookimpl

from hatch_paulrein_template.__about__ import __version__

from .plugin import PaulReinTemplate


@hookimpl
def hatch_register_template() -> type[PaulReinTemplate]:
    """The Pluggy registration hook.

    Returns:
        The class of our main plugin class.
    """
    print(f"Running version {__version__} of {PaulReinTemplate.PLUGIN_NAME}!")
    return PaulReinTemplate
