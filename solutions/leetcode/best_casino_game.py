from collections import namedtuple, defaultdict
Game = namedtuple("Game", ["name", "outcomes"])
# test cases
# Breakeven, EV = 0
g1 = Game("Breakeven Steven", ((0.5, 20), (0.5, -20)))

# EV = -0.1
g2 = Game("Go big or go home", ((0.99, -10), (0.01, 980)))

# EV = -0.2
g3 = Game("Steady Eddy", ((0.51, -10), (0.49, 10)))

# EV = -20
g4 = Game("The staircase", ((0.75, -100), (0.10, 100),
                            (0.05, 200),(0.05, 300),
                            (0.05, 400)))

def find_best_game(games):
    '''
    sample class:
    Game = namedtuple("Game", ["name", ('outcome', 'outcome')])
    Test 1:
    games ['']
    test.assert_equals(find_best_game((g1, g2)), "Breakeven Steven"
    '''
    '''
    INITIALIZE  name, outcomes variables
        name: str
        outcomes: tuple(tuple)
    CREATE game_odds dictionary:
        game_odds = defaultdict(int)
    FOR outcome in outcomes:
        outcome: (percent, value)
        percent: int
        value: int
    FOR each outcome:
        multiply each value by its percent
        expected value: int: sum all outcome
        INPUT each game name as key: 
            {'game': 'expected value'}
    return max 
    '''
    game_odds = defaultdict(int)
    for game in games:
        name = game[0]
        outcomes = game[1]
        ev = 0
        for outcome in outcomes:
            # round 1:(0.5, 20)
            # round 2:(0.5, -20)
            ev += outcome[0] * outcome[1]
        game_odds[name] = ev
    # return the max expected value game
    return max(game_odds, key= game_odds.get)


print(find_best_game((g1, g2)))