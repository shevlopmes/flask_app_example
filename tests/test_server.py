import pytest
from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """
    Тест проверяет:
    1. Что главная страница возвращает успешный статус код
    2. Что возвращается HTML
    3. Что на странице есть ключевые элементы
    """
    response = client.get('/')

    # Проверяем статус код
    assert response.status_code == 200

    # Проверяем, что вернулся HTML
    assert response.content_type == 'text/html; charset=utf-8'

    # Проверяем наличие важных элементов на странице
    html_content = response.data.decode('utf-8')
    assert '<title>Task Tracker</title>' in html_content
    assert 'Add New Task' in html_content
    assert 'id="tasks"' in html_content


# Можно добавить больше тестов для API endpoints
def test_get_tasks_empty(client):
    """
    Тест проверяет, что при пустой базе данных
    GET /api/tasks возвращает пустой список
    """
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert response.json == []