# YaMDb API

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

---
## Установка

```bash
python3 -m venv venv    # use 'python' instead 'python3' for Windows
source venv/bin/activate
pip3 install -r requirements.txt
```

## Запуск приложения

```bash
python3 manage.py runserver    # use 'python' instead 'python3' for Windows
```
---
## Алгоритм регистрации пользователей
- Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.
- YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
- Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит token (JWT-токен).
- При желании пользователь отправляет PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполняет поля в своём профайле (описание полей — в документации).
---

## Пользовательские роли
**Аноним** — может просматривать описания произведений, читать отзывы и комментарии.

**Аутентифицированный пользователь (user)** — может читать всё, как и Аноним, дополнительно может публиковать отзывы и ставить рейтинг произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы и ставить им оценки; может редактировать и удалять свои отзывы и комментарии.

**Модератор (moderator)** — те же права, что и у Аутентифицированного пользователя плюс право удалять и редактировать любые отзывы и комментарии.

**Администратор (admin)** — полные права на управление проектом и всем его содержимым. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.

**Администратор Django** — те же права, что и у роли Администратор.

---

## Аутентификация
`jwt-token`

Используется аутентификация с использованием JWT-токенов

---

## Примеры запросов к API:

### Регистрация нового пользователя
```
POST   /api/v1/auth/signup/
```

### Получение JWT-токена
```
POST  /api/v1/auth/token/
```

### Получение списка всех категорий / Добавление новой категории/ Удаление категории
```
GET/POST  /api/v1/categories/
DELETE  /api/v1/categories/{slug}/
```

### Получение списка всех жанров / Добавление жанра / Удаление жанра
```
GET/POST  /api/v1/genres/
DELETE  /api/v1/genres/{slug}/
```

### Получение списка всех произведений / Добавление произведения 
```
GET/POST  /api/v1/titles/
```

### Получение информации / Частичное обновление / Удаление произведения
```
GET/PATCH/DELETE  /api/v1/titles/{titles_id}/
```

### Получение списка всех отзывов / Добавление нового отзыва
```
GET/POST  /api/v1/titles/{title_id}/reviews/)
```

### Полуение/ Частичное обновление/ Удаление отзыва по id
```
GET/PATCH/DELETE /api/v1/titles/{title_id}/reviews/{review_id}/
```

### Получение списка всех комментариев к отзыву / Добавление комментария к отзыву
```
GET/POST  /api/v1/titles/{title_id}/reviews/{review_id}/comments/)
```

### Получение/ Частичное обновление/ Удаление комментария к отзыву
```
GET/PATCH/DELETE  /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

---
## Технологии
- Django 2.2
- Python 3.7
- Django REST Framework
- ReDoc