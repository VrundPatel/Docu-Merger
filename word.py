import os
from docx import Document
import getFullDocText as fullDoc

finalDoc = Document()
for root, dirs, files in os.walk(os.getcwd()):
    for name in files:
        if 'Questions' in name and name.endswith('.docx'):
            fullText = fullDoc.getText(os.path.join(root, name))
            finalDoc.add_heading(name[:-5])
            finalDoc.add_paragraph(fullText)
finalDoc.save('docs/final.docx')
