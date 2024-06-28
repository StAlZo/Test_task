import dataclasses

import fitz  # PyMuPDF, imported as fitz for backward compatibility reasons
# file_path = "ТЗ на выполнение работ.pdf"
# doc = fitz.open(file_path)  # open document
# for i, page in enumerate(doc):
#     pix = page.get_pixmap()  # render page to an image
#     pix.save(f"page_{i}.png")


class PDFTranslate:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def gen_png(self):
        doc = fitz.open(self.file_path)  # open document
        for i, page in enumerate(doc):
            pix = page.get_pixmap()  # render page to an image
            pix.save(f"ggg/page_{i}.png")


@dataclasses
class File:
    name: str