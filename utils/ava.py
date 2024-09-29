import requests
from PIL import Image, ImageDraw
from io import BytesIO
from utils import db

def download() -> None:
    'Скачивает изображение по ссылке'
    url = f'https://es.ciur.ru/{db.user.get().avatar_url}'
    response = requests.get(url)
    
    # Создаем объект изображения из байтов
    img = Image.open(BytesIO(response.content)).convert("RGBA")
    
    # Превращаем изображение в кружочек
    circle(img)

def circle(img: Image) -> None:
    'Превращает изображение в кружочек'
    # Определяем размер для квадратного изображения
    size = min(img.size)  # Используем минимальный размер для обрезки
    
    # Обрезаем изображение до квадрата
    left = (img.width - size) // 2
    top = (img.height - size) // 2
    right = (img.width + size) // 2
    bottom = (img.height + size) // 2
    square_img = img.crop((left, top, right, bottom))
    
    # Создаем маску в форме круга
    mask = Image.new("L", square_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    
    # Создаем новое изображение с прозрачным фоном
    circle_img = Image.new("RGBA", square_img.size, (255, 255, 255, 0))
    
    # Применяем маску к квадратному изображению
    circle_img.paste(square_img, (0, 0), mask)
    
    # Сохраняем результат
    circle_img.save('ava.png')