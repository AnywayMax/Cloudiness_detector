# Cloudiness Detector
_Cloudiness detector for Raspberry Pi Zero on your mini‑satellite._

Снимает кадр с камеры, анализирует яркость и выдаёт процент облачности.

**Простой детектор облачности:**

– Вместо тяжёлых фотографий скрипт на Python (Pillow или OpenCV) анализирует кадр и считает долю белых пикселей – то есть процент облачности.

– По 1 кбит/с вы шлёте не мегабайты, а одно число: «облачность 73 %».

– Пару десятков строк кода, минимальная нагрузка на Raspberry Pi Zero и почти нулевая скорость обработки.

– С такими данными можно делать оперативные погодные сводки, проверять прогнозы и собирать экологические отчёты прямо из космоса.


Простой, но очень полезный проект для вашего мини‑спутника!

**Что нужно установить на борту:**
pip3 install pillow numpy picamera

**Как запускать:**
python3 cloudiness_detector.py


P.S. Скрипт займёт на RPi Zero пару десятков строк, почти не нагрузит CPU и по SSH вернёт только одну строку с процентом облачности — идеально для канала в 1 кбит/с.
https://habr.com/ru/companies/ruvds/articles/924590/
