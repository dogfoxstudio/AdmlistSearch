import requests
import lxml.html

# Получение html страницы
def get_markup(link):
    return lxml.html.fromstring(requests.get(link).content)

# Получение основной таблицы
def get_main_table(markup):
    tbl = []
    rows = markup.cssselect("tr")
    for row in rows:
        tbl.append(list())
        for td in row.cssselect("td"):
            tbl[-1].append(str(td.text_content()))
    # tbl[1][0] КЦП
    # tbl[1][1] заявления
    # tbl[x][0] номер
    # tbl[x][1] номер по оригиналам
    # tbl[x][2] номер оптимистичный
    # tbl[x][3] ФИО
    # баллы не работают (admlist их выкладывает через скрипт)
    # tbl[x][4] копия/оригинал
    # x>=3
    return tbl

# Получение названия ВУЗа и специальности. Оно работает. Не спрашивайте как
def get_header(markup):
    # header[0] ВУЗ
    # header[1] подразделение/институт
    # header[2] специальность
    return (str(markup.cssselect("h2")[0].text_content()).split(",",3))
