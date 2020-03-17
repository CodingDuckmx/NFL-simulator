#NFL-simulator/matches.py

from random import sample,shuffle
from possible_values import *
from itertools import permutations, product

# List whose are goint to be used. 
matches = []
matches_afc = []
matches_nfc = []
matches_other_division = []
matches_other_conference = []
matches_dbly = []

# Listing the division of the conferences:
division_list_afc = [afc_east, afc_north, afc_south, afc_west]

division_list_nfc = [nfc_east, nfc_north, nfc_south, nfc_west]

# Matches inside the division.
for team in division_list_afc:
    matches_afc.extend(list(permutations(team,2)))

for team in division_list_nfc:
    matches_nfc.extend(list(permutations(team,2)))   


matches.extend(matches_afc)
matches.extend(matches_nfc)

# Matches with other division inside the same conference.

matches_other_division_afc1 = list(product(afc_east,afc_north))
for match in matches_other_division_afc1:
    matches_other_division.append(match)

matches_other_division_afc2 = list(product(afc_south,afc_west))
for match in matches_other_division_afc2:
    matches_other_division.append(match)

matches_other_division_nfc1 = list(product(nfc_east,nfc_north))
for match in matches_other_division_nfc1:
    matches_other_division.append(match)

matches_other_division_nfc2 = list(product(nfc_south,nfc_west))
for match in matches_other_division_nfc2:
    matches_other_division.append(match)

# Matches with a division of the opposite conference:

matches_other_conference_1 = list(product(afc_east,nfc_north))
for match in matches_other_conference_1:
    matches_other_division.append(match)

matches_other_conference_2 = list(product(afc_north,nfc_south))
for match in matches_other_conference_2:
    matches_other_division.append(match)

matches_other_conference_3 = list(product(afc_south,nfc_west))
for match in matches_other_conference_3:
    matches_other_division.append(match)

matches_other_conference_4 = list(product(afc_west,nfc_east))
for match in matches_other_conference_4:
    matches_other_division.append(match)

matches.extend(matches_other_division)
matches.extend(matches_other_conference)

# Interconference games determined by last year's standings.

for i in list(range(4)):
    matches_dbly.append((division_list_afc[0][i],division_list_afc[2][i]))
    matches_dbly.append((division_list_afc[0][i],division_list_afc[3][i]))
    matches_dbly.append((division_list_afc[0][i],division_list_afc[2][i]))
    matches_dbly.append((division_list_nfc[0][i],division_list_nfc[3][i]))

matches.extend(matches_dbly)


if __name__ == "__main__":
    for i in range(len(matches)):
        print(matches[i])
    print('Number of matches: ', len(matches))    


