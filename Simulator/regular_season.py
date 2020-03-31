from possible_values import *
from matches import *
from game import Game
from random import sample, randint, random, choice
import pandas as pd


def generate_rand_games(seasonmatches):
    '''
    Generate the games of the regular season.
    '''

    # Begin with a empy list
    games = []

    for i in range(len(seasonmatches)):
        game = Game(teams=seasonmatches[i])

        #Score Touchdowns
        randomness = random()
        if (randomness < 0.45):
            for _ in list(range(3)):
                j_1 = randint(0,1)
                k = choice(range(0,3,1)) 
                game.touchdown(game.teams[j_1],k)
        elif (randomness >= 0.45) & (random() < 0.9):
            for _ in list(range(4)):
                j_1 = randint(0,1)
                k = choice(range(0,3,1)) 
                game.touchdown(game.teams[j_1],k)
        else:
            for _ in list(range(5)):
                j_1 = randint(0,1)
                k = choice(range(0,3,1)) 
                game.touchdown(game.teams[j_1],k)
        
        #Score Field Goals
        randomness = random()
        if (randomness < 0.6):
            for _ in list(range(2)):
                j_2 = randint(0,1)
                game.field_goal(game.teams[j_2])
        elif (randomness >= 0.6) & (randomness < 0.9):
            for _ in list(range(3)):
                j_2 = randint(0,1)           
        else:
            for _ in list(range(4)):
                j_2 = randint(0,1)
                game.field_goal(game.teams[j_2])

        #Score Safety Points
        randomness = random()
        if randomness > 0.9999:
            j_3 = randint(0,1)
            game.safety(game.teams[j_3])

        #Overtime because tie
        if game.score[game.teams[0]] == game.score[game.teams[1]]:
            randomness = random()
            if randomness > 0.2:
                i = randint(0,1)
                k = choice(range(0,3,1)) 
                game.touchdown(game.teams[i],k) 

        games.append(game)
    return games    

# breakpoint()

def matches_report(games):
    for match in games:
        print(match.score)
    return games


