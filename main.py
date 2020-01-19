# Youtube MP3 Downloader v0.1

import os
import os.path
import tkinter as tk
import urllib.request
from bs4 import BeautifulSoup


final_url = 0


def search_to_url():
    query = urllib.parse.quote(inputValue)
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


inputValue = 0

root = tk.Tk()
#root.geometry("700x100")
root.title("Youtube Downloader")


def get_input():
    global inputValue
    inputValue = textBox.get("1.0", "end-1c")
    search_to_url()



textBox = tk.Text(root, height=1, width=50)
textBox.grid(row=3, column=1)


buttonCommit = tk.Button(
    root, height=1, width=10, text="Download", command=lambda: get_input()
)
buttonCommit.grid(row=4, column=1)
root.grid_rowconfigure(4, minsize=100)
tk.mainloop()
