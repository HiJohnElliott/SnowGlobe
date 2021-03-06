from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def calCall():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='eqj36jc3hpir07lmd85puarpok@group.calendar.google.com', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    else: return events
    # for event in events:
    #     # print(event.keys())
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     summary = event['summary']
    #     location = event['location']
    # 	# print(start, event['summary'])
    # 	# print(event['location'])
    # 	#print('\n')
    # 	# except: 
    # 		# print(start, event['summary'])
    # 		# print('No Location')		
	

        

if __name__ == '__main__':
    calCall()
    print(calCall)
