import requests

    #Создать задачу, Проставить отметку о выполнении и проверить что completed ==True
def test_task():
    body = {"title":"generated","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]

    body = {'completed':True}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    assert response.status_code == 200
    assert response.json()['completed']==True
