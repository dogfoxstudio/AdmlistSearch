import pandas as pd
import admsearch

with open('listabit.txt', 'r') as la:
    names = la.read().splitlines()
html = ""
for name in names:
    table = admsearch.search_by_name(name)
    html += pd.DataFrame(table).to_html(header=None, index=False, border=2)

with open('a.html', 'w') as f:
    f.write(html)
