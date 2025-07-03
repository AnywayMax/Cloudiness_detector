import time
import io
from picamera import PiCamera
from PIL import Image
import numpy as np


def capture_image(resolution=(640, 480), delay=2):
    """
    Делает снимок с модуля камеры.
    :param resolution: кортеж (ширина, высота)
    :param delay: время в секундах для автонастройки экспозиции
    :return: PIL.Image
    """
    camera = PiCamera()
    camera.resolution = resolution
    camera.start_preview()
    time.sleep(delay)  # ждём, пока камера настроится
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg')
    camera.stop_preview()
    camera.close()
    stream.seek(0)
    return Image.open(stream)


def calculate_cloudiness(image, threshold=200):
    """
    Считает долю пикселей яркостью ≥ threshold.
    :param image: PIL.Image в любом цветовом формате
    :param threshold: порог яркости (0–255), выше которого считаем «облако»
    :return: float процент облачности
    """
    gray = image.convert('L')             # переводим в градации серого
    arr = np.array(gray)                  # в массив NumPy
    white = np.sum(arr >= threshold)      # считаем «белые» пиксели
    total = arr.size                      # всего пикселей
    return white / total * 100


def main():
    img = capture_image(resolution=(640, 480), delay=2)
    cloudiness = calculate_cloudiness(img, threshold=200)
    # выводим только число с одним знаком после запятой
    print(f"{cloudiness:.1f}")


if __name__ == "__main__":
    main()
