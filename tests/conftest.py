import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

BASELINE_ACTIVITIES = copy.deepcopy(app_module.activities)


def _restore_activities() -> None:
    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset in-memory activity data so tests remain isolated."""
    _restore_activities()
    yield
    _restore_activities()


@pytest.fixture
def client() -> TestClient:
    return TestClient(app_module.app)
