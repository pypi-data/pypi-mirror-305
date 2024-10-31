from collections.abc import Mapping, Sequence
from typing import Annotated, Generic, Literal, TypeAlias, TypeVar

from lionabc import Container, Observable, Ordering
from lionfuncs import LN_UNDEFINED, LionUndefinedType
from pydantic import Field

# TypeVar for generic type constraints
T = TypeVar("T", bound=Observable)

# Basic ID type
LnID: TypeAlias = Annotated[str, Field(description="Lion ID string ('ln...')")]


class IDTypes(Generic[T]):
    """
    Generic type definitions for different ID usage contexts.

    TypeVars:
        T: Type parameter constrained to Observable types
    """

    # For functions that accept either ID or item
    Ref: TypeAlias = LnID | T  # type: ignore

    # For functions requiring just the ID
    IDOnly: TypeAlias = LnID

    # For functions requiring Observable object
    ItemOnly = T  # type: ignore

    # For collections
    IDSeq: TypeAlias = Sequence[LnID] | Ordering[LnID]
    ItemSeq: TypeAlias = (  # type: ignore
        Sequence[T] | Mapping[LnID, T] | Container[LnID | T]
    )
    RefSeq: TypeAlias = IDSeq | ItemSeq

    # For system-level interactions
    SenderRecipient: TypeAlias = (  # type: ignore
        LnID | T | Literal["system", "user", "N/A", "assistant"]
    )

    # example: IDTypes[UserClass].Ref


__all__ = ["LnID", "IDTypes", "LN_UNDEFINED", "LionUndefinedType"]
