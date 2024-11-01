from typing import Any
from fastapi import APIRouter, Depends
from sqlmodel import Session
from sqlalchemy.engine.row import Row

from parsomics_api_server.dependencies import get_session_ro
from parsomics_api_server.querying._query_builder import (
    QueryArgs,
    build_statement,
)

router = APIRouter(
    prefix="/querying",
)


@router.get("/", response_model=Any)
def query(
    *,
    session: Session = Depends(get_session_ro),
    query_args: QueryArgs,
):
    statement = build_statement(query_args)
    results = session.exec(statement).all()

    # Convert SQLAlchemy rows to tuples, which are serializable
    results = [tuple(r) if isinstance(r, Row) else r for r in results]

    return results
