import admparser

# Получение ссылок из файла
with open('links.txt', 'r') as ls:
    links = ls.read().splitlines()

# Получение имени (возможны проблемы с полными тезками)
# РЕГИСТРОЗАВИСИМО

def search_by_name(name):
    data = [["ВУЗ","Специальность","Факультет","ФИО","Номер","Номер по оригиналам","Номер оптимистичный","Копия/оригинал"]]
    for link in links:
        markup = admparser.get_markup(link)
        header = admparser.get_header(markup)
        tbl = admparser.get_main_table(markup)
        for i in range(3,len(tbl)):
            if name in tbl[i][3]:
                dt = []
                dt.append(header[0]) # ВУЗ
                dt.append(header[2]) # Специальность
                dt.append(header[1]) # Подразделение/институт
                dt.append(tbl[i][3]) # ФИО
                dt.append(tbl[i][0]) # Номер
                dt.append(tbl[i][1]) # Номер по оригиналам
                dt.append(tbl[i][2]) # Номер оптимистичный
                dt.append(tbl[i][4]) # Копия/оригинал
                data.append(dt)
    return data
