# ometa_project

все необходимые пакеты данных находятся в файле requirements.txt
на ubuntu можна установить с помощью команды pip3 install -r requirements.txt

но не устанавлюваються два пакета так что я их сама добавляла этими командами:
pip3 install django-admin-sortable2
pip3 install easy-thumbnails
pip3 install django-phonenumber-field[phonenumbers]

поменить ip-адресс для запуска можно в файле ometa_project/settings.py
переменная ALLOWED_HOSTS

в файлах уже есть готовая БД, но если будет нужно то создать её можно камандой
pyhton3 manage.py migrate

запуск роекта вцыполняется командой
python manage.py runserver
