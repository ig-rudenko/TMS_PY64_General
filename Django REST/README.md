### Запуск тестов

Тесты Django.

```shell
python manage.py test
```

### Вместе с coverage

#### Установка.

Используйте pip или uv

```shell
pip install coverage
uv add coverage
```

Для запуска в проекте Django используйте команду:

```shell
coverage run --source='.' manage.py test
```

Эта команда заполнит «.coverage», который расположен в COVERAGE_FILE,
а затем вы можете увидеть результаты или отчет. 

Если вы хотите проверить только код Python, то вам необходимо сделать:

```shell
coverage run your_program.py arg1 arg2 arg3
```

#### Просмотр результата.

Если вы хотите вывести результаты в командной строке:

```shell
coverage report
```

Для более понятных и удобных отчетов:

```shell
coverage html
```