import dataclasses
import enum
from numbers import Number
from typing import Any, Tuple, Type

from modelity.loc import Loc


class ErrorCode:
    NONE_REQUIRED = "modelity.NoneRequired"
    INTEGER_REQUIRED = "modelity.IntegerRequired"
    STRING_REQUIRED = "modelity.StringRequired"
    BYTES_REQUIRED = "modelity.BytesRequired"
    FLOAT_REQUIRED = "modelity.FloatRequired"
    BOOLEAN_REQUIRED = "modelity.BooleanRequired"
    ITERABLE_REQUIRED = "modelity.IterableRequired"
    HASHABLE_REQUIRED = "modelity.HashableRequired"
    MAPPING_REQUIRED = "modelity.MappingRequired"
    DATETIME_REQUIRED = "modelity.DatetimeRequired"
    UNKNOWN_DATETIME_FORMAT = "modelity.UnknownDatetimeFormat"
    UNSUPPORTED_TYPE = "modelity.UnsupportedType"
    INVALID_TUPLE_FORMAT = "modelity.InvalidTupleFormat"
    INVALID_ENUM = "modelity.InvalidEnum"
    INVALID_LITERAL = "modelity.InvalidLiteral"
    VALUE_TOO_LOW = "modelity.ValueTooLow"
    VALUE_TOO_HIGH = "modelity.ValueTooHigh"
    VALUE_TOO_SHORT = "modelity.ValueTooShort"
    VALUE_TOO_LONG = "modelity.ValueTooLong"
    REQUIRED_MISSING = "modelity.RequiredMissing"
    VALUE_ERROR = "modelity.ValueError"
    TYPE_ERROR = "modelity.TypeError"
    UNICODE_DECODE_ERROR = "modelity.UnicodeDecodeError"


@dataclasses.dataclass
class Error:
    """Object describing error."""

    #: Location of the error.
    loc: Loc

    #: Error code.
    code: str

    #: Optional error data, with format depending on the :attr:`code`.
    data: dict = dataclasses.field(default_factory=dict)

    @classmethod
    def create(cls, loc: Loc, code: str, **data: Any) -> "Error":
        return cls(loc, code, data)

    @classmethod
    def create_unsupported_type(cls, loc: Loc, supported_types: Tuple[Type]) -> "Error":
        return cls.create(loc, ErrorCode.UNSUPPORTED_TYPE, supported_types=supported_types)

    @classmethod
    def create_invalid_tuple_format(cls, loc: Loc, expected_format: Tuple[Type]) -> "Error":
        return cls.create(loc, ErrorCode.INVALID_TUPLE_FORMAT, expected_format=expected_format)


class ErrorFactory:
    """Factory class for making errors that can be reported by built-in types."""

    @staticmethod
    def create(loc: Loc, code: str, **data: Any) -> Error:
        """Generic error factory.

        :param loc:
            Error location.

        :param code:
            Error code.

        :param `**data`:
            Code-specific additional error data.

            Check specific factory methods for description of what parameters
            can be expected here.
        """
        return Error(loc, code, data)

    @classmethod
    def create_invalid_enum(cls, loc: Loc, tp: enum.Enum) -> Error:
        """Create invalid enum value error.

        Used by parser for :class:`enum.Enum` subclasses when it fails to map
        user input to supported list of enum values.

        Additional error data:

        ``supported_values``
            Tuple containing supported enum values.
        """
        return cls.create(loc, ErrorCode.INVALID_ENUM, supported_values=tuple(tp))  # type: ignore

    @classmethod
    def create_invalid_literal(cls, loc: Loc, supported_values: tuple) -> Error:
        """Returned for :class:`typing.Literal` types, when user input does not
        match literal type being used."""
        return cls.create(loc, ErrorCode.INVALID_LITERAL, supported_values=supported_values)

    @classmethod
    def string_required(cls, loc: Loc) -> Error:
        return cls.create(loc, ErrorCode.STRING_REQUIRED)

    @classmethod
    def bytes_required(cls, loc: Loc) -> Error:
        return cls.create(loc, ErrorCode.BYTES_REQUIRED)

    @classmethod
    def mapping_required(cls, loc: Loc) -> Error:
        return cls.create(loc, ErrorCode.MAPPING_REQUIRED)

    @classmethod
    def datetime_required(cls, loc: Loc) -> Error:
        return cls.create(loc, ErrorCode.DATETIME_REQUIRED)

    @classmethod
    def unknown_datetime_format(cls, loc: Loc, supported_formats: Tuple[str]) -> Error:
        return cls.create(loc, ErrorCode.UNKNOWN_DATETIME_FORMAT, supported_formats=supported_formats)

    @classmethod
    def required_missing(cls, loc: Loc) -> Error:
        return cls.create(loc, ErrorCode.REQUIRED_MISSING)

    @classmethod
    def value_error(cls, loc: Loc, message: str) -> Error:
        return cls.create(loc, ErrorCode.VALUE_ERROR, message=message)

    @classmethod
    def type_error(cls, loc: Loc, message: str) -> Error:
        return cls.create(loc, ErrorCode.TYPE_ERROR, message=message)

    @classmethod
    def value_too_low(cls, loc: Loc, min_inclusive: Any = None, min_exclusive: Any = None) -> Error:
        return cls.create(loc, ErrorCode.VALUE_TOO_LOW, min_inclusive=min_inclusive, min_exclusive=min_exclusive)

    @classmethod
    def value_too_high(cls, loc: Loc, max_inclusive: Any = None, max_exclusive: Any = None) -> Error:
        return cls.create(loc, ErrorCode.VALUE_TOO_HIGH, max_inclusive=max_inclusive, max_exclusive=max_exclusive)

    @classmethod
    def value_too_short(cls, loc: Loc, min_length: int) -> Error:
        return cls.create(loc, ErrorCode.VALUE_TOO_SHORT, min_length=min_length)

    @classmethod
    def value_too_long(cls, loc: Loc, max_length: int) -> Error:
        return cls.create(loc, ErrorCode.VALUE_TOO_LONG, max_length=max_length)

    @classmethod
    def unicode_decode_error(cls, loc: Loc, encoding: str) -> Error:
        return cls.create(loc, ErrorCode.UNICODE_DECODE_ERROR, encoding=encoding)
