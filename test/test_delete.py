import requests


def test_add():
    body = {"title": "Задача1", "completed": False}
    response = requests.post("http://5.101.50.9:8014/", json=body)
    response_body = response.json()


    response = requests.delete(f'http://5.101.50.9:8014/{id}')

    assert response.status_code == 404