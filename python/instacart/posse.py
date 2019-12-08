import requests

ENDPOINT = 'http://enigmatic-hamlet-4927.herokuapp.com/posse'

LETTER_SETS = {
    0: (ord('Ü'), ord('u'), ord('U')),
    1: (ord('Ö'), ord('o'), ord('O')),
    2: (ord('Ä'), ord('a'), ord('A')),
}

THIRD_CASE = (ord('Ü'), ord('Ö'), ord('Ä'))


def start_posse():
    print('start_posse')
    r = requests.post(ENDPOINT)
    return r.json()


def submit_posse(game_id, posse):
    r = requests.post('%s/%s' % (ENDPOINT, game_id), json = {
        'posse': posse
    })
    print(r)
    return r.json()


def is_valid_posse(posse: 'Tuple'):
    """Test validity of a single posse
    """
    # todo: write this as iterator through test types
    # could use test types as blocks for lambda calculus
    # for test in attribute tests:

    # print('testing posse: %s' % str(posse))

    prefixes = set()
    cases = set()
    lengths = set()
    letters = set()

    for member in posse:
        # prefix validity
        prefixes.add(member[0])

        # case validity
        if ord(member[1]) in THIRD_CASE:
            cases.add(2)
        elif member[1].isupper():
            cases.add(1)
        else:
            cases.add(0)

        # length validity
        lengths.add(len(member[1:]))

        # letter validity
        # print('letter validity for %s' % member)
        for letter_type in LETTER_SETS:
            if ord(member[1]) in LETTER_SETS[letter_type]:
                letters.add(letter_type)

    prefix_is_valid = len(prefixes) == 1 or len(prefixes) == 3
    case_is_valid = len(cases) == 1 or len(cases) == 3
    length_is_valid = len(lengths) == 1 or len(lengths) == 3
    letter_is_valid = len(letters) == 1 or len(letters) == 3

    # print('prefix_is_valid: %s' % prefix_is_valid)
    # print('case_is_valid: %s' % case_is_valid)
    # print('length_is_valid: %s' % length_is_valid)
    # print('letter_is_valid: %s' % letter_is_valid)

    return all((prefix_is_valid,
               case_is_valid,
               length_is_valid,
               letter_is_valid))


def find_valid_posse(board: 'List') -> 'List':
    """Get a valid posse from a board

    Naive strat: triply nested loop
    Real strat: combinator - remember how to implement
    """
    for i, a in enumerate(board):
        for j, b in enumerate(board):
            if j != i:
                for k, c in enumerate(board):
                    if k not in (i, j) and \
                       is_valid_posse((a, b, c)):
                            # print((i, j, k))
                            return [a, b, c]


def play_posse():
    game = start_posse()

    while 'password' not in game:
        print('playing posse')
        posse = find_valid_posse(game['board'])
        response = submit_posse(game['id'], posse)
        if 'board' in response:
            game['board'] = response['board']
        elif 'password' in response:
            game['password'] = response['password']
        print(game)

    return game['password']

# print(is_valid_posse(('=aa', '=uuu', '=o')))
