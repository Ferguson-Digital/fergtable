from datetime import datetime

from django.test.utils import override_settings

import pytest
from freezegun import freeze_time

from baserow.core.action.handler import ActionHandler
from baserow.core.actions import CreateGroupActionType
from baserow_enterprise.audit_log.handler import AuditLogHandler
from baserow_enterprise.audit_log.models import AuditLogEntry


@pytest.mark.django_db(transaction=True)
@override_settings(DEBUG=True)
def test_actions_are_not_inserted_as_audit_log_entries_without_license(
    api_client, enterprise_data_fixture
):

    user = enterprise_data_fixture.create_user()

    with freeze_time("2023-01-01 12:00:00"):
        CreateGroupActionType.do(user, "group 1")

    assert AuditLogEntry.objects.count() == 0


@pytest.mark.django_db
@override_settings(DEBUG=True)
def test_actions_are_inserted_as_audit_log_entries_with_license(
    api_client, enterprise_data_fixture, synced_roles
):
    enterprise_data_fixture.enable_enterprise()
    user = enterprise_data_fixture.create_user()

    with freeze_time("2023-01-01 12:00:00"):
        CreateGroupActionType.do(user, "group 1")

    with freeze_time("2023-01-01 12:00:01"):
        CreateGroupActionType.do(user, "group 2")

    assert AuditLogEntry.objects.count() == 2


@pytest.mark.django_db
@override_settings(DEBUG=True)
def test_audit_log_handler_can_clear_entries_older_than(
    api_client, enterprise_data_fixture, synced_roles
):
    enterprise_data_fixture.enable_enterprise()
    user = enterprise_data_fixture.create_user()

    with freeze_time("2023-01-01 12:00:00"):
        CreateGroupActionType.do(user, "group 1")

    with freeze_time("2023-01-01 12:00:10"):
        CreateGroupActionType.do(user, "group 2")

    AuditLogHandler.delete_entries_older_than(datetime(2023, 1, 1, 12, 0, 1))
    assert AuditLogEntry.objects.count() == 1

    AuditLogHandler.delete_entries_older_than(datetime(2023, 1, 2, 12, 0, 0))
    assert AuditLogEntry.objects.count() == 0


@pytest.mark.django_db
@pytest.mark.undo_redo
@override_settings(DEBUG=True)
def test_audit_log_handler_add_entries_for_undone_redone_actions(
    api_client, enterprise_data_fixture, synced_roles
):
    enterprise_data_fixture.enable_enterprise()
    session_id = "session-id"
    user = enterprise_data_fixture.create_user(session_id=session_id)

    with freeze_time("2023-01-01 12:00:00"):
        CreateGroupActionType.do(user, "group 1")

    assert AuditLogEntry.objects.count() == 1

    ActionHandler.undo(user, [CreateGroupActionType.scope()], session_id)
    assert AuditLogEntry.objects.count() == 2

    ActionHandler.redo(user, [CreateGroupActionType.scope()], session_id)
    assert AuditLogEntry.objects.count() == 3
