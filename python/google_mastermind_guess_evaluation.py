# Please use this Google doc to code during your interview. To free your hands for coding, we recommend that you use a headset or a phone with speaker option.

# Hidden: 1234
# Guess: 1122
# Score: B W

# hidden: 1221
# guess: 2222
# score: BB

# New guess: 3333
# false
# new guess: 2222
# false
# new guess: 1122
# true

import collections


def generate_score(hidden: 'String', guess: 'String') -> 'String':
    """Return mastermind scoring string.
        Strategy: build frequency count of hidden string
                iterate through guess
    either mark correct(black)
    or correct color(white, decrement color frequency)
    """
    score = ''
    hidden_freq = collections.defaultdict(int)
    for h in hidden:
        hidden_freq[h] += 1

    for i, char in enumerate(guess):
        if char == hidden[i]:
            score += 'B'
            hidden_freq[char] -= 1

    for char in guess:
        if char in hidden_freq and hidden_freq[char] > 0:
            score += 'W'
            hidden_freq[char] -= 1

    return score


# =========
# Next step:
# given: previous guess, score
# determine: *WHETHER* new guess X can possibly be correct


def is_valid_guess(old_guess: 'String', new_guess: 'String', score: 'String'):

    black_count = 0
    white_count = 0

    # invalid case: same incorrect guess
    if len(score) != len(old_guess) and \
       'W' not in score and \
       old_guess == new_guess:
        return False

    for char in score:
        if char == 'B':
            black_count += 1
        else:
            white_count += 1

    pintersection = 0
    unmoved_count = 0
    for i, char in enumerate(new_guess):
        if char in old_guess:
            pintersection += 1
            if old_guess[i] == char:
                unmoved_count += 1

    # invalid case: wrong number of repeated colors from prev guess
    if pintersection != black_count + white_count:
        return False

    # invalid case: wrong number of colors shifted
    if unmoved_count != black_count or \
       pintersection - unmoved_count != white_count:
        return False

    return True

print(is_valid_guess('2222', '3333', 'BB'))
