# api_yatube
Данный API написан в рамках курса "Python-разработчик" на платформе Яндекс Практикум
Для его создания использовались:
● Python 3.9.13
● Django REST Framework 3.12.4
● djoser

Авторизация выполняется с помощью JWT токенов

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/PsychoPendos/api_yatube.git
```

```
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:

(GET, POST): получаем список всех постов или создаём новый пост.
```
api/v1/posts/
```

(GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
```
api/v1/posts/{post_id}/
```

(GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
```
api/v1/posts/{post_id}/comments/
```

(GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
```
api/v1/posts/{post_id}/comments/{comment_id}/
```

(GET): получаем список всех групп.
```
api/v1/groups/
```

(GET): получаем информацию о группе по id.
```
api/v1/groups/{group_id}/
```

(GET): получаем подписки пользователя, сделавшего запрос, анонимные запросы запрещены.
```
api/v1/follow/
```

(POST): подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса.
```
api/v1/follow/
```

(POST): передаём логин и пароль, получаем JWT-токен.
```
api/v1/jwt/create/
```

(POST): передаём старый JWT-токен, получаем новый.
```
api/v1/jwt/refresh/
```

(POST): передаём JWT-токен, получаем его валидность.
```
api/v1/jwt/verify/
```

