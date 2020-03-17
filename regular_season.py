from possible_values import *
from matches import *
from game import Game
from random import sample, randint, random
import pandas as pd


def generate_rand_games(n=len(matches)):
    '''
    Generate the games of the regular season.
    '''

    # Begin with a empy list
    games = []

    for i in range(len(matches)):
        game = Game(teams=matches[i])

        #Score Touchdowns
        if (random() < 0.45):
            for _ in list(range(3)):
                j_1 = randint(0,1)
                k = randint(1,2)
                game.touchdown(game.teams[j_1],k)
        elif (random() >= 0.45) & (random() < 0.9):
            for _ in list(range(4)):
                j_1 = randint(0,1)
                k = randint(1,2)
                game.touchdown(game.teams[j_1],k)
        else:
            for _ in list(range(5)):
                j_1 = randint(0,1)
                k = randint(1,2)
                game.touchdown(game.teams[j_1],k)
        
        #Score Field Goals
        if (random() < 0.6):
            for _ in list(range(2)):
                j_2 = randint(0,1)
                game.field_goal(game.teams[j_2])
        elif (random() >= 0.6) & (random() < 0.9):
            for _ in list(range(3)):
                j_2 = randint(0,1)           
        else:
            for _ in list(range(4)):
                j_2 = randint(0,1)
                game.field_goal(game.teams[j_2])
        #Score Safety Points
        if random() > 0.9999:
            j_3 = randint(0,1)
            game.safety(game.teams[j_3])
        games.append(game)
    return games    



def season_report(games):
    '''
    Print out the report season.
    '''
    winning_teams = []
    losing_teams = []
    winning_scores = []
    losing_scores = []

    # Setting winning teams and losing teams sets. 
    for game in games:
        winning_team, losing_team = game.get_winning_team()
        winning_teams.append(winning_team)
        losing_teams.append(losing_team)
    
    # Count victories and loses from each team.
    for team in teams_name:
        winning_scores.append(winning_teams.count(team))
        losing_scores.append(losing_teams.count(team))

    winning_table = {'Teams':teams_name, 'Winning matches': winning_scores,
                         'Losing matches': losing_scores}                   

    # Print results. 
    print(pd.DataFrame.from_dict(winning_table))


if __name__ == "__main__":
    season_report(generate_rand_games())











