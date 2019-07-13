import pandas as pd
import sys
import admsearch

names = []

if (len(sys.argv)>1):
    for i in range(1, len(sys.argv)):
        names.append(sys.argv[i])
else:
    with open('listabit.txt', 'r') as la:
        names = la.read().splitlines()
html = ""
for name in names:
    html = html + "<h3>" + name + "</h3>"
    table = admsearch.search_by_name(name)
    html += pd.DataFrame(table).to_html(header=None, index=False, border=2)

with open('a.html', 'w') as f:
    f.write(html)
