import cv2
import pytesseract

# Загрузка изображения
image = cv2.imread('page_0.png')

# Преобразование изображения в оттенки серого
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение порогового фильтра для выделения текста
_, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Использование pytesseract для распознавания текста
text = pytesseract.image_to_string(threshold_image, lang="rus")

# Запись распознанного текста в файл
with open('recognized_text.txt', 'w', encoding='utf-8') as file:
    file.write(text)
