from __future__ import annotations

from sqlalchemy.orm import Session

from code_canvas.integrations.git import configure_git, git_state, preview_git, publish_git
from code_canvas.schemas import GitSettingsUpdate, RestoreRequest
from code_canvas.services.errors import ServiceError
from code_canvas.services.sync import (
    SyncBlockedError,
    SyncBusyError,
    inspect_sync,
    prepare_export,
    reconcile_catalog,
)


def export_preview(*, session: Session) -> dict:
    try:
        prepared = prepare_export(session)
    except (SyncBlockedError, SyncBusyError) as exc:
        raise ServiceError(409, str(exc)) from exc
    return {**prepared, "git": preview_git(fetch=False)}


def sync_status(*, session: Session) -> dict:
    try:
        return inspect_sync(session)
    except SyncBusyError as exc:
        raise ServiceError(409, str(exc)) from exc


def restore(payload: RestoreRequest, *, session: Session) -> dict:
    try:
        return reconcile_catalog(
            session,
            dry_run=payload.dry_run,
            decisions=payload.decisions,
            review_version=payload.review_version,
        )
    except (SyncBlockedError, SyncBusyError) as exc:
        raise ServiceError(409, str(exc)) from exc


def get_git_state() -> dict:
    return git_state(fetch=False)


def update_git_settings(payload: GitSettingsUpdate) -> dict:
    try:
        return configure_git(
            payload.remote_url, payload.branch, payload.user_name, payload.user_email
        )
    except (ValueError, RuntimeError) as exc:
        raise ServiceError(422, str(exc)) from exc


def preview_publish(*, session: Session) -> dict:
    try:
        prepared = prepare_export(session)
    except (SyncBlockedError, SyncBusyError) as exc:
        raise ServiceError(409, str(exc)) from exc
    result = preview_git(fetch=True)
    result["backup"] = prepared["backup"]
    result["sync"] = prepared["sync"]
    return result


def publish(*, session: Session) -> dict:
    try:
        prepared = prepare_export(session)
        return {**publish_git(), "backup": prepared["backup"], "sync": prepared["sync"]}
    except (RuntimeError, SyncBlockedError, SyncBusyError) as exc:
        raise ServiceError(409, str(exc)) from exc
