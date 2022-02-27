def solution(p, s):
    people = sum(p)
    min_cars = [0] + [float('inf')] * (people)

    for seating in range(max(s)):
        min_cars[seating] = 1

    for i in range(people + 1):
        for j in s:
            if i - j > 0 and min_cars[i - j] + 1 < min_cars[i]:
                min_cars[i] = min_cars[i - j] + 1
    
    for i in range(people + 1):
        print((i, min_cars[i]))
    return min_cars[-1]
