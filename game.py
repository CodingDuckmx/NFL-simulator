# football/game_1.py

from possible_values import *
from random import randint

class Game:
    '''
    Models a football game.

    Parameters:
    ---------------------------
    teams: list
        list of two strings of team_names_1 
    score: dict
        key = team name
        value = score for the team
    
    '''

    def __init__(self, teams=None, score=None):
        self.teams = teams
        if teams and not score:
            self.score = {self.teams[0]:0, self.teams[1]:0}
        else:
            self.score = score

    def touchdown(self, team, extra_point=1):
        '''
        Records touchdown for the team
        ---------------------------
        Parameters:
        team: str
            team that scored
        extra points: int
            extrapoints earned in extra point play
        '''
        if team not in self.teams:
            raise ValueError('Team must be in the game')
        else:
            self.score[team] += (6 + extra_point)

    def field_goal(self, team):
        '''
        Records field goals for a team
        ---------------------------
        Parameters
        team: str
            team that scored
        '''
        if team not in self.teams:
            raise ValueError('Team must be in the game')
        else:
            self.score[team] += 3    

    def safety(self, team):
        '''
        record safety points for the other team
        ---------------------------
        Parameters
        team: str
            team who made the mistake
        '''        t_o_g = [self.teams[0],self.teams[1]]
        for p, o in enumerate(t_o_g):
            if o == team:
                del t_o_g[p]
                break

        if team not in self.teams:
            raise ValueError('Team must be in the game')
        else:
            self.score[t_o_g[0]] += 2    

    def get_winning_team(self):
        '''
        When game is done, this can be run to add attributes
        winning_team_ and losing_team_ to the game to easily
        see who won
        '''
    # If it's a tie, let's randomly break that tie and say one
    # team scored a touchdown in over time...
        if self.score[self.teams[0]] == self.score[self.teams[1]]:
            i = randint(0,1)
            self.touchdown(self.teams[i])

        v = list(self.score.values())
        k = list(self.score.keys())
        self.winning_team_ = k[v.index(max(v))]
        self.losing_team_ = k[v.index(min(v))]   

        return self.winning_team_, self.losing_team_  
        







                