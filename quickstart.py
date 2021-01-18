#!/usr/bin/python3

from __future__ import print_function
import datetime
import pickle
import tzlocal
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    dirname=os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(dirname + '/token.pickle'):
        with open(dirname + '/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                dirname + '/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(dirname + '/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    todaymin = datetime.datetime.combine(datetime.date.today(), datetime.datetime.min.time()).astimezone(tzlocal.get_localzone()).isoformat()
    todaymax = datetime.datetime.combine(datetime.date.today(), datetime.datetime.max.time()).astimezone(tzlocal.get_localzone()).isoformat()
 
    # Call the Calendar API
    events_result = service.events().list(calendarId='primary', timeMin=todaymin, timeMax=todaymax, 
                                        maxResults=20, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(datetime.datetime.fromisoformat(start).strftime("%I:%M %p"), " - [[", event['summary'].replace(' (copy)', ''), "]]", sep='')

if __name__ == '__main__':
    main()
