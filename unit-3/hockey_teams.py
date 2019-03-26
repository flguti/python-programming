class HockeyTeam:
    def __init__(self, name, division, conference):
        self.name = name
        self.division = division
        self.conference = conference
        self.roster = []


    def add_player(self, player):
        self.roster.append(player)

    def remove_player(self, player_name):
        pass

    def get_roster(self):
        pass
    
    def __repr__(self):
        return ''

def print_menu():
   print("1. Create hockey team")
   print("2. Add player to a team roster")
   print("3. Remove player from a team roster")
   print("4. Show team roster")

def main():
    hockey_teams = []
    #print menu
    n = 0
    while n != 'q':
        print_menu()
        n = input('Enter menu option (q to quit)')
        if n == '1':
            name, division, conference = input('please enter Team name, division and Conference (separeted by come)  :').split(',')
            team = HockeyTeam(name, division, conference)
            hockey_teams.append(team)
            #print(hockey_teams)
        elif n == '2':
            name, pos, num = input('Enter player\'s name, position, number (comma separated)  :').split(',')
            player = {}
            player['player_name'] = name
            player['position'] = pos
            player['shirt_number'] = num
            team_name = input('Enter team name to add player to:  ')

            for idx, team in enumerate(hockey_teams):
                # try:
                    if team['name'] == team_name:
                        hockey_teams[idx].add_player(player)
                # except ValueError:
                #     print('Team does not exist')
        if n == '3':
            HockeyTeam.remove_player()
        if n == '4':
            HockeyTeam.get_roster()
        #if n != '1' and n != '2' and n != '3' and n != 'q':
        #    print('Wrong value, read carefully the menu')
    

if __name__ == "__main__":
   main()