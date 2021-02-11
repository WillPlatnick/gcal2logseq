# Google Calendar to logseq

This is a Python script and Alfred Workflow to export today's Google Calendar events and put them into logseq.

**This is very rough and not meant to be plug and play. It is completely unsupported. I just wanted to put it out there to be a base start for others.**

## Requirements

* macOS Catalina (Uses system Python 3.7
* Python 3.7
* Alfred Workflow

## Setup

git clone https://github.com/WilliamDurin/gcal2logseq.git

Go [here](https://developers.google.com/calendar/quickstart/python) and click the 'Enable the Google API' button, download the credentials.json file and stick it into the gcal-logseq directory you just checked out.

Run /usr/bin/pip3 install -r requirements.txt

Run /usr/bin/python3 quickstart.py, it should load a web page to give permissions to the app. You can ignore the insecure prompts since it's your own app.

## Alfred Workflow

I've also included an Alfred workflow. You'll have to edit the workflow and change the repopath directory on your local machine.
