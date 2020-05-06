# django-lab1-opt10
Django| The first laboratory. News. 10-th option

Task:
Реалізувати веб-сайт з наступними сторінками: адміністративна сторінка для завантаження / видалення файлів і їх описів на / з сайту; призначена для користувача сторінка для пошуку файлу за ключовими словами опису і скачування файлу; адміністративна сторінка для відображення статистики про кількість завантажень кожного файлу з сайту. 

Start Instruction in russian:
После копирования проекта, создай python виртуальное окружение (python -m venv venv). Активируй его, и в корне проекта выполни команду pip install -r requirements.txt (Она установит все необходимые для проекта зависимости). Так же, по заданию нужно было делать все на mysql, создай у себя локально бд с названием "django_lab1_var10" , логином "root" и паролем "root". (Если что, можно назвать как угодно и потом заменить в файле Lab1Files_eng/Lab1Files_eng/settings.py под свои данные). Дальнейшие действия будут проихводиться в папке Lab1Files_eng/Lab1Files. Выполни команду " python manage.py makemigrations Lab1Files "  и после нее " python manage.py migrate ". После этого выполни команду " python manage.py createsuperuser " . Вводи какие хочешь данные. Они тебе будут нужны для перехода на администрирование сайта по URL адресу "localhost:8000/admin.py". Дальше выполни команду " python manage.py runserver ". Если все прошло без ошибок, переходи по ссылке, которая будет в командной строке и щелкай лабу.

[ Если появились проблемы с установкой и подключением данной лабораторной работы к mysql]
1. Перейди в Lab1Files_eng/Lab1Files_eng/settings.
2. Найти вот такие строчки:
      # DATABASES = {
      #     'default': {
      #         'ENGINE': 'django.db.backends.sqlite3',
      #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      #     }
      # }
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'django_lab1_var10',
              'USER': 'root',
              'PASSWORD': 'root',
          }
      }
3. Выдели их и вставь место них это:
       DATABASES = {
           'default': {
               'ENGINE': 'django.db.backends.sqlite3',
               'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
           }
       }
      # DATABASES = {
      #   'default': {
      #        'ENGINE': 'django.db.backends.mysql',
      #        'NAME': 'django_lab1_var10',
      #        'USER': 'root',
      #        'PASSWORD': 'root',
      #    }
      # }
4. Выполни команду из инструкции по установке " manage.py makemigrations Lab1Files " и следуй дальнейшим инструкциям из установки. Это создаст Sqlite базу данных. Это, конечно, не подходит по заданию лабораторной работы, но может тебе повезет и этого не обнаружат :)

P.S. Так же, в папке Screens лежат скрины для отчета
