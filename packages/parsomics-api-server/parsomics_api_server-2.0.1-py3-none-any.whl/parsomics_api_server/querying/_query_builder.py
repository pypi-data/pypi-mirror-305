from operator import eq, le, ge, lt, gt
from dataclasses import dataclass
from typing import Annotated, Any, Callable, ClassVar, Type

from pydantic import AfterValidator, BaseModel, field_validator
from sqlmodel import SQLModel, select

from . import model_registry


def in_model_registry(m: str) -> str:
    if m not in model_registry:
        raise ValueError(
            f"Model {m} targeted for JOIN is not the model registry {model_registry}"
        )
    return m


ModelName = Annotated[str, AfterValidator(in_model_registry)]


def format(model_name: ModelName, property_name: str | None = None):
    model = model_registry[model_name]

    if property_name is None:
        return model
    else:
        return getattr(model, property_name)


class OnClause(BaseModel):
    mdl_l: ModelName
    attr_l: str
    mdl_r: ModelName
    attr_r: str

    def to_arg(self):
        left = format(self.mdl_l, self.attr_l)
        right = format(self.mdl_r, self.attr_r)
        return left == right


class JoinArgs(BaseModel):
    mdl: ModelName
    onclause: OnClause | None = None
    isouter: bool = False
    full: bool = False

    def to_kwarg(self) -> dict:
        # Fetch target class in the model registry
        target = format(self.mdl)

        # Parse the onclause
        onclause = None
        if self.onclause is not None:
            onclause = self.onclause.to_arg()

        return {
            "target": target,
            "onclause": onclause,
            "isouter": self.isouter,
            "full": self.full,
        }


class WhereArgs(BaseModel):
    mdl: ModelName
    attr: str
    op: str
    val: Any

    STR_TO_OP: ClassVar = {
        "==": eq,
        "<=": le,
        ">=": ge,
        "<": lt,
        ">": gt,
    }

    def to_arg(self):
        column = format(self.mdl, self.attr)
        operator = WhereArgs.STR_TO_OP[self.op]
        whereclause = operator(column, self.val)
        return whereclause


class SelectArgs(BaseModel):
    mdl: ModelName
    attr: str | None = None

    def to_arg(self):
        return format(self.mdl, self.attr)


class QueryArgs(BaseModel):
    selects: list[SelectArgs]
    joins: list[JoinArgs]
    wheres: list[WhereArgs]


def build_statement(query_args: QueryArgs):
    # SELECT
    statement = select(*[s.to_arg() for s in query_args.selects])

    # JOIN
    for j in query_args.joins:
        statement = statement.join(**j.to_kwarg())

    # WHERE
    for w in query_args.wheres:
        statement = statement.where(w.to_arg())

    return statement
