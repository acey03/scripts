import PyPDF2
from sys import argv
import os

merger = PyPDF2.PdfMerger()
result = "result"

if len(argv) > 1:
    result = argv[1]

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
merger.write(result + ".pdf")