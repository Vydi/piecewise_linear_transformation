# Алгоритм решения задачи

1. Загрузка необходимых библиотек для обработки изображения, если они нужны.
2. Преобразуем картинку к чёрно-белой для обработки. В данной работе использовалась функция из OpenCV (cv2.cvtColor). 
Это преобразование между RGB/BGR и оттенками серого. 
Ссылаясь на официальную документацию OpenCV, формула выглядит следующим образом:
RGB[A] to Gray:Y←0.299⋅R+0.587⋅G+0.114⋅B
3. Представим картинку в виде массива пикселей. 
4. Находим среднюю яркость. Чтоб найти среднюю яркость изображения нам нужно узнать сумму всех пикселей и разделить на их кол-во.
   _L=(SUM(r(i,j)))/(LEN(r(i,j)))_
5. Создаём новый массив заполненный 0 на основе нашего изображения.
6. Перебираем пиксели в массиве и преобразуем те, которые менее среднего линейно в значение из диапазона от [0, 128], а те, которые более или равны среднему в диапазон [128, 255]. Так, чтоб в общем средняя яркость преобразовалась к 128. 
   Воспользуемся формулой канонического уравнения прямой:

(x-x_a)/(x_b-x_a )=(y-y_a)/(y_b-y_a )

(x-0)/(L-0)=(y-0)/(L-0)  при x ∈[0,L]

(x-0)/(L-0)=(y-0)/(128-0)  x=L преобразуется в y=128 
				
(x-L)/(255-L)=(y-L)/(255-L)  при x ∈[L,255]
			
(x-L)/(255-L)=(y-128)/(255-128)  x=L преобразуется в y=128

          	Обозначим x-исходная яркость,y-новая яркость   
7. Преобразуем наш массив пикселей к картинке, чтоб увидеть результат.

Ко всем изображениям выполнялась пороговая обработка кусочно-линейного преобразования. 
После преобразования формул из алгоритма получаем такие уравнения:

y= 128x/L  при x ∈[0,L]
			
y= ((x-L)127)/(255-L)-128 при x ∈[L,255]
