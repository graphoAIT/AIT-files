import os
import time
import webbrowser as web
import base64
import os
import speech_recognition as sr
from datetime import datetime
from PIL import Image
import pywikihow
from datetime import date
import requests
from os import startfile
from pyautogui import click
from time import sleep
from keyboard import press
from keyboard import write
import pywhatkit
import wolframalpha
from pywikihow import search_wikihow, WikiHow
import random
import sys
from translate import Translator
import pyttsx3
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import wikipedia
from PyDictionary import PyDictionary as dictionary
import json
import pyjokes
import datetime
from email.message import EmailMessage
import ssl
import smtplib
# import cartopy.crs as ccrs
# import matplotlib.pyplot as plt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 176.5)


def speak(audio):
    print(f': {audio}')
    print('  ')
    engine.say(audio)
    engine.runAndWait()


def listen():
    text = input('> ')

    return text.lower()


def listen_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        # r.energy_threshold()
        print("say anything : ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            listen()

    return text.lower()


passcode = str('don')
password = input('Password : ')

if passcode == password:
    speak('Initiating Grapho AIT')
    speak('Wait a minute please')

    time.sleep(5)

    def tasker():
        while True:
            query = listen()

            if 'bye' in query:
                speak('Alright, see ya')
                quit()

            elif 'who are you' in query:
                print('I am Grapho AIT developed by Raiyan Khan Farhaan, President of Graphosoft')

            elif 'google search' in query:
                term = query.replace('google search', '')
                term = term.replace('search', '')
                term = term.replace('jarvis', '')
                term = term.replace('masgo', '')
                # term = term.replace('how to', '')

                Query = str(term)
                pywhatkit.search(Query)

            elif 'youtube search' in query:
                term = query.replace('youtube search', '')
                term = term.replace('MASGO', '')
                result = 'https://www.youtube.com/results?search_query=' + term
                web.open(result)

                pywhatkit.playonyt(term)

            elif 'speed test' in query:

                def run_uit():

                    print("I Am Checking Speed Sir , Wait For A While .")

                    import speedtest

                    speed = speedtest.Speedtest()

                    upload = speed.upload()

                    correct_Up = int(int(upload) / 800000)

                    download = speed.download()

                    correct_down = int(int(download) / 800000)

                    print(f"Downloading Speed Is {correct_down} MB Per Second .")
                    print(f"Uploading Speed Is {correct_Up} MB Per Second .")

                run_uit()

            elif 'task' in query:
                Query = query.replace('task', '')
                api_key = 'A7L6AG-A33737U8QJ'
                requester = wolframalpha.Client(api_key)
                requested = requester.query(Query)

                try:
                    answer = next(requested.results).text
                    print(answer)
                except:
                    print('I apologise, but am still in debt with the answers.')
                    print('Pray you say me the answer')
                    value = input('The actual answer: ')
                    values = value.replace('correct answer', '')
                    values = values.replace('answer', '')
                    print(f'The answer is: {values}')

            elif 'whatsapp' in query:
                print('''Would you like to
    1.Call
    2.Message
    3.Chats
    4.Video''')
                task = input('Task> ')

                if task.lower() == 'message':

                    def whatsappMessage(name, message):
                        startfile(
                            "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2333.8.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
                        sleep(1)
                        click(x=126, y=117)
                        write(name)

                        sleep(0.5)
                        click(x=192, y=196)
                        sleep(0.15)
                        click(x=587, y=1060)
                        write(message)
                        press('enter')

                    name = input('Name: ')
                    message = input('Message: ')

                    whatsappMessage(name, message)

                elif task.lower() == 'call':

                    def whatsappCall(name):
                        startfile(
                            "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2333.8.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
                        sleep(0.5)
                        click(x=225, y=115)
                        write(name)

                        sleep(0.5)
                        click(x=192, y=196)
                        sleep(0.15)
                        click(x=1808, y=72)

                    name = input('Name: ')
                    whatsappCall(name)

                elif task.lower() == 'chats':
                    def whatsappMessage(name):
                        startfile(
                            "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2333.8.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
                        sleep(1)
                        click(x=126, y=117)
                        write(name)

                        sleep(0.5)
                        click(x=192, y=196)

                    name = input('Name: ')
                    whatsappMessage(name)

                elif task.lower() == 'video':

                    def whatsappVideoCall(name):
                        startfile(
                            "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2333.8.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
                        sleep(1)
                        click(x=126, y=117)
                        write(name)

                        sleep(0.9)
                        click(x=192, y=196)
                        sleep(0.5)
                        click(x=1750, y=72)

                    name = input('Name: ')
                    whatsappVideoCall(name)

            elif 'space news' in query:
                print('''
    Please input the date in numbers''')
                year = input('Year: ')
                month = input('Month: ')
                day = input('day: ')

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

                    path1 = "C:\\Users\\WALTON\\PycharmProjects\\TestAIT\\" + str(fileName)
                    path2 = "C:\\Users\\WALTON\\PycharmProjects\\TestAIT\\Nasa Database\\Space Images\\" + str(
                        fileName)

                    os.rename(path1, path2)
                    img = Image.open(path2)
                    img.show()
                    print(f'{title}')
                    print(f''' {info}''')

                nasaNews(f'{year}-{month}-{day}')

            elif 'mars image' in query:
                print('''
                Please input the date in numbers''')
                year = input('Year: ')
                month = input('Month: ')
                day = input('day: ')

                apiKey = 'VoGJYdB71YZwFeubjQiy1ibx7Q1OymYlysx2cdUj'

                def marsImg(date):

                    name = 'curiosity'
                    api = str(apiKey)
                    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={api}"
                    r = requests.get(url)
                    data = r.json()
                    photos = data['photos'][:5]

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

                            path1 = 'C:\\Users\\WALTON\\PycharmProjects\\AIT\\' + str(img)
                            path2 = 'C:\\Users\\WALTON\\PycharmProjects\\AIT\\Nasa Database\\Mars Images\\' + str(
                                img)
                            os.rename(path1, path2)
                            os.startfile(path2)
                            print(
                                f'This image was captured by {rover_name} rover through {full_camera_name} or {camera_name} on {date} ')

                    except:
                        print(f'No Images have captured on {date}')

                marsImg(f'{year}-{month}-{day}')

            elif 'my location' in query:
                ipAdd = requests.get('https://api.ipify.org').text
                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                geoQ = requests.get(url)
                geoD = geoQ.json()
                latitude = geoD['latitude']
                longitude = geoD['longitude']

                print(f"Sir , You Are Now In {latitude}, {longitude}.")

            elif 'where is' in query:
                Query = query.replace('where is', '')
                Query = Query.replace('masgo', '')

                place = Query
                print(place)
                urlPlace = 'www.google.com/maps/place/' + str(place)
                web.open(url=urlPlace)

                try:

                    geolocator = Nominatim(user_agent='myGeocoder')
                    location = geolocator.geocode(place, addressdetails=True)
                    targetLocation = location.latitude, location.longitude
                    location = location.raw['address']
                    target = {'city': location.get('city', ''), 'state': location.get('state', ''),
                              'country': location.get('country', '')}
                    currentLocation = geocoder.ip('me')
                    currentLatLon = currentLocation.latlng
                    distance = str(great_circle(currentLatLon, targetLocation))
                    distance = str(distance.split(' ', 1)[0])
                    distance = round(float(distance), 2)

                    print(f'{target}')
                    speak(f'{place} is {distance}km away from you')

                except:
                    print(f'Sorry, but there is currently no location available or discovered by the name{place}')

            elif 'timetable' in query:
                from Automation import timetable
                timetable()

            elif 'image generator' in query:
                what = input('What is your requirement sir: ')

                url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

                body = {
                    "steps": 40,
                    "width": 1024,
                    "height": 1024,
                    "seed": 0,
                    "cfg_scale": 4,
                    "samples": 1,
                    "text_prompts": [
                        {
                            "text": str(what),
                            "weight": 1
                        },
                        {
                            "text": "blurry, bad",
                            "weight": -1
                        }
                    ],
                }

                headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {'sk-JmyrTq4cQItabGM1PHMs4gnWVyE2EIukZuON1ah9tqqsZC4K'}",
                }

                response = requests.post(
                    url,
                    headers=headers,
                    json=body,
                )

                if response.status_code != 200:
                    raise Exception("Non-200 response: " + str(response.text))

                data = response.json()

                # make sure the out directory exists
                if not os.path.exists("C:\\Users\\WALTON\\PycharmProjects\\AIT\\Ai Image"):
                    os.makedirs("./out")

                for i, image in enumerate(data["artifacts"]):
                    with open(f'C:\\Users\\WALTON\\PycharmProjects\\AIT\\Ai Image\\MASGOimg_{image["seed"]}.png',
                              "wb") as f:
                        f.write(base64.b64decode(image["base64"]))

            elif 'wikipedia' in query:
                print('Accessing Wikipedia')
                time.sleep(0.5)
                print('Wikipedia Accessed')
                Query = query.replace('wikipedia', '')
                result = wikipedia.search(Query)
                print(result)
                one = input('Which one would you like to choose: ')
                wiki = wikipedia.page(one, auto_suggest=False)
                print(wikipedia.summary(wiki, 3))

            # elif 'translate' in query:
            #     statement = input('Text: ')
            #     originalLanguage = input('Original Language: ').lower()
            #     translatedLanguage = input('Translated Language: ').lower()
            #
            #     translator = Translator(provider='mymemory', from_lang=originalLanguage, to_lang=translatedLanguage)
            #     translation = translator.translate(statement)
            #     print(translation)

            elif 'dictionary' in query:
                data = json.load(open('dictionary_compact.json'))
                word = input('Word: ').lower()

                if word in data:
                    print(data[word])
                else:
                    print(f'The word {word} could not ne found')

            # elif 'joke' in query:
            #     joke = pyjokes.get_joke()
            #     print(joke)

            # elif 'iss tracker' in query:
            #
            #     def issTracker():
            #         url = 'http://api.open-notify.org/iss-now.json'
            #         r = requests.get(url)
            #         data = r.json()
            #         dt = data['timestamp']
            #         latitude = data['iss_position']['latitude']
            #         longitude = data['iss_position']['longitude']
            #
            #         currentTime = datetime.datetime.now()
            #         currentDate = f'{currentTime.day}.{currentTime.month}.{currentTime.year}'
            #         exactTime = f'{currentTime.hour}:{currentTime.minute}:{currentTime.second}:{currentTime.microsecond}'
            #
            #         print(f'Time: {currentTime}')
            #         print(f'Latitude:{latitude}')
            #         print(f'Latitude:{longitude}')
            #
            #         plt.figure(figsize=(10, 8))
            #         axes = plt.axes(projection=ccrs.PlateCarree())
            #         axes.stock_img()
            #         plt.scatter(float(longitude), float(latitude), color='blue', marker='o')
            #         plt.show()
            #
            #     issTracker()

            elif 'astro' in query:

                def astro(staringDate, endingDate):
                    apiKey = 'VoGJYdB71YZwFeubjQiy1ibx7Q1OymYlysx2cdUj'
                    url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={staringDate}&end_date={endingDate}&api_key={apiKey}'

                    r = requests.get(url)
                    data = r.json()
                    totalAstro = data['element_count']
                    print(data.keys())
                    print(totalAstro)
                    neo = data['near_earth_objects']
                    print(f'Total near earth objects between {staringDate} and {endingDate} is {totalAstro}')
                    for body in neo[staringDate]:
                        id = body['id']
                        name = body['name']
                        absoluteMagnitude = body['absolute_magnitude_h']
                        # estimatedDiametre = body['estimated_diameter'] #in km
                        print(f'''
ID: {id}
Name: {name}
Absolute Magnitude: {round(absoluteMagnitude)} km
                        ''')

                print('Input the date for the starting time')
                sYear = input('Year: ')
                sMonth = input('month: ')
                sDay = input('day: ')

                print('Input the date for the ending time')
                eYear = input('Year: ')
                eMonth = input('month: ')
                eDay = input('day: ')

                possibleNumbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

                if sMonth in str(possibleNumbers):
                    sMonth = f'{0}{sMonth}'

                if eMonth in str(possibleNumbers):
                    eMonth = f'{0}{eMonth}'

                if sDay in str(possibleNumbers):
                    sDay = f'{0}{sDay}'

                if eDay in str(possibleNumbers):
                    eDay = f'{0}{eDay}'

                starting_Date = f'{sYear}-{sMonth}-{sDay}'
                ending_Date = f'{eYear}-{eMonth}-{eDay}'

                astro(starting_Date, ending_Date)

            else:
                # from bardapi import Bard
                # bard = Bard(token="bgj8FuB0V-6tj94pZWIkQc7ZMpdpkW4eYayU7QRSzjQzAMvIqAnJZCuEFlQfdLCzp1Rr_A.")
                # result = bard.get_answer(str(query))['content']
                # print(result)

                import openai
                openai.api_key = "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"

                messages = [
                    {'role': 'system',
                     'content': query}
                ]

                message = query
                if message:
                    messages.append({'role': 'user', 'content': message})
                    chat = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages)
                    reply = chat.choices[0].message.content
                    print(reply)
                    messages.append({'role': 'assistant', 'content': reply})


    tasker()

else:
    speak('Initiating Grapho AIT')
    speak('Wait a minute please')

    emailSender = 'raiyankhan242008@gmail.com'
    emailPassword = 'oqxl aiva pxva wwfv'
    emailReceiver = 'airstudiosproductions@gmail.com'

    currentTime = datetime.datetime.now()
    currentDate = f'{currentTime.day}.{currentTime.month}.{currentTime.year}'
    exactTime = f'{currentTime.hour}:{currentTime.minute}:{currentTime.second}:{currentTime.microsecond}'

    subject = 'MASGO Emergency'
    body = f'''
Hello Sir,
Someone is trying to access Grapho AIT. 
Time: {exactTime}
Date: {currentDate}
    '''

    em = EmailMessage()
    em['From'] = emailSender
    em['To'] = emailReceiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(emailSender, emailPassword)
        smtp.sendmail(emailSender, emailReceiver, em.as_string())

    speak('Permission Denied')
    speak('Mailing Sir')
