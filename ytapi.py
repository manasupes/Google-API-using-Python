from googleapiclient.discovery import build

api_key = '#collect it from google api'

youtube = build('youtube', 'v3',developerKey=api_key)

request = youtube.channels().list(
		part='statistics',
		forUsername='#your User Name'
		)

response = request.execute()
print(response)