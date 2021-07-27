from selenium import webdriver
import time
import os
import imageio
import re
import glob

#GLOBALS
DASH_URL= "file:///home/michael/dash/index.html"
RECORDING_TIME = 10
IMG_DIR = "/home/michael/browser_recorder/imgs"
GIF_DIR = "/home/michael/browser_recorder/gifs"
GIF_FILENAME = "test1.gif"

#Create browser object, set kind to google chrome
browser = webdriver.Chrome()

#Open to DASH
browser.get(DASH_URL)

start_time = time.time()
counter = 0
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    counter += 1
    browser.get_screenshot_as_file(f"{IMG_DIR}/{counter}.png")
    if elapsed_time >= RECORDING_TIME:
        break
browser.close()

image_files = os.listdir(IMG_DIR)
image_files.sort(key=lambda f: int(re.sub('\D', '', f)))

gif = []
with imageio.get_writer(f"{GIF_DIR}/{GIF_FILENAME}", mode='I') as writer:
    for file in image_files:
        image = imageio.imread(f"{IMG_DIR}/{file}")
        writer.append_data(image)

files = glob.glob(f"{IMG_DIR}/*")
for f in files:
    os.remove(f)
