#All NFL teams

teams_name = [
'Arizona Cardinals',
'Atlanta Falcons',
'Baltimore Ravens',
'Buffalo Bills',
'Carolina Panthers',
'Chicago Bears',
'Cincinnati Bengals',
'Cleveland Browns',
'Dallas Cowboys',
'Denver Broncos',
'Detroit Lions',
'Green Bay Packers',
'Houston Texans',
'Indianapolis Colts',
'Jacksonville Jaguars',
'Kansas City Chiefs',
'Los Angeles Chargers',
'Los Angeles Rams',
'Miami Dolphins',
'Minnesota Vikings',
'New England Patriots',
'New Orleans Saints',
'New York Giants',
'New York Jets',
'Oakland Raiders',
'Philadelphia Eagles',
'Pittsburgh Steelers',
'San Francisco 49ers',
'Seattle Seahawks',
'Tampa Bay Buccaneers',
'Tennessee Titans',
'Washington Redskins'
]

#Grouped Teams by conference and division.

''' The AFC stands for the American Football Conference '''

divisions_list_afc = ['afc_east', 'afc_north', 'afc_south', 'afc_west']


afc_east = [
'Buffalo Bills',
'Miami Dolphins',
'New England Patriots',
'New York Jets'
]

afc_north = [
'Baltimore Ravens',
'Cincinnati Bengals',
'Cleveland Browns',
'Pittsburgh Steelers'
]

afc_south = [
'Houston Texans',
'Indianapolis Colts',
'Jacksonville Jaguars',
'Tennessee Titans'
]

afc_west = [
'Denver Broncos',
'Kansas City Chiefs',
'Oakland Raiders',
'Los Angeles Chargers',
]

division_list_afc = [afc_east, afc_north, afc_south, afc_west]

''' The NFC stands for the National Football Conference '''

divisions_list_nfc = ['nfc_east', 'nfc_north', 'nfc_south', 'nfc_west']

nfc_east = [
'Dallas Cowboys',
'New York Giants',
'Philadelphia Eagles',
'Washington Redskins'
]

nfc_north = [
'Chicago Bears',
'Detroit Lions',
'Green Bay Packers',
'Minnesota Vikings'
]

nfc_south = [
'Atlanta Falcons',
'Carolina Panthers',
'New Orleans Saints',
'Tampa Bay Buccaneers',
]

nfc_west = [
'Arizona Cardinals',
'Los Angeles Rams',
'San Francisco 49ers',
'Seattle Seahawks',
]

division_list_nfc = [nfc_east, nfc_north, nfc_south, nfc_west]

if __name__ == "__main__":
    print('The AFC stands for the American Football Conference and their divisions are:')
    print('East')
    print(afc_east)
    print('North')
    print(afc_north)
    print('South')
    print(afc_south)
    print('West')
    print(afc_west)
    print('-------------------------------------------------------------------------------')
    print('The NFC stands for the National Football Conference and their divisions are:')
    print('East')
    print(nfc_east)
    print('North')
    print(nfc_north)
    print('South')
    print(nfc_south)
    print('West')
    print(nfc_west)