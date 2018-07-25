"""
Merge a list of tuples representing timeslots

ideas:
    some kind of lookup on each possible slot, incrementing where occupied
    could be O(n)?

    no, there's a specification that these range values don't have upper bound

    throw them all in a hash table? - doesn't seem useful
    tree? no need to sort, really. would need representation of full block
    linked list of full range? again, size. also, why
    I've literally done this before. for DayWon.

    reduce the list? check if contiguous, modify/insert?

    what type of data structure can really represent these ranges?
    some kind of float or something?

    not tuples. useful as input, not writeable.

    set up a dict. set keys as all meeting start/ends.
    iterate through keys IN ORDER, creating/ending tuples as necessary.

    works, but sorting would be nlogn without constrained space.

    can avoid sorting - just keep track of max time.
    then increment through all possible keys.
    keep a stack/count of how many events are currently running
    for multiple overlaps
"""

import unittest
import functools


def _draw_agendas(booked_times, booking):
    """
    booked_times: dict{int: [bool]}
    booking: tuple(int, int)

    Accept next booking. Return full dict of all bookings.
    O(n)
    """
    if booking[0] in booked_times:
        booked_times[booking[0]].append(True)
    else:
        booked_times[booking[0]] = [True]
    if booking[1] in booked_times:
        booked_times[booking[1]].append(False)
    else:
        booked_times[booking[1]] = [False]

    if booking[1] > booked_times['last']:
        booked_times['last'] = booking[1]

    return booked_times


def _create_slots_from_agenda(agenda):
    """
    agenda: {int: [bool]}
    Accept full dict of all bookings

    Return list of start/end times for merged bookings
    O(n)?
    Maybe worst-case O(n^2) if everything starts/ends at the same time
    """
    schedule = []
    events_underway = []
    last_event_ending = agenda.pop('last') + 1
    for i in range(0, last_event_ending):
        if i in agenda:
            for e in agenda[i]:
                if (e is True):
                    events_underway.append(i)
                elif (e is False):
                    start = events_underway.pop()
                    if len(events_underway) == 0:
                        schedule.append((start, i))
    return schedule


def merge_ranges(ranges):
    agenda = functools.reduce(_draw_agendas, ranges, {'last': 0})
    merged_slots = _create_slots_from_agenda(agenda)

    return merged_slots


class Test(unittest.TestCase):

    MEETING_TIMES = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

    def test_merge_ranges(self):
        self.assertEqual(merge_ranges([(1, 10), (2, 6), (3, 5), (7, 9)]),
                         [(1, 10)])
        self.assertEqual(merge_ranges(self.MEETING_TIMES),
                         [(0, 1), (3, 8), (9, 12)])


unittest.main(verbosity=2)
