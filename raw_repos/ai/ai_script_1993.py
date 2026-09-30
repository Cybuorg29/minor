# define a class to manage a sports team
class SportsTeam:
    def __init__(self, name):
        # store the team name
        self.name = name
        # create an empty list for team members
        self.team_members = []

    # create a method to add a new player to the team
    def add_player(self, player_name):
        if player_name not in self.team_members:
            self.team_members.append(player_name)
    
    # create a method to remove a player from the team
    def remove_player(self, player_name):
        if player_name in self.team_members:
            self.team_members.remove(player_name)