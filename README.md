Репозиторий eshop 
Установка (для пользователей операционных систем семейства MacOs/Linux):

Открыть терминал или консоль и перейти в нужную Вам директорию
Прописать команду git@github.com:Timenem/enshop.git

Если Вы используете https, то: https://github.com/Timenem/enshop.git

Прописать следующие команды:

  1. virtualenv env ДиректорияВиртуальногоОкружения
  2. source ДиректорияВиртуальногоОкружения/bin/activate
     
     Перейти в директорию eshop

  3. pip install -r requirements.txt
  4. python manage.py migrate

Запустить сервер - python manage.py runserver
