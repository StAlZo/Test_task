import cv2
import numpy as np
import pytesseract

image = cv2.imread('page_0.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение порогового фильтра для выделения текста
_, threshold_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Подготовка изображения для передачи его в модель
input_image = cv2.resize(threshold_image, (32, 32))
input_image = np.expand_dims(input_image, axis=-1)
input_image = np.expand_dims(input_image, axis=0)

text = pytesseract.image_to_string(input_image, lang="rus")

# Запись распознанного текста в файл
with open('recognized_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)