# ometa_project

## Как деплоить:

### Если обновили файлы моделей (**/models.py):
Запустить из папки проекта:
1) `python3 manage.py makemigrations`
2) `python3 manage.py migrate`
3) `systemctl restart gunicorn`

Всё, база обновлена, gunicorn перезапущен


### Если обновили любые python (*.py) файлы:
`systemctl restart gunicorn`

### Если добавили или обновили файлы в/из custom_static
Запустить из папки проекта:
1) `python3 manage.py collectstatic` (если попросит ввод - ответить ему `yes`)
2) Вы великолепны, новую статику уже сёрвит **nginx**
