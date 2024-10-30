from typing import Union

from exasol_data_science_utils_python.schema.column import Column
from exasol_data_science_utils_python.schema.column_name import ColumnName
from exasol_data_science_utils_python.schema.column_type import ColumnType


class ColumnBuilder:
    def __init__(self, column: Union[Column, None] = None):
        if column is not None:
            self._name = column.name
            self._type = column.type
        else:
            self._name = None
            self._type = None

    def with_name(self, name: ColumnName) -> "ColumnBuilder":
        self._name = name
        return self

    def with_type(self, type: ColumnType) -> "ColumnBuilder":
        self._type = type
        return self

    def build(self) -> Column:
        column = Column(self._name, self._type)
        return column
