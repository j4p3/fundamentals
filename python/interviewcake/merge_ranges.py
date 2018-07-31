import unittest
# import functools


# def _draw_agendas(booked_times, booking):
#     """
#     booked_times: dict{int: [bool]}
#     booking: tuple(int, int)

#     Accept next booking. Return full dict of all bookings.
#     O(n)
#     """
#     if booking[0] in booked_times:
#         booked_times[booking[0]].append(True)
#     else:
#         booked_times[booking[0]] = [True]
#     if booking[1] in booked_times:
#         booked_times[booking[1]].append(False)
#     else:
#         booked_times[booking[1]] = [False]

#     if booking[1] > booked_times['last']:
#         booked_times['last'] = booking[1]

#     return booked_times


# def _create_slots_from_agenda(agenda):
#     """
#     agenda: {int: [bool]}
#     Accept full dict of all bookings

#     Return list of start/end times for merged bookings
#     O(n)?
#     Maybe worst-case O(n^2) if everything starts/ends at the same time
#     """
#     schedule = []
#     events_underway = []
#     last_event_ending = agenda.pop('last') + 1
#     for i in range(0, last_event_ending):
#         if i in agenda:
#             for e in agenda[i]:
#                 if (e is True):
#                     events_underway.append(i)
#                 elif (e is False):
#                     start = events_underway.pop()
#                     if len(events_underway) == 0:
#                         schedule.append((start, i))
#     return schedule


# def merge_ranges(ranges):
#     agenda = functools.reduce(_draw_agendas, ranges, {'last': 0})
#     merged_slots = _create_slots_from_agenda(agenda)

#     return merged_slots

def merge_ranges(ranges):
    """Merge a list of tuples into a list of unions of those tuples

    Strategies:
        * build some unified thing encompassing all ranges
            and just glom the new ranges onto it
            O(n), if we can get O(1) writes
        * some kind of pairing/splitting thing
            i.e. give me union of these halves, then its halves
            nlogn
        * a naive glom-with-next approach on a *sorted* list
    """
    ranges.sort(key=lambda el: el[0])
    merged_meetings = []
    last_meeting = ranges[0]

    for meeting in ranges[1:]:
        # with sort, we know start(i) <= start(i+1)
        meeting
        if meeting[0] <= last_meeting[1]:
            last_meeting = (
                last_meeting[0],
                max(last_meeting[1], meeting[1])
            )
        else:
            merged_meetings.append(last_meeting)
            last_meeting = meeting
    merged_meetings.append(last_meeting)

    return merged_meetings


# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
