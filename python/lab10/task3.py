from docx import Document
doc = Document('document.docx')
table = doc.tables[0]
data = {}
for row in table.rows[1:]:
    key = row.cells[0].text
    value = row.cells[2].text
    data[key] = value
print(data)