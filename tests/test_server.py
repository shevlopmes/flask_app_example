import pytest
from app.server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_tasks_empty(client):
    """
    Тест проверяет, что при пустой базе данных
    GET /api/tasks возвращает пустой список
    """
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert response.json == []