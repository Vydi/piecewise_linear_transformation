# Импорт нужных для работы библиотек
import cv2
import imutils
import numpy as np


def func(img):  # Функция, где передаём параметры название картинки, параметр из диапазона [0, 128], параметр из диапазона [128, 255]
    image = cv2.imread(img)  # Прочитываем изображение
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Преобразуем изображение в чб формат

    plist = []  # Список для хранения массива пикселей
    # Заполнение списка массивом пикселей
    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            plist.append(gray_img[i, j])
    r_avg = int(sum(plist) / len(plist))  # Средняя яркость изображения
    print('Средняя яркость изображения: ', r_avg)
    thresh_img = np.zeros((gray_img.shape[0], gray_img.shape[1]),
                          dtype=np.uint8)  # Создаём новый массив заполненный 0 на основе нашего изображения.
    new_plist = []  # Новый список для хранения преобразованного массива пикселей
    # Заполнение списка массивом преобразованных пикселей в соответсвии с указанными параметрами из диапазонов
    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            if gray_img[i, j] < r_avg:
                thresh_img[i, j] = (128*thresh_img[i, j])/r_avg
                # print(i, j)
            elif gray_img[i, j] >= r_avg:
                thresh_img[i, j] = (((thresh_img[i, j] - r_avg)*127)/(255-r_avg)) - 128
            new_plist.append(thresh_img[i, j])
    new_r_avg = int(sum(new_plist) / len(new_plist))  # Средняя яркость изображения после преобразования
    print('Средняя яркость изображения: ', new_r_avg)
    cv2.imshow('original image', imutils.resize(gray_img, 400))  # Выводим исходное изображение
    cv2.imshow('precewise image', imutils.resize(thresh_img, 400))  # Выводим преобразованное изображение
    if cv2.waitKey(
            0):  # Делаем остановку для того, чтоб с экрана не пропали изображения, пока пользователь не закроет сам
        cv2.destroyWindow()


# Вводим нужные нам параметры
img = input('Ведите название картинки: ')

func(img)  # Запускаем функцию
