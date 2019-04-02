import requests

#https://statsapi.web.nhl.com/api/v1/teams

response = requests.get('https://statsapi.web.nhl.com/api/v1/teams/5/stats')

team_list = response.json()

print(team_list)