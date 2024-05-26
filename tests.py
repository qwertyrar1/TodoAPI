import requests
import pytest

from config import Config


@pytest.fixture
def created_task():
    response = requests.post(
        f"{Config.BASE_URL}/tasks",
        json={"title": "Test Task", "description": "This is a test task."}
    )
    assert response.status_code == 201
    task_id = response.json().get("id")
    yield task_id
    # Cleanup
    delete_response = requests.delete(f"{Config.BASE_URL}/tasks/{task_id}")
    assert delete_response.status_code == 200


def test_create_task():
    response = requests.post(
        f"{Config.BASE_URL}/tasks",
        json={"title": "Test Task", "description": "This is a test task."}
    )
    assert response.status_code == 201
    # Cleanup
    task_id = response.json().get("id")
    delete_response = requests.delete(f"{Config.BASE_URL}/tasks/{task_id}")
    assert delete_response.status_code == 200


def test_get_task(created_task):
    response = requests.get(f"{Config.BASE_URL}/tasks/{created_task}")
    assert response.status_code == 200


def test_get_nonexistent_task():
    response = requests.get(f"{Config.BASE_URL}/tasks/nonexistent_task_id")
    assert response.status_code == 404


def test_update_task(created_task):
    update_response = requests.put(
        f"{Config.BASE_URL}/tasks/{created_task}",
        json={"title": "Updated Task", "description": "This is an updated task."}
    )
    assert update_response.status_code == 200


def test_delete_task():
    response = requests.post(
        f"{Config.BASE_URL}/tasks",
        json={"title": "Test Task to Delete", "description": "This task will be deleted."}
    )
    assert response.status_code == 201
    task_id = response.json().get("id")
    delete_response = requests.delete(f"{Config.BASE_URL}/tasks/{task_id}")
    assert delete_response.status_code == 200


