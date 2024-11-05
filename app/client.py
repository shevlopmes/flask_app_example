import requests

def check_root_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Запрос успешен, код 200.")
        else:
            print(f"Ожидался код 200, но получен код {response.status_code}.")
    except requests.RequestException as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")


check_root_url("http://localhost:8080")