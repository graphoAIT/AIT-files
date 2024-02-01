import flask

from datetime import datetime

import requests
import os
from PIL import Image

apiKey = 'VoGJYdB71YZwFeubjQiy1ibx7Q1OymYlysx2cdUj'


def nasaNews(date):
    print('Extracting data')
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + str(apiKey)
    params = {'date': str(date)}
    r = requests.get(url, params=params)
    data = r.json()
    info = data['explanation']
    title = data['title']

    imageURl = data['url']
    imageR = requests.get(imageURl)

    fileName = str(date) + '.jpg'
    with open(fileName, 'wb') as f:
        f.write(imageR.content)

    path1 = "C:\\Users\\WALTON\\PycharmProjects\\MASGO\\" + str(fileName)
    path2 = "C:\\Users\\WALTON\\PycharmProjects\\MASGO\\Database\\Nasa Database\\Space Images\\" + str(fileName)

    os.rename(path1, path2)
    img = Image.open(path2)
    img.show()
    print(f'{title}')
    print(f''' {info}''')

def marsImg(date):

    name = 'curiosity'
    api = str(apiKey)
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={api}"
    r = requests.get(url)
    data = r.json()
    photos = data['photos'][:1]

    try:
        for index, photo in enumerate(photos):
            camera = photo['camera']
            rover = photo['rover']
            rover_name = rover['name']
            camera_name = camera['name']
            full_camera_name = camera['full_name']
            date_of_photo = ['earth-date']
            imgUrl = photo['img_src']
            p = requests.get(imgUrl)
            img = f'{index}.jpg'

            with open(img, 'wb') as file:
                file.write(p.content)

            path1 = 'C:\\Users\\WALTON\\PycharmProjects\\MASGO\\' + str(img)
            path2 = 'C:\\Users\\WALTON\\PycharmProjects\\MASGO\\Database\\Nasa Database\\Mars Images\\' + str(img)
            os.rename(path1, path2)
            os.startfile(path2)
            print(f'This image was captured by {rover_name} rover through {full_camera_name} or {camera_name} on {date} ')

    except:
        print(f'No Images have captured on {date}')

