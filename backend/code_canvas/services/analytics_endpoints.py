from __future__ import annotations

from sqlalchemy.orm import Session

from code_canvas.services.analytics import analytics_overview, canvas_graph


def overview(*, session: Session) -> dict:
    return analytics_overview(session)


def canvas(*, session: Session) -> dict:
    return canvas_graph(session)
