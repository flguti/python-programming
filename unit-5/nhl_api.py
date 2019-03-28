import requests

#https://statsapi.web.nhl.com/api/v1/teams

response = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

team_list = response.json()

print(team_list)