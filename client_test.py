import requests

BASE_URL = "http://aurora19.duckdns.org:29/api"  # базовый url
data = {}
token = None

def aurora_chat(message: str, token: str):
    url = f"{BASE_URL}/chat"

    # Подготовка данных для запроса
    data = {
        "message": message  # Отправляем строку напрямую
    }

    # Подготовка заголовков
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Отправка POST-запроса
    response = requests.post(url, json=data, headers=headers)

    # Проверка статуса ответа
    if response.status_code == 200:
        return response.json()  # Возвращаем ответ в формате JSON
    else:
        raise Exception(f"Ошибка при отправке сообщения: {response.status_code} - {response.text}")

def aurora_register(username: str, password: str):
    url = f"{BASE_URL}/register"

    data = {'username': username,
            'password': password}

    response = requests.post(url, json=data, verify=False)  # Отключение проверки SSL

    return response.json()['access_token']

def aurora_login(username: str, password: str):

    url = f"{BASE_URL}/token"

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)

    return response.json()['access_token']  # Возвращаем токен доступа

# Пример использования функции
if __name__ == "__main__":
    act = int(input("""Выберите действие:
                1) Регистрация в системе
                2) Вход в систему
                >>>"""))
    
    if act == 1:
        username = input('Ваше имя пользователя- ')
        password = input('Ваш пароль- ')
        token = aurora_register(username, password)
        print(token)
    elif act == 2:
        username = input('Ваше имя пользователя- ')
        password = input('Ваш пароль- ')
        token = aurora_login(username, password)
        print(token)

    while True:
        if token != None:
            msg = input('Вы- ')
            response = aurora_chat(message=msg, token=token)
            print("Аврора- ", response['response'])