
from regular_season import *

(winning_table, wt_afc_east, wt_afc_north, wt_afc_south, wt_afc_west, 
        wt_nfc_east, wt_nfc_north, wt_nfc_south, wt_nfc_west, 
        division_winner_1_afc, division_winner_2_afc, division_winner_3_afc, division_winner_4_afc,
        division_winner_1_nfc, division_winner_2_nfc, division_winner_3_nfc, division_winner_4_nfc,
            division_wild_carders_2_nfc, division_winner_3_nfc, division_winner_4_nfc,
        division_wild_carders_1_afc, division_wild_carders_2_afc, division_wild_carders_3_afc, 
        division_wild_carders_1_nfc, division_wild_carders_2_nfc, division_wild_carders_3_nfc, 
        wild_card_matches) = season_report(generate_rand_games(seasonmatches=matches))

matches_report(generate_rand_games(seasonmatches=matches))
print('---------------------------------------')


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

# print(wild_card_matches[0])
# print(wild_card_matches[1])

# print(wild_card_matches[2])
# print(wild_card_matches[3])

# Matches of the Wild Card Round



wild_card_round = matches_report(generate_rand_games(seasonmatches=wild_card_matches))

if wild_card_round[0].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))
    wild_card_round[0].touchdown(wild_card_matches[0][j],k)
    wild_card_round_match_1_winner = wild_card_round[0].get_winning_team()[0]
else:
    wild_card_round_match_1_winner = wild_card_round[0].get_winning_team()[0]

if wild_card_round[1].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))   
    wild_card_round[1].touchdown(wild_card_matches[1][j],k)
    wild_card_round_match_2_winner = wild_card_round[1].get_winning_team()[0]
else:
    wild_card_round_match_2_winner = wild_card_round[1].get_winning_team()[0]

if wild_card_round[2].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))   
    wild_card_round[2].touchdown(wild_card_matches[0][j],k)
    wild_card_round_match_3_winner = wild_card_round[2].get_winning_team()[0]
else:
    wild_card_round_match_3_winner = wild_card_round[2].get_winning_team()[0]

if wild_card_round[3].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))
    wild_card_round[3].touchdown(wild_card_matches[0][j],k)
    wild_card_round_match_4_winner = wild_card_round[3].get_winning_team()[0]
else:
    wild_card_round_match_4_winner = wild_card_round[3].get_winning_team()[0]

# print(wild_card_round_match_1_winner)
# print(wild_card_round_match_2_winner)
# print(wild_card_round_match_3_winner)
# print(wild_card_round_match_4_winner)

afc_wild_card_table = winning_table.iloc[[winning_table[winning_table['Teams'] == wild_card_round_match_1_winner].index[0], winning_table[winning_table['Teams'] == wild_card_round_match_2_winner].index[0]],:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])

nfc_wild_card_table = winning_table.iloc[[winning_table[winning_table['Teams'] == wild_card_round_match_3_winner].index[0], winning_table[winning_table['Teams'] == wild_card_round_match_4_winner].index[0]],:].sort_values(by=['Winning matches','Losing matches','Tying matches'],
                                      ascending=[False, True, False])


divisional_round_matches = [(division_winner_1_afc,afc_wild_card_table.iloc[1,0]),
                            (division_winner_2_afc,afc_wild_card_table.iloc[0,0]),
                            (division_winner_1_nfc,nfc_wild_card_table.iloc[1,0]),
                            (division_winner_2_nfc,nfc_wild_card_table.iloc[0,0])]

print('---------------------------------------')
# Divisional Round

print('Divisional Round Matches')

divisional_round = matches_report(generate_rand_games(seasonmatches=divisional_round_matches))

if divisional_round[0].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))
    divisional_round[0].touchdown(divisional_round[0][j],k)
    divisional_round_match_1_winner = divisional_round[0].get_winning_team()[0]
else:
    divisional_round_match_1_winner = divisional_round[0].get_winning_team()[0]

if divisional_round[1].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))   
    divisional_round[1].touchdown(divisional_round[1][j],k)
    divisional_round_match_2_winner = divisional_round[1].get_winning_team()[0]
else:
    divisional_round_match_2_winner = divisional_round[1].get_winning_team()[0]

if divisional_round[2].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))   
    divisional_round[2].touchdown(divisional_matches[0][j],k)
    divisional_round_match_3_winner = divisional_round[2].get_winning_team()[0]
else:
    divisional_round_match_3_winner = divisional_round[2].get_winning_team()[0]

if divisional_round[3].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))
    divisional_round[3].touchdown(divisional_matches[0][j],k)
    divisional_round_match_4_winner = divisional_round[3].get_winning_team()[0]
else:
    divisional_round_match_4_winner = divisional_round[3].get_winning_team()[0]

conference_championship_matches = [(divisional_round_match_1_winner, divisional_round_match_2_winner),
                                    (divisional_round_match_3_winner,divisional_round_match_4_winner)]


# print(divisional_round_match_1_winner)
# print(divisional_round_match_2_winner)
# print(divisional_round_match_3_winner)
# print(divisional_round_match_4_winner)

print('---------------------------------------')

# Conference Championship

print('Conference Championship Matches:')

conference_championship_round = matches_report(generate_rand_games(seasonmatches=conference_championship_matches))


if conference_championship_round[0].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))
    conference_championship_round[0].touchdown(conference_championship_matches[0][j],k)
    conference_championship_round_match_1_winner = conference_championship_round[0].get_winning_team()[0]
else:
    conference_championship_round_match_1_winner = conference_championship_round[0].get_winning_team()[0]

if conference_championship_round[1].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))   
    conference_championship_round[1].touchdown(conference_championship_matches[1][j],k)
    conference_championship_round_match_2_winner = conference_championship_round[1].get_winning_team()[0]
else:
    conference_championship_match_2_winner = conference_championship_round[1].get_winning_team()[0]

super_bowl_match = [(conference_championship_round_match_1_winner,conference_championship_match_2_winner)]

# print(conference_championship_round_match_1_winner)
# print(conference_championship_match_2_winner)

print('---------------------------------------')

# Super Bowl

print('Super Bowl Match:')

super_bowl_round = matches_report(generate_rand_games(seasonmatches=super_bowl_match))

if super_bowl_round[0].get_winning_team()[2] != []:
    j = randint(0,1)
    k = choice(range(0,3,1))
    super_bowl_round[0].touchdown(super_bowl_match[0][j],k)
    super_bowl_winner = super_bowl_round[0].get_winning_team()[0]
else:
    super_bowl_winner = super_bowl_round[0].get_winning_team()[0]
print('-%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -')
print('The Super Bowl Winner is', super_bowl_winner)
print('-%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -')
