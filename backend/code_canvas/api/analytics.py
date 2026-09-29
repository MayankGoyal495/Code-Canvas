from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from code_canvas.db import get_session
from code_canvas.services import analytics_endpoints as operations

router = APIRouter()


@router.get("/api/analytics/overview")
def overview(session: Session = Depends(get_session)) -> dict:
    return operations.overview(session=session)


@router.get("/api/analytics/canvas")
def canvas(session: Session = Depends(get_session)) -> dict:
    return operations.canvas(session=session)
