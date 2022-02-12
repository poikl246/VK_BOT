# from PIL import Image
import json
import os
import random

from PIL import Image, ImageDraw, ImageFont

with open("data.json", 'r', encoding='utf-8') as f:
    templates = json.load(f)


def magic(data, name):
    im = Image.open(f'foto/{data["file_name"]}')
    # Создаем объект со шрифтом
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('Comic_CAT.otf', size=data['saze'], encoding='utf-8')
    draw.text(
        (data['poz_F_name'][0], data['poz_F_name'][1]),
        data['F_name'],
        # Добавляем шрифт к изображению
        font=font,
        fill=data['colour_f'])

    draw.text(
        (data['poz_name'][0], data['poz_name'][1]),
        name,
        # Добавляем шрифт к изображению
        font=font,
        fill= data['colour_name'])

    file_name = f'output/{random.randint(-999999, 99999999)}.jpg'

    im.save(file_name)
    # im.show()
    return file_name



def main(name, foto_n = random.randint(0, len(os.listdir("foto")) - 1)):
    if foto_n >= len(os.listdir("foto")):
        foto_n = foto_n - 1

    data = templates[f'{foto_n}']
    # data = templates['10']
    print(foto_n, data)
    # name =
    return magic(data=data, name=name)

if __name__ == '__main__':
    # for i in range(10):
    #     main()
    main('NIKITA MOSKALEV')




# data = {}
#
# for i in range(50):
#     data[i] = {
#         "file_name": '1.jpg',
#         'F_name': 'привет',
#         'Name': 'Nikita',
#         'poz_F_name': [2891, 2310],
#         'poz_name': [2529, 2786],
#         'colour_f': '#1CA606',
#         'colour_name': '#1CA606'
#     }
#
#
# with open("data.json", "w", encoding='utf-8') as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)