def season_report(games):
    '''
    Print out the report season.
    '''
    winning_teams = []
    losing_teams = []
    tying_teams = []
    winning_scores = []
    losing_scores = []
    tying_scores = []

    # Setting winning teams and losing teams sets. 
    for game in games:
        winning_team, losing_team, tying_team = game.get_winning_team()
        winning_teams.append(winning_team)
        losing_teams.append(losing_team)
        tying_teams.extend(tying_team)


    # Count victories, loses and ties from each team.
    for team in teams_name:
        winning_scores.append(winning_teams.count(team))
        losing_scores.append(losing_teams.count(team))
        tying_scores.append(tying_teams.count(team))


    winning_dict = {'Teams':teams_name, 'Winning matches': winning_scores,
                         'Losing matches': losing_scores,
                         'Tying matches': tying_scores}                   

    # Locating each team in the global position,
    # # to display the division position table.

    afc_east_global_positions=[]
    afc_north_global_positions=[]
    afc_south_global_positions=[]
    afc_west_global_positions=[]
    nfc_east_global_positions=[]
    nfc_north_global_positions=[]
    nfc_south_global_positions=[]
    nfc_west_global_positions=[]


    for i, team in enumerate(list(winning_dict['Teams'])):
        if team in afc_east:
            afc_east_global_positions.append(i)

    for i, team in enumerate(list(winning_dict['Teams'])):
        if team in afc_north:
            afc_north_global_positions.append(i)

    for i, team in enumerate(list(winning_dict['Teams'])):
        if team in afc_south:
            afc_south_global_positions.append(i)

    for i, team in enumerate(list(winning_dict['Teams'])):
        if team in afc_west:
            afc_west_global_positions.append(i)

    for i, team in enumerate(list(winning_dict['Teams'])):
        if team in nfc_east:
            nfc_east_global_positions.append(i)

    for i, team in enumerate(list(winning_dict['Teams'])):
        if team in nfc_north:
            nfc_north_global_positions.append(i)

    for i, team in enumerate(list(winning_dict['Teams'])):
        if team in nfc_south:
            nfc_south_global_positions.append(i)

    for i, team in enumerate(list(winning_dict['Teams'])):
        if team in nfc_west:
            nfc_west_global_positions.append(i)
    
 
    
    winning_table = pd.DataFrame.from_dict(winning_dict)
    
    # Winning tables per division
    
    wt_afc_east = winning_table.iloc[afc_east_global_positions,:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])
    wt_afc_north = winning_table.iloc[afc_north_global_positions,:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])
    wt_afc_south = winning_table.iloc[afc_south_global_positions,:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])
    wt_afc_west = winning_table.iloc[afc_west_global_positions,:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])

    wt_nfc_east = winning_table.iloc[nfc_east_global_positions,:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])
    wt_nfc_north = winning_table.iloc[nfc_north_global_positions,:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])
    wt_nfc_south = winning_table.iloc[nfc_south_global_positions,:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])
    wt_nfc_west = winning_table.iloc[nfc_west_global_positions,:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])
    # Division winners:

    division_winners_afc = []
    division_winners_nfc = []

    for division in [wt_afc_east, wt_afc_north, wt_afc_south, wt_afc_west]:
        division_winners_afc.append(division.iloc[0,:])
    for division in [wt_nfc_east,wt_nfc_north,wt_nfc_south,wt_nfc_west]:
        division_winners_nfc.append(division.iloc[0,:])

    division_winners_afc = pd.DataFrame(division_winners_afc).sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])
    division_winners_nfc = pd.DataFrame(division_winners_nfc).sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])


    division_winner_1_afc = division_winners_afc.iloc[0,0]
    division_winner_2_afc = division_winners_afc.iloc[1,0]
    division_winner_3_afc = division_winners_afc.iloc[2,0]
    division_winner_4_afc = division_winners_afc.iloc[3,0]

    division_winner_1_nfc = division_winners_nfc.iloc[0,0]
    division_winner_2_nfc = division_winners_nfc.iloc[1,0]
    division_winner_3_nfc = division_winners_nfc.iloc[2,0]
    division_winner_4_nfc = division_winners_nfc.iloc[3,0]

    division_wild_carders_afc = []
    division_wild_carders_nfc = []
    
    for division in [wt_afc_east,wt_afc_north,wt_afc_south,wt_afc_west]:
        division_wild_carders_afc.append(division.iloc[1,:])
    for division in [wt_nfc_east,wt_nfc_north,wt_nfc_south,wt_nfc_west]:
        division_wild_carders_nfc.append(division.iloc[1,:])    

    division_wild_carders_afc = pd.DataFrame(division_wild_carders_afc).sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])
    division_wild_carders_nfc = pd.DataFrame(division_wild_carders_nfc).sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])

    division_wild_carders_1_afc = division_wild_carders_afc.iloc[0,0]
    division_wild_carders_2_afc = division_wild_carders_afc.iloc[1,0]
    division_wild_carders_3_afc = division_wild_carders_afc.iloc[2,0]


    division_wild_carders_1_nfc = division_wild_carders_nfc.iloc[0,0]
    division_wild_carders_2_nfc = division_wild_carders_nfc.iloc[1,0]
    division_wild_carders_3_nfc = division_wild_carders_nfc.iloc[2,0]

    wild_card_matches = [(division_winner_4_afc, division_wild_carders_1_afc),(division_winner_3_afc, division_wild_carders_2_afc),(division_winner_4_nfc, division_wild_carders_1_nfc),(division_winner_3_nfc, division_wild_carders_2_nfc)]
    
    return (winning_table, wt_afc_east, wt_afc_north, wt_afc_south, wt_afc_west, 
            wt_nfc_east, wt_nfc_north, wt_nfc_south, wt_nfc_west, 
            division_winner_1_afc, division_winner_2_afc, division_winner_3_afc, division_winner_4_afc,
            division_winner_1_nfc, division_winner_2_nfc, division_winner_3_nfc, division_winner_4_nfc,
             division_wild_carders_2_nfc, division_winner_3_nfc, division_winner_4_nfc,
            division_wild_carders_1_afc, division_wild_carders_2_afc, division_wild_carders_3_afc, 
            division_wild_carders_1_nfc, division_wild_carders_2_nfc, division_wild_carders_3_nfc, 
            wild_card_matches)



if __name__ == "__main__":
    matches_report(generate_rand_games(seasonmatches=matches))
    print('---------------------------------------')
    (winning_table, wt_afc_east, wt_afc_north, wt_afc_south, wt_afc_west, 
            wt_nfc_east, wt_nfc_north, wt_nfc_south, wt_nfc_west, 
            division_winner_1_afc, division_winner_2_afc, division_winner_3_afc, division_winner_4_afc,
            division_winner_1_nfc, division_winner_2_nfc, division_winner_3_nfc, division_winner_4_nfc,
             division_wild_carders_2_nfc, division_winner_3_nfc, division_winner_4_nfc,
            division_wild_carders_1_afc, division_wild_carders_2_afc, division_wild_carders_3_afc, 
            division_wild_carders_1_nfc, division_wild_carders_2_nfc, division_wild_carders_3_nfc, 
            wild_card_matches) = season_report(generate_rand_games(seasonmatches=matches))

    print('Winning tables per division:')

    print(wt_afc_east)
    print(wt_afc_north)
    print(wt_afc_south)
    print(wt_afc_west)

    print(wt_nfc_east)
    print(wt_nfc_north)
    print(wt_nfc_south)
    print(wt_nfc_west)

    print('---------------------------------------')

    print('Wild Card Round Matches:')

    print(wild_card_matches[0])
    print(wild_card_matches[1])

    print(wild_card_matches[2])
    print(wild_card_matches[3])

    print('---------------------------------------')












