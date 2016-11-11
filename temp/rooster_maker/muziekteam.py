muziek = {
    'muziekteams':[1,2],
    'muzikanten':{
        1:{
            'team': 1,
            'instrument': 'zang',
            'zangleiding': True,
        },
        2:{
            'team': 1,
            'instrument': 'zang',
            'zangleiding': True,
        },
        3:{
            'team': 1,
            'instrument': 'zang',
            'zangleiding': True,
        },
        4:{
            'team': 1,
            'instrument': 'zang',
            'zangleiding': False,
        },
        5:{
            'team': 1,
            'instrument': 'piano',
        },
        6:{
            'team': 1,
            'instrument': 'fluit',
        },
        7:{
            'team': 1,
            'instrument': 'gitaar',
        },
        8:{
            'team': 1,
            'instrument': 'basgitaar',
        },
        9:{
            'team': [1,2],
            'instrument': 'djembe',
        },
        10:{
            'team': 2,
            'instrument': 'zang',
            'zangleiding': True,
        },
        11:{
            'team': 2,
            'instrument': 'zang',
            'zangleiding': False,
        },
        12:{
            'team': 2,
            'instrument': 'piano',
        },
        13:{
            'team': 2,
            'instrument': 'fluit',
        },
        14:{
            'team': 2,
            'instrument': 'gitaar',
        },
        15:{
            'team': 2,
            'instrument': 'basgitaar',
        },
        16:{
            'team':2,
            'instrument': 'klarinet',
        },
      
    },
}
testweek = [10,12,13,14,16,9]

def is_zangleiding(muzikanten):
    x = muzikanten[muzikant]
    return x['instrument'] == 'zang' and x['zangleiding']

def in_muziekteam(muzikant, muziekteam):
    if type(muzikant['team']) == list:
        return muziekteam in muzikant['team']
    else:
        return muzikant['team'] == muziekteam

def instrumenten(muzikanten, team):
    instrumenten = []
    for muzikant in muzikanten:
        if type(muzikanten[muzikant]['team']) == list:
            if team in muzikanten[muzikant]['team']:
                instrumenten.append(muzikanten[muzikant]['instrument'])
        elif muzikanten[muzikant]['team'] == team:
            instrumenten.append(muzikanten[muzikant]['instrument'])
    return set(instrumenten)

def is_mogelijk(muziek, week):
    kunnen = []
    for muziekteam in muziek['muziekteams']:
        instrumenten_muziekteam = instrumenten(muziek['muzikanten'], muziekteam)
        print(instrumenten_muziekteam)
        huidige_week = []
        for muzikant in week:
            huidige_muzikant = muziek['muzikanten'][muzikant]
            if in_muziekteam(huidige_muzikant, muziekteam):
                if huidige_muzikant['instrument'] == 'zang':
                    if huidige_muzikant['zangleiding']:
                        huidige_week.append(huidige_muzikant['instrument'])
                else:
                    huidige_week.append(huidige_muzikant['instrument'])
        if len(set(huidige_week)) == len(instrumenten_muziekteam):
            kunnen.append(muziekteam)
    return kunnen
    

x = instrumenten(muziek['muzikanten'], 1)
y = is_mogelijk(muziek, testweek)
print(y)
