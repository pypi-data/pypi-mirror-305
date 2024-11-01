"""Utility functions concerning data sources."""

from __future__ import annotations

from typing import Final, Union, cast

import numpy as np
import pandas as pd

from bitfount.data.types import DataPathModifiers

# FileSystemIterableSource metadata columns
ORIGINAL_FILENAME_METADATA_COLUMN: Final[str] = "_original_filename"
LAST_MODIFIED_METADATA_COLUMN: Final[str] = "_last_modified"
FILE_SYSTEM_ITERABLE_METADATA_COLUMNS: Final[tuple[str, ...]] = (
    ORIGINAL_FILENAME_METADATA_COLUMN,
    LAST_MODIFIED_METADATA_COLUMN,
)


def _modify_column(
    column: Union[np.ndarray, pd.Series],
    modifier_dict: DataPathModifiers,
) -> Union[np.ndarray, pd.Series]:
    """Modify the given column.

    Args:
        column: The column you are operating on.
        modifier_dict: A dictionary with the key as the
            prefix/suffix and the value to be prefixed/suffixed.
    """
    # Get the modifier dictionary:
    for modifier_type, modifier_string in modifier_dict.items():
        # TypedDicts mark values as object() so have to reassure mypy
        modifier_string = cast(str, modifier_string)

        if modifier_type == "prefix":
            column = modifier_string + column.astype(str)

        elif modifier_type == "suffix":
            column = column.astype(str) + modifier_string
    return column


def _modify_file_paths(
    data: pd.DataFrame, modifiers: dict[str, DataPathModifiers]
) -> None:
    """Modifies image file paths if provided.

    Args:
        data: The dataframe to modify.
        modifiers: A dictionary with the column name and
            prefix and/or suffix to modify file path.
    """
    for column_name in modifiers:
        # Get the modifier dictionary:
        modifier_dict = modifiers[column_name]
        data[column_name] = _modify_column(data[column_name], modifier_dict)
