import requests
import sqlite3

# Получаем API ключ и базовый URL сервиса dadata
api_key = input('Введите API ключ: ')
url = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address'

# Подключаемся к локальной базе данных для хранения пользовательских настроек
conn = sqlite3.connect('settings.db')
c = conn.cursor()

# Создаем таблицу для хранения настроек, если ее еще нет
c.execute('CREATE TABLE IF NOT EXISTS settings (key TEXT, value TEXT)')
conn.commit()

# Задаем настройки по умолчанию, если они еще не заданы
c.execute("INSERT OR IGNORE INTO settings VALUES ('url', 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address')")
c.execute("INSERT OR IGNORE INTO settings VALUES ('api_key', ?)", (api_key,))
c.execute("INSERT OR IGNORE INTO settings VALUES ('language', 'ru')")
conn.commit()

while True:
    # Запрашиваем у пользователя адрес
    address = input('Введите адрес или "exit" для выхода: ')
    if address == "exit":
        print("Выход...")
        break

    # Получаем настройки из базы данных
    c.execute("SELECT * FROM settings")
    settings = dict(c.fetchall())

    # Формируем параметры запроса к сервису dadata
    params = {
        'query': address,
        'count': 10,
        'language': settings.get('language', 'ru')
    }

    # Добавляем заголовки с API ключом для авторизации запросов к сервису dadata
    headers = {
        'Authorization': f'Token {settings.get("api_key", api_key)}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Отправляем запрос к сервису dadata
    response = requests.post(settings.get('url', url), json=params, headers=headers)

    # Если запрос прошел успешно, выводим список адресов на экран и запрашиваем у пользователя выбор адреса
    if response.status_code == 200:
        data = response.json()
        suggestions = data['suggestions']
        for i, suggestion in enumerate(suggestions):
            print(f"{i+1}. {suggestion['value']}")
        selected = input('Выберите номер нужного адреса или введите "exit" для выхода: ')
        if selected == "exit":
            print("Выход...")
            break
        else:
            selected = int(selected)
            selected_suggestion = suggestions[selected - 1]
            address = selected_suggestion['value']
            full_address = selected_suggestion['unrestricted_value']
            coords = selected_suggestion['data']['geo_lat'], selected_suggestion['data']['geo_lon']
            print(f"Адрес: {full_address}")
            print(f"Координаты: {coords}")
    else:
        print('Ошибка при выполнении запроса к сервису dadata')

# Закрываем соединение с базой данных
conn.close()



