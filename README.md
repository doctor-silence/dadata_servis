<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&center=true&vCenter=true&width=435&lines=DaDaTa_servise%F0%9F%87%B7%F0%9F%87%BA"/></a>

______
Цель программы:
Программа предназначена для автоматического заполнения адреса с помощью сервиса Dadata на основе введенной пользователем информации.

Для установки зависимостей, необходимо выполнить следующие шаги:

Откройте командную строку в директории проекта
Введите команду "pip install -r requirements.txt"
Нажмите Enter и дождитесь завершения установки зависимостей
После установки зависимостей, вы можете запустить программу.
______
Использование программы:

Введите API ключ Dadata при первом запуске программы.
Введите адрес, для которого нужно получить рекомендации.
Программа отправляет запрос к сервису Dadata, чтобы получить рекомендации для введенного адреса.
Если запрос выполнен успешно, программа выведет список рекомендованных адресов и попросит вас выбрать нужный адрес.
Если вы хотите завершить работу программы в любой момент, введите команду "exit".
Если вы выберете адрес из списка, программа автоматически заполнит его в соответствующее поле и отобразит его на экране.
Если запрос выполнен с ошибкой, программа выведет сообщение об ошибке.
Настройки программы:
При первом запуске программы вам будет предложено ввести API ключ Dadata. Если вы не знаете, как получить ключ, пожалуйста, обратитесь к документации сервиса Dadata. По умолчанию программа использует следующие настройки:

URL сервиса Dadata: https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address<br>
API ключ: YOUR_API_KEY<br>
Язык запроса: русский<br>
Если вы хотите изменить настройки, вы можете сделать это вручную, отредактировав значения в таблице настроек. Таблица настроек находится в локальной базе данных и может быть открыта с помощью любого инструмента для работы с базами данных. В таблице настроек содержатся следующие поля:

key: название параметра настройки (url, api_key, language)<br>
value: значение параметра настройки<br>
Примеры использования:<br>
Пример 1. Запрос рекомендаций для адреса "ул. Красная площадь, 1".<br>
Введите адрес: ул. Красная площадь, 1

Россия, Москва, Красная площадь, 1<br>
Россия, Москва, Замоскворечье, Красная площадь, 1<br>
Россия, Краснодарский край, г. Краснодар, ул. Красная площадь, 1<br>
Выберите номер нужного адреса или введите "exit" для выхода:

