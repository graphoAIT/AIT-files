import time
from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
# from notifypy import Notify
from datetime import date

from Database.Timetable.Sunday import time as suntime
from Database.Timetable.Monday import time as montime
from Database.Timetable.Tuesday import time as tuestime
from Database.Timetable.Wednesday import time as wedtime
from Database.Timetable.Thursday import time as thurstime
from Database.Timetable.Saturday import time as sattime


def whatsappMessage(name, message):
    startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2321.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(1)
    click(x=126, y=117)
    write(name)

    sleep(0.5)
    click(x=192, y=196)
    sleep(0.15)
    click(x=587, y=1060)
    write(message)
    press('enter')


def whatsappCall(name):
    startfile("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2321.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(0.5)
    click(x=225, y=115)
    write(name)

    sleep(0.25)
    click(x=192, y=196)
    sleep(0.15)
    click(x=1808, y=72)


def whatsappChat(name):
    startfile(
        "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2321.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(1)
    click(x=126, y=117)
    write(name)

    sleep(0.5)
    click(x=192, y=196)


def whatsappVideoCall(name):
    startfile(
        "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2321.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe")
    sleep(1)
    click(x=126, y=117)
    write(name)

    sleep(0.5)
    click(x=192, y=196)
    sleep(0.15)
    click(x=1750, y=72)


def timetable():
    print('Checking your Timetable...')
    time.sleep(1)

    if date.today().weekday() == 5:
        suntime()

    elif date.today().weekday() == 0:
        montime()

    elif date.today().weekday() == 1:
        tuestime()

    elif date.today().weekday() == 2:
        wedtime()

    elif date.today().weekday() == 3:
        thurstime()

    elif date.today().weekday() == 5:
        sattime()



