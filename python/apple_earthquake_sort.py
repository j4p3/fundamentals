# Quake sorter
#
# Operation:
# python3 apple_earthquake_sort.py --top5
#   Returns top 5 earthquake states
#
# python3 apple_earthquake_sort.py --[state]
#   Returns top 25 earthquakes in given state
#

import urllib.request
import urllib.parse
import sys
import json
import collections
import datetime

API_URL = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
STATE_QUANITITY = 5
QUAKE_QUANTITY = 25
DEFAULT_STATE = 'California'


def parse_state(quake: 'Dict') -> 'String':
    """Retrieve state string from quake object
    """
    return quake['properties']['place'].split(' ')[-1]


def get_quakes(url=API_URL) -> 'List':
    """Retrieve quakes from web URL
    """
    print('Downloading quakes')
    req = urllib.request.urlopen(url)
    res = req.read().decode('utf-8')
    data = json.loads(res)
    if data:
        print('Quakes downloaded')
        return data['features']
    return None


def top_quake_states(state_quantity: 'Int', quakes: 'List[Dict]]') -> 'List':
    """Highest frequency <state_quantity> states for quakes
    """
    print('Analyzing quakes')
    quake_map = collections.defaultdict(int)

    for quake in quakes:
        quake_map[parse_state(quake)] += 1

    return sorted(quake_map.items(),
                  key=lambda s: s[1],
                  reverse=True)[:state_quantity]


def top_quakes_in(state: 'String', quantity: 'Int', quakes: 'List[Dict]]'):
    """Highest <quantity> magnitude quakes in <state>
    """
    print('Analyzing quakes in %s' % state)
    state_quakes = []

    for quake in quakes:
        if (parse_state(quake) == state):
            state_quakes.append({
                'magnitude': quake['properties']['mag'],
                'time': datetime.datetime.fromtimestamp(
                    quake['properties']['time'] / 1000.0,
                    datetime.timezone(
                        datetime.timedelta(minutes=-600))).isoformat(),
                'location': quake['properties']['place'],
            })

    return sorted(state_quakes,
                  key=lambda q: q['magnitude'],
                  reverse=True)[:quantity]


def sort_quakes(mode='ranked', **kwargs):
    """Return earthquakes or states for the given analysis mode
    """
    quakes = get_quakes()

    if mode == 'state':
        state_quakes = top_quakes_in(kwargs['state'], QUAKE_QUANTITY, quakes)
        return '\n'.join(map(lambda q: ' %s: %s, %s' % (
            q['magnitude'],
            q['location'],
            q['time']),
            state_quakes))

    states = top_quake_states(STATE_QUANITITY, quakes)
    return '\n'.join(map(lambda s: '%s: %d' % (s[0], s[1]), states))


if __name__ == '__main__':

    mode = 'ranked'
    state = None

    options = sys.argv

    if len(options) > 1:
        arg = options[1].split('--')[1]
        if arg == 'top5':
            mode = 'ranked'
        else:
            mode = 'state'
            state = arg.capitalize()

    result = sort_quakes(mode, **{'state': state})

    print('-'*25)
    print(result)
