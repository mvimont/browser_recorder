# browser_recorder
Simple example of recording DASH activity via Python

This prototype (1) Initalizes a Chrome browser session, (2) Records for a set amount of time, (3) closes browser session and saves recording as GIF

Python env has been included so that prototype can run out of the box. Requires manual installation of Selenium's Chrome driver to /env/bin directory

Quickstart directions:
(1) Alter GLOBALS to fall in line with your local directory structure. 
(2) If running on Mac, you will need to run the following: xattr -d com.apple.quarantine ${PATH_TO_PROJECT}/env/bin/chromedriver
    (Not tested on other OS)
(3) Run pip install -r requirements.txt
(4) Run python browser_recorder.py

GIFs will be saved to browser_recorder/gifs
