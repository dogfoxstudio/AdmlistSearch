# AdmlistSearch
Скрипт для парсинга сайта admlist и поиска абитуриента по их базе

Проект всё ещё достаточно сырой. Постараюсь его более менее закончить к 26 июля (началу первой волны зачисления)

### Как пользоваться
  В файле `links.txt` должны находиться ссылки на список заявлений по какой-либо специальности ВУЗа. Каждая ссылка на новой строке. Можно добавить абсолютно все ссылки вместо использования только необходимых, но тогда время поиска будет очень долгим. **Ссылки нужно вводить самому.**

  В файл `listabit.txt` заносятся имена для поиска, каждое с новой строки. **Свое имя пишется также как в admlist иначе ничего работать не будет.**
  
### Запуск
  * Вариант 1 (используется `listabit.txt`):
  
  `python3 main.py`
  
  * Вариант 2:
  
  `python3 main.py "ФИО 1" "ФИО 2" "ФИО N"`
  
  В случае ошибки:
  > "python3" не является внутренней или внешней
  >  командой, исполняемой программой или пакетным файлом.
  
  заменить `python3` на `python`

### Столбцы таблицы:
* ВУЗ
* Специальность
* Факультет
* ФИО
* Номер в списках
* Номер по оригиналам
* Номер оптимистичный
* Копия/оригинал

### To do:
* реализовать нормальный поиск без лишних файлов
* сделать взможность отправки таблицы сразу на электронную почту
* переработать форматирование и оформление
* попытаться реализовать всё в виде веб сервиса

### Контакты
Вопросы, проблемы и предложения писать на почту dogfoxstudiowork@yandex.ru

Донат [Яндекс.Деньги](https://money.yandex.ru/to/410018824908040)
