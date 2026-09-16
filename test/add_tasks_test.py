import requests

def add_tasks():
    """ формирует новую задачу, изменяет и проверяет что ИД не поменялся"""
    url = "http://5.101.50.9:8014/"
    body = {"title":"задание на сегодня","completed":False}
    response = requests.post(url, json = body)
    response_body_id = response.json()[id]
    assert response.status_code == 200

#изменить и проверить что ИД не поменялся
    body = {"title":"Новое задание"}
    response = requests.patch(f'{url}/{response_body_id}', json = body)
    response_id = response.json()[id]
    assert  response_body_id == response_id


