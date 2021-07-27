# browser_recorder
Simple example of recording DASH activity via Python
</br>
This prototype:</br> 
<li>(1) Initalizes a Chrome browser session,</li>
<li>(2) Records for a set amount of time, </li>
<li>(3) closes browser session and saves recording as GIF</li>
<br/>
Recommendations
<br/>
<li>Use with a linux distribution</li>
<li>Use a machine with upwards of 60 GB of RAM</li>
<li>GPU used was NVIDIA GeForce GTX 1080 Ti (Unclear if required for same performance)</li>
<li>Required to get sufficient frame rate for human annotation</li>
</br> 
Quickstart directions:
<li>(1) Create Virtual Environment</li>
<li>(2) Download chromedriver for you chrome version: <a href="https://chromedriver.chromium.org/downloads">Find Here</a></li>
<li>(3) Copy compressed file to you python environment's bin directory (/env/bin/)</li>
<li>(4) Unzip compressed file to bin directory, delete compressed file</li> 
<li>(5) Alter GLOBALS to fall in line with your local directory structure.</li> 
<li>(6) Run pip install -r requirements.txt</li>
<li>(7) Run python browser_recorder.py</li>
<br/>
GIFs will be saved to browser_recorder/gifs
