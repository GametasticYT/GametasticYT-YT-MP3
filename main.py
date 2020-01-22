# Youtube MP3 Downloader v0.2
import os
import os.path
import tkinter as tk
import urllib.request
from bs4 import BeautifulSoup
import PySimpleGUI as sg

def search_to_url(search):
    query = urllib.parse.quote(search)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    counter = 0
    for vid in soup.find_all(attrs={"class": "yt-uix-tile-link"}):
        if counter < 1:
            counter = counter + 1
            global final_url
            final_url = str("https://www.youtube.com" + vid["href"])
            os.system(
                "youtube-dl -o output/%(title)s-%(id)s.%(ext)s --no-playlist --playlist-items 1 -x --audio-format mp3 "
                + final_url
            )

sg.theme('DarkAmber')

layout = [
    [sg.InputText()],
    [sg.Button('Download'), sg.Button('Exit')],    
]

window = sg.Window('Youtube MP3 Downloader', layout)

while True:
    event, inputValue = window.read()
    if event in(None, 'Exit'):
        break
    search_to_url(inputValue[0])

