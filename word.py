# Import for working with file-system.
import os
# Import for the GUI
import Tkinter as tk
import tkMessageBox
# Import for working with word documents
from docx import Document
import getFullDocText as fullDoc

def merge():
    finalDoc = Document()
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            if 'Questions' in name and name.endswith('.docx'):
                fullText = fullDoc.getText(os.path.join(root, name))
                finalDoc.add_heading(name[:-5])
                finalDoc.add_paragraph(fullText)
    finalDoc.save('docs/final.docx')
    tkMessageBox.showinfo("Docu-Merger", "Documents merged!")

window = tk.Tk()
window.wm_title('Docu-Merger')
window.geometry('200x100')
window.configure(background='#146eff')
button = tk.Button(window, text="Merge Document", command = merge)
button.pack()
window.mainloop()