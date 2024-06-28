import cv2
import pytesseract
from autocorrect import Speller

# # Загрузка изображения
# image = cv2.imread('CV_pdf/page_0.png')
#
# # Преобразование изображения в оттенки серого
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# # invert = 255 - thresh
# # Применение порогового фильтра для выделения текста
# # _, threshold_image = cv2.threshold(invert, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# cv2.imwrite("ggg.png", thresh)
# # Использование pytesseract для распознавания текста
# text = pytesseract.image_to_string(image, lang="rus", config='--psm 6')

# spell = Speller(lang='ru')
# # Запись распознанного текста в файл
# with open('recognized_text.txt', 'w', encoding='utf-8') as file:
#     file.write(spell(text))
#     # file.write(text)


class ComVis:
    def __init__(self, path):
        self.image = cv2.imread(path)

    def bgr_gray(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        return thresh

    def get_image(self):
        return self.image


class NeuralNetwork:
    def __init__(self, image):
        self.text = pytesseract.image_to_string(image, lang="rus", config='--psm 6')

    def get_text(self):
        return self.text