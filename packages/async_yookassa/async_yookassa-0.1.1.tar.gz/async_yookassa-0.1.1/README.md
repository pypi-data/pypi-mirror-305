# Async YooKassa (unofficial)

Неофициальный клиент для работы с платежами по [API ЮKassa](https://yookassa.ru/developers/api)

За основу взята [официальная библиотека от ЮМани](https://git.yoomoney.ru/projects/SDK/repos/yookassa-sdk-python/browse).  

## Цель
Заменить синхронный `requests` на асинхронный `httpx`, также переложить валидацию данных на `Pydantic`.

## Реализовано на данный момент

* Модели данных запроса и ответа платежа, а также необходимые для них модели.
* Класс `Configuration`, для определения авторизации по апи.
* Класс `Payment` с возможностью создать платёж.
* Класс `APIClient` для выполнения запросов к API.


## Требования

1. Python >=3.12 (на момент разработки)
2. pip

## Установка
### C помощью pip

1. Установите pip.
2. В консоли выполните команду
```bash
pip install --upgrade yookassa
```

## Начало работы

1. Импортируйте модуль
```python
import async_yookassa
```
2. Установите данные для конфигурации
```python
from async_yookassa import Configuration

Configuration.configure(account_id='<Идентификатор магазина>', secret_key='<Секретный ключ>')
```

или

```python
from async_yookassa import Configuration

Configuration.account_id = '<Идентификатор магазина>'
Configuration.secret_key = '<Секретный ключ>'
```

или через oauth

```python
from async_yookassa import Configuration

Configuration.configure_auth_token(token='<Oauth Token>')
```

Если вы согласны участвовать в развитии SDK, вы можете передать данные о вашем фреймворке, cms или модуле:
```python
from async_yookassa import Configuration
from async_yookassa.models.configuration_submodels.version_model import Version

Configuration.configure('<Идентификатор магазина>', '<Секретный ключ>')
Configuration.configure_user_agent(
    framework=Version(name='Django', version='2.2.3'),
    cms=Version(name='Wagtail', version='2.6.2'),
    module=Version(name='Y.CMS', version='0.0.1')
)
```

3. Вызовите нужный метод API. [Подробнее в документации к API ЮKassa](https://yookassa.ru/developers/api)
