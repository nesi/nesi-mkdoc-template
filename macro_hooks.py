"""
Allows injection of variables into macro stage of rendering.
This allows for arbitrary use of variables in ARTICLES, (e.g. `docs/.md`).
As opposed to `mkdocs_hooks.py` which works only in template step, (e.g. `overrides/*.html`).
If this is confusing, ask Cal to explain.
"""


def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """
