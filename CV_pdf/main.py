from autocorrect import Speller
from CV_logic import ComVis, NeuralNetwork
from pdf_translate import PDFTranslate
import os


class Crave:
    def __init__(self, path):
        self.__comvis = ComVis()
        self.__neunet = NeuralNetwork()
        self.__pdf_img = PDFTranslate(path)

    def create_txt(self):
        print("sdfsdf")
        self.__pdf_img.gen_png()
        for i in self.__pdf_img.list_name:
            print(i)
            self.__comvis.set_image(f'ggg/' + i)
            self.__neunet.set_text(self.__comvis.get_image())
            print(self.__neunet.get_text())


c = Crave("/home/stas/PycharmProjects/Test_task/ТЗ на выполнение работ.pdf")
c.create_txt()