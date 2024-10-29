from __future__ import annotations

import contextlib
from collections.abc import Iterable
from functools import partial
from inspect import getmembers, isfunction, signature

from kfactory import logger

from gdsfactory.typings import Any, Callable, Component


def get_cells(modules: Any, verbose: bool = False) -> dict[str, Callable]:
    """Returns PCells (component functions) from a module or list of modules.

    Args:
        modules: A module or an iterable of modules.
        verbose: If true, prints in case any errors occur.
    """
    # Ensure modules is iterable
    modules = modules if isinstance(modules, Iterable) else [modules]

    cells = {}
    for module in modules:
        for name, member in getmembers(module):
            if not name.startswith("_") and (
                callable(member) and (isfunction(member) or isinstance(member, partial))
            ):
                try:
                    r = signature(
                        member.func if isinstance(member, partial) else member
                    ).return_annotation
                    if r == Component or (
                        isinstance(r, str) and r.endswith("Component")
                    ):
                        cells[name] = member
                except ValueError as e:
                    if verbose:
                        logger.warn(f"error in {name}: {e}")
    return cells


def get_cells_from_dict(cells: dict[str, Callable]) -> dict[str, Callable]:
    """Returns PCells (component functions) from a dictionary.

    Args:
        cells: A dictionary of cells.

    Returns:
        A dictionary of valid component functions.
    """
    valid_cells = {}

    for name, member in cells.items():
        if not name.startswith("_") and (
            callable(member) and (isfunction(member) or isinstance(member, partial))
        ):
            with contextlib.suppress(ValueError):
                func = member.func if isinstance(member, partial) else member
                r = signature(func).return_annotation
                if r == Component or (isinstance(r, str) and r.endswith("Component")):
                    valid_cells[name] = member
    return valid_cells
