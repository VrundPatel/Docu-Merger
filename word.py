import os

from docx import Document
from docx.shared import Inches
import getFullDocText as fullDoc

finalDoc = Document()

for file in os.listdir('docs'):
    if file.endswith('.docx'):
        fullText = fullDoc.getText(os.path.join('docs', file))
        finalDoc.add_paragraph(fullText)

finalDoc.save('docs/final.docx')
