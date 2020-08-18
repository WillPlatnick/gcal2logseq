# Google Calendar to Roam

This is a Python script and Alfred Workflow to export today's Google Calendar events and put them into Roam.

**This is very rough and not meant to be plug and play. It is completely unsupported. I just wanted to put it out there to be a base start for others.**

Demo Video:

[![Demo Video](https://img.youtube.com/vi/x4id7c5jtTk/0.jpg)](https://youtu.be/x4id7c5jtTk)

## Requirements

* macOS Catalina (Uses system Python 3.7
* Python 3.7
* Alfred Workflow

## Setup

git clone https://github.com/WilliamDurin/gcal-roam.git

Go [here](https://developers.google.com/calendar/quickstart/python) and click the 'Enable the Google API' button, download the credentials.json file and stick it into the gcal-roam directory you just checked out.

Run /usr/bin/pip3 -r requirements.txt

Run /usr/bin/python3 quickstart.py, it should load a web page to give permissions to the app. You can ignore the insecure prompts since it's your own app.

## Alfred Workflow

I've also included an Alfred workflow. You'll have to edit the workflow and change it to the gcal-roam directory on your local machine.
